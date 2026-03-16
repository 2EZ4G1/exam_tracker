from django.shortcuts import render, redirect
from .models import Exam, Marks, SubjectMarks
from .forms import ExamForm, MarksForm, SubjectForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def index(request):
    return render(request, 'exam_tracker/index.html')

# for exams to be viewed
@login_required
def exams(request):
    exams = Exam.objects.filter(owner=request.user).order_by('date_added')
    context = {'exams':exams}
    return render(request, 'exam_tracker/exams.html', context)

@login_required
def marks(request,exam_id):
    exam = Exam.objects.get(id=exam_id)
    # Make sure the topic belongs to the current user.
    if exam.owner != request.user:
        raise Http404
    totalmarks = exam.marks_set.order_by('-date_added')
    context = {'exam':exam, 'marks':totalmarks}
    return render(request, 'exam_tracker/marks.html', context)
@login_required
def submarks(request,exam_id,marks_id):
    exam = Exam.objects.get(id=exam_id)
    if exam.owner != request.user:
        raise Http404
    marks = Marks.objects.get(id=marks_id)
    submarks = marks.subjectmarks_set.all()
    context = {'exam':exam,'marks':marks, 'submarks':submarks}
    return render(request, 'exam_tracker/subjects.html',context)
@login_required
def new_exams(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = ExamForm()
    else:
        form = ExamForm(data=request.POST)
        if form.is_valid():
            new_exam = form.save(commit=False)
            new_exam.owner = request.user
            new_exam.save()
            return redirect('exam_tracker:exams')
        
        #Display a blank or invalid form.
    context = {'form':form}
    return render(request, 'exam_tracker/new_exams.html',context)

def new_marks(request,exam_id):
    exam = Exam.objects.get(id=exam_id)

    if request.method != 'POST':
        form = MarksForm()

    else:
        form = MarksForm(data=request.POST)
        if form.is_valid():
            new_marks = form.save(commit=False)
            new_marks.exam = exam
            new_marks.save()
            return redirect('exam_tracker:marks',exam_id=exam_id)
        
    context = {'exam':exam,'form':form}
    return render(request, 'exam_tracker/new_marks.html',context)
@login_required
def new_submarks(request,exam_id,marks_id):
    exam = Exam.objects.get(id=exam_id)
    marks = Marks.objects.get(id=marks_id)

    if request.method != 'POST':
        form = SubjectForm()
    else:
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            new_marks = form.save(commit=False)
            new_marks.marks = marks
            new_marks.save()
            return redirect('exam_tracker:subjects',exam_id=exam_id, marks_id=marks_id)
        
    context = {'exam':exam, 'marks':marks, 'form':form}
    return render(request, 'exam_tracker/new_submarks.html',context)
