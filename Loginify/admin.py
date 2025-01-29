from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserDetails

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']