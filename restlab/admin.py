from django.contrib import admin
from .models import Patient, CustomUser, ProjectSubmission, Student

admin.site.register(Patient)
admin.site.register(CustomUser)
admin.site.register(ProjectSubmission)
admin.site.register(Student)
