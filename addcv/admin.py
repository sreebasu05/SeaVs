from django.contrib import admin
from .models import person

@admin.register(person)
class UserAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname']
