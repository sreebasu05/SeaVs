from django.urls import path
from . import views


urlpatterns = [
     ##################### FORMS ########################
     path('personal/', views.personal,name='personal'), #personal form
     path('education/<int:person_id>', views.educational,name='ed'),   #education form
     path('experiences/<int:person_id>', views.experiences, name='ex'),  #job form
     path('project/<int:person_id>', views.project, name='project'),  #project form
     path('skill/<int:person_id>', views.skill_person,name='skill'),   #skill form

     ##################### DASHBOARD TOOLS ########################
     path('userdash/', views.dashboard,name='dashboard'),
     path('updatepersonal/<int:person_id>', views.updatepersonal,name='updatepersonal'),
     path('deletepersonal/<int:person_id>', views.deletepersonal,name='deletepersonal'),
     path('showcv/<int:person_id>', views.showcv, name='showcv'),
     path('showmycv/<int:person_id>', views.showmycv, name='showmycv'),
     path('changetemp/<int:person_id>', views.changetemp, name='changetemp'),


     path('persondash/<int:person_id>', views.personaldash, name='persondash'),
     path('updateeducation/<int:person_id>/<int:edu_id>', views.updateeducation, name='updateeducation'),
     path('deleteeducation/<int:person_id>/<int:edu_id>', views.deleteeducation, name='deleteeducation'),
     path('updateexperience/<int:person_id>/<int:exp_id>', views.updateexperience, name='updateexperience'),
     path('deleteexperience/<int:person_id>/<int:exp_id>', views.deleteexperience, name='deleteexperience'),
     path('updateproject/<int:person_id>/<int:pro_id>', views.updateproject, name='updateproject'),
     path('deleteproject/<int:person_id>/<int:pro_id>', views.deleteproject, name='deleteproject'),
     path('updateskill/<int:person_id>/<int:skill_id>', views.updateskill, name='updateskill'),
     path('deleteskill/<int:person_id>/<int:skill_id>', views.deleteskill, name='deleteskill'),


     ##################### CV CREATION ########################
     path('templist', views.templist, name='templist'),
      path('mycv/<int:person_id>/<int:my_id>', views.mycv, name='mycv'),

     #############################################-old



     path('',views.createcv, name='create-cv-page'),    #createcv page




   #   path('madecv/',views.cv,name='cv'),                #cv2
     path('export-pdf/<int:person_id>/', views.export_pdf, name='export-pdf'),
 ]
