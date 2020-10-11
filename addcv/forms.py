from django import forms
from . models import person

class personalform(forms.ModelForm):
     class Meta:
          model = person
          fields='__all__'
