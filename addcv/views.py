from django.shortcuts import render
from .forms import personalform, educationform, experienceform, projectform
from .models import experience, education, person,projects
from django.contrib import messages
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime

def createcv(request):
    return render(request, 'addcv/cv.html')
def personal(request):
    if request.method == 'POST':

        fm = personalform(request.POST)

        #em = educationform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by = request.user
            instance.save()
            person_id = instance.id
            messages.success(request,'Your personal details has been added')
        return render(request,'addcv/moredetails.html',{'person_id':person_id})
    else:
        fm = personalform()
        #em = educationform()
        return render(request,'addcv/personal.html',{'form':fm})

def updatepersonal(request,person_id):
    per = person.objects.get(id=person_id)
    fm = personalform(instance=per)
    if request.method == 'POST':

        fm = personalform(request.POST, instance=per)

        #em = educationform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by = request.user
            instance.save()
            person_id=instance.id
            return redirect('/')
    return render(request,'addcv/personal.html',{'form':fm})

def deletepersonal(request, person_id):
    per = person.objects.get(id=person_id)
    if request.method == 'POST':
        per.delete()
        messages.success(request,'The information has been deleted')
        return redirect('dashboard')
    return render(request,'addcv/delete.html')
  

def educational(request,person_id):
    if request.method == 'POST':
        fm = educationform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance = fm.save(commit=False)
            instance.added_by = current_person
            instance.save()
        return render(request, 'addcv/educational.html', {'form':fm})
    else:
        fm = educationform()
        #em = educationform()
        return render(request,'addcv/educational.html',{'form':fm})

def deleteeducation(request, person_id, edu_id):
    edu = education.objects.get(id=edu_id)
    if request.method == 'POST':
        edu.delete()
        current_person = person.objects.get(id=person_id)
        cont = education.objects.filter(added_by=current_person)
        context = experience.objects.filter(added_by=current_person)
        pro = projects.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
        'projects':pro,'person_id':person_id})
    return render(request, 'addcv/deleteeducation.html')
    
def deleteexperience(request, person_id, exp_id):
    exp = experience.objects.get(id=exp_id)
    if request.method == 'POST':
        exp.delete()
        current_person = person.objects.get(id=person_id)
        cont = education.objects.filter(added_by=current_person)
        context = experience.objects.filter(added_by=current_person)
        pro = projects.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
        'projects':pro,'person_id':person_id})
    return render(request,'addcv/deleteeducation.html')

def edudashboard(request,test_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user,id=test_id)
    print(current_person)
    content = education.objects.filter(added_by=current_person)
    return render (request, 'addcv/edudashboard.html',{'content':content})

def prodashboard(request):
    current_user = request.user
    content = projects.objects.filter(added_by=current_user)
    return render (request, 'addcv/prodashboard.html',{'content':content})

def jobdashboard(request):
    current_user = request.user
    print(current_user)
    content = experience.objects.filter(added_by=current_user)
    return render (request, 'addcv/jobdashboard.html',{'content':content})

def experiences(request,person_id):
    if request.method == 'POST':
        fm = experienceform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance.added_by = current_person
            instance.save()
        return render(request,'addcv/experience.html',{'form':fm})
    else:
        fm = experienceform()
        return render(request,'addcv/experience.html',{'form':fm})

def project(request,person_id):
    if request.method == 'POST':
        fm = projectform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance.added_by = current_person
            instance.save()
        return render(request,'addcv/project.html',{'form':fm})
    else:
        fm = projectform()
        #em = educationform()
        return render(request, 'addcv/project.html', {'form': fm})
        
def upproject(request,person_id,pro_id):
    pro = projects.objects.get(id=pro_id)
    fm = projectform(instance=pro)
    if request.method == 'POST':
        fm = projectform(request.POST, instance=pro)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by=person.objects.get(id=person_id)
            instance.save()
            return redirect('/')
    return render(request, 'addcv/project.html', {'form': fm})
    
def updateeducation(request,person_id,edu_id):
    edu = education.objects.get(id=edu_id)
    fm = educationform(instance=edu)
    if request.method == 'POST':
        fm = educationform(request.POST, instance=edu)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by=person.objects.get(id=person_id)
            instance.save()
            return redirect('/')
    return render(request, 'addcv/educational.html', {'form': fm})
    
def updateexperience(request,person_id,exp_id):
    exp = experience.objects.get(id=exp_id)
    fm = experienceform(instance=exp)
    if request.method == 'POST':
        fm = experienceform(request.POST, instance=exp)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by=person.objects.get(id=person_id)
            instance.save()
            return redirect('/')
    return render(request,'addcv/experience.html',{'form':fm})

def makecv(request,test_id):
    user = request.user
    print(user)
    ed = user.education_set.all()
    return render(request, 'addcv/personaledit.html', {'op': ed})

def dashboard(request):
    current_user = request.user
    person1 = person.objects.filter(added_by=current_user)
    return render(request,'addcv/dashboard.html',{'persons':person1})

def personaldash(request,person_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user,id=person_id)
    print(current_person)
    cont = education.objects.filter(added_by=current_person)
    context = experience.objects.filter(added_by=current_person)
    pro = projects.objects.filter(added_by=current_person)
    return render (request, 'addcv/persondashboard.html',{'contents':cont,'experiences':context,'projects':pro,'person_id':person_id})



# Create your views here.

# def export_pdf(request):

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; attachment; filename=Addcv'+\
#         str(datetime.datetime.now())+'.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'


#     html_string=render_to_string('resumes/2/pdf-output.html')
#     html=HTML(string=html_string)

#     result = html.write_pdf()


#     with tempfile.NamedTemporaryFile(delete=True)as output:
#         output.write(result)
#         output.flush()

#         output=open(output.name,'rb')

#         response.write(output.read())


#     return response
