from django import forms
from . models import person
 
class personalform(forms.ModelForm):
     class Meta:
          model = person
          fields=['firstname','lastname']
class educationform(forms.Form):
     school = forms.CharField(max_length=100,required=False)
     college= forms.CharField(max_length=100)