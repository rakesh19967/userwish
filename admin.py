from django.contrib import admin
from WebApp.models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['Wish_List','Date']
admin.site.register(User,UserAdmin)