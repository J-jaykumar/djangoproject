from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=50)
    collagename = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    mobilenum = models.IntegerField()
    def __str__(self) :
        return self.studentname