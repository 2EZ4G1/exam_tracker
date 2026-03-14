from django.contrib import admin

# Register your models here.
from .models import Exam, Marks, SubjectMarks
admin.site.register(Exam)
admin.site.register(Marks)
admin.site.register(SubjectMarks)