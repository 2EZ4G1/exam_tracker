from django import forms

from .models import Exam, Marks, SubjectMarks

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam']
        labels = {'exam':'Exam Name'}

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['total_marks','percentile']
        labels = {'total_marks':'Total Marks','percentile':'Percentile'}

class SubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectMarks
        fields = ['english','reasoning','maths','general_studies']
        labels = {'english':'English','reasoning':'Reasoning','maths':'Maths','general_studies':'GS'}