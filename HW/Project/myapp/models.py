from django.db import models


class Student(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    birth_date = models.IntegerField()
    gpa= models.FloatField()


