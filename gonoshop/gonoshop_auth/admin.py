from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# Register your models here.
@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display=['email', 'first_name', 'last_name', 'username', 'is_active', 'is_staff']