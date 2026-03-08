from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Patient(models.Model):
    patient_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    dob = models.DateField() 
    doctor_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} - {self.patient_id}"
    
class CustomUser(models.Model):
    full_name = models.CharField(max_length=40) 
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class ProjectSubmission(models.Model):
    tu_reg_no = models.CharField(max_length=50)
    email = models.EmailField() 
    project_file = models.FileField(upload_to='projects/')

    def __str__(self):
        return f"{self.tu_reg_no} - {self.email}"
    
class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username