from django.contrib import admin
from .models import Developer

# Register your models here.

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','password')
