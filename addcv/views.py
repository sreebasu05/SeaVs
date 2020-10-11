from django.shortcuts import render
from .forms import personalform
from .models import person

def adddetail(request):
    if request.method == 'POST':
        fm = personalform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
            print('form is valid')
            content = {
                'firstname':fm.cleaned_data['firstname'],
                'lastname':fm.cleaned_data['lastname'],
                'profession':fm.cleaned_data['profession'],
                'city':fm.cleaned_data['city'],
                'state':fm.cleaned_data['state'],
                'pincode':fm.cleaned_data['pincode'],
                'phoneno':fm.cleaned_data['phoneno'],
            }

            #reg = person(firstname=firstname, lastname=lastname)
            #reg.save()

        #if em.is_valid():
        #    school = em.cleaned_data['school']
        #    college = em.cleaned_data['college']
        #    print(college)
        #    print(school)
        return render(request, 'resumes/2/index.html', content)
    else:
        fm = personalform()
        #em = educationform()
        return render(request,'addcv/personal.html',{'form':fm})

# Create your views here.
