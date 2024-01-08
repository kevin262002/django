from django.db import models


class Member(models.Model):
  firstname = models.CharField(max_length=25)
  lastname = models.CharField(max_length=25)
  city = models.CharField(max_length=20)



    