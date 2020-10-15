from django.contrib import admin
from .models import person,education,experience,resume,projects

@admin.register(person,education,experience,resume,projects)
class UserAdmin(admin.ModelAdmin):
    #list_display=['firstname','lastname']
    pass
