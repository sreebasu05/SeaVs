from django.shortcuts import render
from .models import contact
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'seavs/home.html')

def contactus(request):
    if request.method == 'POST':
        Name = request.POST['name1']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Content = request.POST['content']
        if len(Name) < 2 or len(Email) < 4 or len(Phone) < 10 or len(Content) < 4:
            messages.error(request, 'Please enter valid data')
        else:
            Contact=contact(name=Name,email=Email,phone=Phone,content=Content)
            Contact.save()
            messages.success(request,'Your message has been send successfully')
    return render(request,'seavs/contact.html')
