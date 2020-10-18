from django import forms
from . models import person, education, experience, resume, projects

#All the forms used
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

class projectform(forms.ModelForm):
    class Meta:
        model = projects
        fields='__all__'

class resumeform(forms.ModelForm):

    class Meta:
        model = resume
        fields='__all__'
