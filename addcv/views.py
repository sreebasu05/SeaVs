from django.shortcuts import render,redirect
from .forms import personalform, educationform, experienceform, projectform,skillform
from .models import experience, education, person,projects,skill,temp
from django.contrib import messages
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime

##################### FORM VIEWS ########################
def personal(request):
    if request.method == 'POST':
        fm = personalform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by = request.user
            instance.save()
            person_id = instance.id
            messages.success(request,'Your personal details has been added')
            return render(request,'addcv/showcv.html',{'person_id':person_id})
    else:
        fm = personalform()
        return render(request, 'form/personal.html', {'form': fm})

def educational(request,person_id):
    if request.method == 'POST':
        fm = educationform(request.POST)
        if fm.is_valid():
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance = fm.save(commit=False)
            instance.added_by = current_person
            instance.save()
            messages.success(request,'Your education has been added')
        return render(request,'addcv/moredetails.html',{'person_id':person_id})
    else:
        fm = educationform()
        return render(request,'form/educational.html',{'form':fm})

def experiences(request,person_id):
    if request.method == 'POST':
        fm = experienceform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance.added_by = current_person
            instance.save()
            messages.success(request,'Your experience has been added')
        return render(request,'addcv/moredetails.html',{'person_id':person_id})
    else:
        fm = experienceform()
        return render(request, 'form/experience.html', {'form': fm})

def project(request,person_id):
    if request.method == 'POST':
        fm = projectform(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance.added_by = current_person
            instance.save()
            messages.success(request,'Your project has been added')
        return render(request,'addcv/moredetails.html',{'person_id':person_id})
    else:
        fm = projectform()
        return render(request, 'form/project.html', {'form': fm})

def skill_person(request,person_id):
    if request.method == 'POST':
        fm = skillform(request.POST)
        if fm.is_valid():
            current_user=request.user
            current_person = person.objects.get(added_by=current_user,id=person_id)
            instance = fm.save(commit=False)
            instance.added_by = current_person
            instance.save()
            messages.success(request,'Your project has been added')
        return render(request,'addcv/moredetails.html',{'person_id':person_id})
    else:
        fm = skillform()
        return render(request,'addcv/skill.html',{'form':fm})

##################### PERSON DASHBOARD ########################

def dashboard(request):
    current_user = request.user
    person1 = person.objects.filter(added_by=current_user)
    return render(request,'addcv/dashboard.html',{'persons':person1})

def updatepersonal(request,person_id):
    per = person.objects.get(id=person_id)
    fm = personalform(instance=per)
    if request.method == 'POST':
        fm = personalform(request.POST, instance=per)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by = request.user
            instance.save()
            person_id = instance.id
            current_user=request.user
            per=person.objects.filter(added_by=current_user)
            messages.danger(request,'The information has been updated')
        return render(request,'addcv/dashboard.html',{'persons':per})

    return render(request,'form/personal.html',{'form':fm})

def deletepersonal(request, person_id):
    per = person.objects.get(id=person_id)
    current_user=request.user
    if request.method == 'POST':
        per.delete()
        per=person.objects.filter(added_by=current_user)
        messages.success(request,'The information has been deleted')
        return render(request,'addcv/dashboard.html',{'persons':per})
    return render(request,'addcv/delete.html',{'per':per})

def personaldash(request,person_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user,id=person_id)
    print(current_person)
    cont = education.objects.filter(added_by=current_person)
    context = experience.objects.filter(added_by=current_person)
    pro = projects.objects.filter(added_by=current_person)
    ski = skill.objects.filter(added_by=current_person)
    return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
    'projects':pro,'person_id':person_id,'skills':ski})

def updateeducation(request,person_id,edu_id):
    edu = education.objects.get(id=edu_id)
    fm = educationform(instance=edu)
    if request.method == 'POST':
        fm = educationform(request.POST, instance=edu)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by=person.objects.get(id=person_id)
            instance.save()
            current_person = person.objects.get(id=person_id)
            cont = education.objects.filter(added_by=current_person)
            context = experience.objects.filter(added_by=current_person)
            pro = projects.objects.filter(added_by=current_person)
            ski = skill.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
            'projects':pro,'person_id':person_id,'skills':ski})

    return render(request, 'form/educational.html', {'form': fm})

def deleteeducation(request, person_id, edu_id):
    edu = education.objects.get(id=edu_id)
    if request.method == 'POST':
        edu.delete()
        current_person = person.objects.get(id=person_id)
        cont = education.objects.filter(added_by=current_person)
        context = experience.objects.filter(added_by=current_person)
        pro = projects.objects.filter(added_by=current_person)
        ski = skill.objects.filter(added_by=current_person)
    return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
        'projects':pro,'person_id':person_id,'skills':ski})
    return render(request, 'addcv/deleteeducation.html')

def updateexperience(request,person_id,exp_id):
    exp = experience.objects.get(id=exp_id)
    fm = experienceform(instance=exp)
    if request.method == 'POST':
        fm = experienceform(request.POST, instance=exp)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by=person.objects.get(id=person_id)
            instance.save()
            current_person = person.objects.get(id=person_id)
            cont = education.objects.filter(added_by=current_person)
            context = experience.objects.filter(added_by=current_person)
            pro = projects.objects.filter(added_by=current_person)
            ski = skill.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
            'projects':pro,'person_id':person_id,'skills':ski})
    return render(request, 'form/experience.html', {'form': fm})

def deleteexperience(request, person_id, exp_id):
    exp = experience.objects.get(id=exp_id)
    if request.method == 'POST':
        exp.delete()
        current_person = person.objects.get(id=person_id)
        cont = education.objects.filter(added_by=current_person)
        context = experience.objects.filter(added_by=current_person)
        pro = projects.objects.filter(added_by=current_person)
        ski = skill.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
        'projects':pro,'person_id':person_id,'skills':ski})
    return render(request,'addcv/deleteeducation.html')

def updateproject(request,person_id,pro_id):
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

def deleteproject(request, person_id, pro_id):
    pro = projects.objects.get(id=pro_id)
    if request.method == 'POST':
        pro.delete()
        current_person = person.objects.get(id=person_id)
        cont = education.objects.filter(added_by=current_person)
        context = experience.objects.filter(added_by=current_person)
        pro = projects.objects.filter(added_by=current_person)
        ski = skill.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
        'projects':pro,'person_id':person_id,'skills':ski})
    return render(request, 'addcv/deleteeducation.html')

def updateskill(request, person_id, skill_id):
    ski = skill.objects.get(id=skill_id)
    fm = skillform(instance=ski)
    if request.method == 'POST':
        fm = skillform(request.POST, instance=ski)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.added_by=person.objects.get(id=person_id)
            instance.save()
            current_person = person.objects.get(id=person_id)
            cont = education.objects.filter(added_by=current_person)
            context = experience.objects.filter(added_by=current_person)
            pro = projects.objects.filter(added_by=current_person)
            ski = skill.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
            'projects':pro,'person_id':person_id,'skills':ski})
    return render(request, 'addcv/skill.html', {'form': fm})

def deleteskill(request, person_id, skill_id):
    ski = skill.objects.get(id=skill_id)
    if request.method == 'POST':
        ski.delete()
        current_person = person.objects.get(id=person_id)
        cont = education.objects.filter(added_by=current_person)
        context = experience.objects.filter(added_by=current_person)
        pro = projects.objects.filter(added_by=current_person)
        ski = skill.objects.filter(added_by=current_person)
        return render(request, 'addcv/persondashboard.html', {'contents': cont, 'experiences': context,
        'projects':pro,'person_id':person_id,'skills':ski})
    return render(request, 'addcv/deleteeducation.html')

##################### CV CREATION ########################
def templist(request):
    return render(request, 'resumes/templist.html')
def mycv(request, person_id, my_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user,id=person_id)
    cont = education.objects.filter(added_by=current_person)
    context = experience.objects.filter(added_by=current_person)
    pro = projects.objects.filter(added_by=current_person)
    ski=skill.objects.filter(added_by=current_person)
    if my_id == 1:
        return render(request, 'resumes/1/index.html', {'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    if my_id == 2:
        return render(request,'resumes/2/index.html', {'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    if my_id == 3:
        return render(request, 'resumes/3/index.html', {'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})


####################################################################- old
def createcv(request):
    return render(request, 'addcv/cv.html')

def templist(request):
    return render(request,'resumes/templist.html')



def showcv(request, person_id):
    return render(request, 'addcv/showcv.html', {'person_id': person_id})

def mycv(request, person_id, my_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user, id=person_id)
    temp_obj = temp.objects.filter(added_by=current_person)
    if temp_obj.count:
        temp_obj.delete()
    temp_obj=temp.objects.create(added_by=current_person,temp_id=my_id)

    return render(request, 'addcv/moredetails.html', {'person_id': person_id})

def showmycv(request, person_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user, id=person_id)
    temp_obj=temp.objects.get(added_by=current_person)
    my_id=temp_obj.temp_id
    cont = education.objects.filter(added_by=current_person)
    context = experience.objects.filter(added_by=current_person)
    pro = projects.objects.filter(added_by=current_person)
    ski = skill.objects.filter(added_by=current_person)
    if my_id == 1:
        return render(request, 'resumes/1/index.html', {'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    if my_id == 2:
        return render(request, 'resumes/2/index.html', {'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    if my_id == 3:
        return render(request, 'resumes/3/index.html', {'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})

def changetemp(request, person_id):
    return render(request, 'addcv/showcv.html', {'person_id': person_id})



def export_pdf(request, person_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user, id=person_id)
    temp_obj=temp.objects.get(added_by=current_person)
    my_id=temp_obj.temp_id
    cont = education.objects.filter(added_by=current_person)
    context = experience.objects.filter(added_by=current_person)
    pro = projects.objects.filter(added_by=current_person)
    ski=skill.objects.filter(added_by=current_person)

def export_pdf(request, person_id,my_id):
    current_user = request.user
    current_person = person.objects.get(added_by=current_user,id=person_id)
    cont = education.objects.filter(added_by=current_person)
    context = experience.objects.filter(added_by=current_person)
    pro = projects.objects.filter(added_by=current_person)
    ski=skill.objects.filter(added_by=current_person)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=resumes'+\
        str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    if my_id == 1:
        html_string=render_to_string('resumes/1/index.html',{'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    if my_id == 2:
        html_string=render_to_string('resumes/2/index.html',{'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    if my_id == 3:
        html_string=render_to_string('resumes/3/index.html',{'educations': cont, 'experiences': context,
        'projects': pro, 'person': current_person, 'skills': ski})
    # if my_id == 4:
    #     html_string=render_to_string('resumes/2/pdf-output.html',{'educations': cont, 'experiences': context,
    #     'projects': pro, 'person': current_person, 'skills': ski})
    # if my_id == 5:
    #     html_string=render_to_string('resumes/2/pdf-output.html',{'educations': cont, 'experiences': context,
    #     'projects': pro, 'person': current_person, 'skills': ski})
    # if my_id == 6:
    #     html_string=render_to_string('resumes/2/pdf-output.html',{'educations': cont, 'experiences': context,
    #     'projects': pro, 'person': current_person, 'skills': ski})
    # if my_id == 7:
    #     html_string=render_to_string('resumes/2/pdf-output.html',{'educations': cont, 'experiences': context,
    #     'projects': pro, 'person': current_person, 'skills': ski})
    # if my_id == 8:
    #     html_string=render_to_string('resumes/2/pdf-output.html',{'educations': cont, 'experiences': context,
    #     'projects': pro, 'person': current_person, 'skills': ski})

    html=HTML(string=html_string)

    result = html.write_pdf()


    with tempfile.NamedTemporaryFile(delete=True)as output:
        output.write(result)
        output.flush()

        output=open(output.name,'rb')

        response.write(output.read())


    return response
