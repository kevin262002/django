from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=25)
  lastname = models.CharField(max_length=25)
  roll_number = models.IntegerField()
  age = models.IntegerField()
  subject = models.CharField(max_length=25)
  city = models.CharField(max_length=25)
