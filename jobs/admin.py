from django.contrib import admin
from .models import Job  # import Job model to manage database data in django admin


admin.site.register(Job)  # model register format for django admin
