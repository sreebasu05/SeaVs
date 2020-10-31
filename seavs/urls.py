from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='seavs-homepage'), #home page
    path('contactus/', views.contactus, name='contactus'),
]
