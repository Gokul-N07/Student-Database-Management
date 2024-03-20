from django.db import models

# Create your models here.

class Student(models.Model):
    Student_No = models.IntegerField()
    Student_Name = models.CharField(max_length = 20)
    Student_Year = models.CharField(max_length = 10)
    Student_Dept = models.CharField(max_length = 10)