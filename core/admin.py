from django.contrib import admin

from .models import Meeting, Meeting_Request

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Meeting_Request)
