from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):
    exam = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.exam
    
class Marks(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    total_marks = models.FloatField()
    percentile = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'marks'

    def __str__(self):
        return f"Total Marks:{self.total_marks}      Percentile:{self.percentile}"
    
class SubjectMarks(models.Model):
    marks = models.ForeignKey(Marks, on_delete=models.CASCADE)
    english = models.FloatField()
    maths = models.FloatField()
    reasoning = models.FloatField()
    general_studies = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Subject wise marks'

    def __str__(self):
        return f"English:{self.english} Maths:{self.maths} Reasoning:{self.reasoning} GS:{self.general_studies}"