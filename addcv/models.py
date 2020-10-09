from django.db import models

class person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)

# Create your models here.
