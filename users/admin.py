from django.contrib import admin
from .models import Student, Interviewer, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Interviewer)