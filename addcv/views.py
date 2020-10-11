from django.shortcuts import render
from .forms import personalform, educationform, experienceform, whole
from .models import experience, education, person
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
import datetime


def personal(request):
    if request.method == 'POST':
        fm = personalform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
            fm.save()
            _ = {
                'firstname':fm.cleaned_data['firstname'],
                'lastname':fm.cleaned_data['lastname'],
                'profession':fm.cleaned_data['profession'],
                'city':fm.cleaned_data['city'],
                'state':fm.cleaned_data['state'],
                'pincode':fm.cleaned_data['pincode'],
                'phoneno':fm.cleaned_data['phoneno'],
            }

        return render(request,'addcv/personal.html',{'form':fm})
    else:
        fm = personalform()
        #em = educationform()
        return render(request,'addcv/personal.html',{'form':fm})


def educational(request):
    if request.method == 'POST':
        fm = educationform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
            print("school")
            fm.save()
            _ = {
                'institute':fm.cleaned_data['institute'],
                'startingyear':fm.cleaned_data['startingyear'],
                'endingyear':fm.cleaned_data['endingyear'],
                'grade':fm.cleaned_data['grade'],
                'course':fm.cleaned_data['course']
            }

        return render(request, 'addcv/personal.html', {'form':fm})
    else:
        fm = educationform()
        #em = educationform()
        return render(request,'addcv/personal.html',{'form':fm})

def experiences(request):
    if request.method == 'POST':
        fm = experienceform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
        #    print('form is valid')
        #    content = {
        #        'company':fm.cleaned_data['company'],
        #        'startingyear':fm.cleaned_data['startingyear'],
        #        'endingyear':fm.cleaned_data['endingyear'],
        #        'post':fm.cleaned_data['post'],
        #        'details':fm.cleaned_data['details']
        #    }

            fm.save()
        return render(request,'addcv/personal.html',{'form':fm})
    else:
        fm = experienceform()
        #em = educationform()
        return render(request,'addcv/personal.html',{'form':fm})

def cv(request):
    context = {
        'persons': person.objects.all(),
        'experiences': experience.objects.all(),
        'educations' : education.objects.all()
    }
    return render(request, 'resumes/2/index.html', context)



# Create your views here.

def export_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Addcv'+\
        str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'


    html_string=render_to_string('addcv/pdf-output.html')
    html=HTML(string=html_string)

    result = html.write_pdf()


    with tempfile.NamedTemporaryFile(delete=True)as output:
        output.write(result)
        output.flush()

        output=open(output.name,'rb')

        response.write(output.read())


    return response
