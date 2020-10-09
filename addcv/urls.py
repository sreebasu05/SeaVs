from django.urls import path
from . import views


urlpatterns = [
     path('', views.adddetail,name='adddetail'),
 ]
