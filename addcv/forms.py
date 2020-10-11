from django import forms
from . models import person, education, experience,whole

class personalform(forms.ModelForm):
     class Meta:
          model = person
          fields='__all__'

class educationform(forms.ModelForm):
    class Meta:
        model = education
        fields='__all__'

class experienceform(forms.ModelForm):
    class Meta:
        model = experience
        fields='__all__'

class whole(forms.ModelForm):
    class Meta:
        model = whole
        fields='__all__'
