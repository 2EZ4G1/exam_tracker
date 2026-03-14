from django.urls import path

from . import views

app_name = 'exam_tracker'
urlpatterns = [
    path('',views.index, name = 'index' ),
    # A page that shows exams
    path('exams/',views.exams, name = 'exams'),
    # A page to show individual exams
    path('exams/<int:exam_id>/',views.marks,name = 'marks'),
    # A page to show marks of subjects in a test
    path('exams/<int:exam_id>/<int:marks_id>/',views.submarks, name = 'subjects'),
    # Page for adding a new exams.
    path('new_exams/', views.new_exams, name = 'new_exams'),
    # Page for adding new marks
    path('new_exams/<int:exam_id>/', views.new_marks, name = 'new_marks'),
    # Page for adding subject marks
    path('new_exams/<int:exam_id>/<int:marks_id>/', views.new_submarks, name = 'new_submarks'),
    
]