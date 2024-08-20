from django.db import models

# Create your models here.


class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    course = models.CharField(max_length=100) 
    marks = models.IntegerField()
    grade = models.CharField(max_length=10)


# class Teacher(models.Model):
#     teacherId = models.AutoField(primary_key=True)
#     fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     subject = models.CharField(max_length=10)
   


