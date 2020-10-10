from django.db import models

class person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.IntegerField(max_length=6)
    phoneno=models.IntegerField(max_length=9)
    emailid=models.EmailField()
    profile=models.TextField(max_length=100)
class education(models.Model):
    institute=models.CharField(max_length=40)
    startingyear=models.IntegerField(max_length=4)
    endingyear=models.IntegerField(max_length=4)
    grade=models.CharField(max_length=4)
    course=models.CharField(max_length=20)
class experience(models.Model):
    company=models.CharField(max_length=40)
    startingyear=models.IntegerField(max_length=4)
    endingyear=models.IntegerField(max_length=4)
    post=models.CharField(max_length=20)
    course=models.TextField(max_length=200)
class projects(models.Model):
    topic=models.CharField(max_length=40)
    startingyear=models.IntegerField(max_length=4)
    endingyear=models.IntegerField(max_length=4)
    details=models.TextField(max_length=200)

# Create your models here.
