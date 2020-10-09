from django.shortcuts import render
from .forms import personalform, educationform
from .models import person

def adddetail(request):
    if request.method == 'POST':
        fm = personalform(request.POST)
        em = educationform(request.POST)
        if fm.is_valid():
            print('form is valid')
            firstname=fm.cleaned_data['firstname']
            lastname=fm.cleaned_data['lastname']
            print(firstname)
            print(lastname)
            reg = person(firstname=firstname, lastname=lastname)
            reg.save()
        if em.is_valid():
            school = em.cleaned_data['school']
            college = em.cleaned_data['college']
            print(college)
            print(school)
        return render(request, 'addcv/added.html', {'name': firstname, "name2": lastname, "cname": college, "sname": school})     
    else:
        fm = personalform()
        em = educationform()
        return render(request,'addcv/add.html',{'form':fm,'form1':em})

# Create your views here.
