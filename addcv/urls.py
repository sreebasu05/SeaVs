from django.urls import path
from . import views


urlpatterns = [
     path('personal/', views.personal,name='personal'),
     path('education/', views.educational,name='ed'),
     path('experiences/', views.experiences,name='ex'),
     #path('projects/', views.projects,name='personal'),
     path('', views.cv,name='cv'),
 ]
