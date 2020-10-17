from django.contrib import admin
from .models import *

#registering the models
admin.site.register(person)
admin.site.register(education)
admin.site.register(experience)
admin.site.register(projects)
admin.site.register(resume)


#@admin.register(person,education,experience,projects,resume)
#class UserAdmin(admin.ModelAdmin):
#    pass
