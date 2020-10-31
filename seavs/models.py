from django.db import models

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField(max_length=13)
    
    def __str__(self):
       return self.name
