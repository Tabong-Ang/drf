from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
# This will allow the Student model to be managed through the Django admin interface.