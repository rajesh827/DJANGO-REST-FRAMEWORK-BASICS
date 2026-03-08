from rest_framework import serializers
from .models import Patient
from .models import CustomUser
from .models import ProjectSubmission
import re, os

class PatientSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])

    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'name', 'mobile', 'gender', 'address', 'dob', 'doctor_name']

    def validate_mobile(self, value):
        if not re.match(r'^(98|97|96)\d{8}$', value):
            raise serializers.ValidationError(
                "Mobile number must be exactly 10 digits and start with 98, 97, or 96."
            )
        return value
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True} 
        }

    def validate_username(self, value):
        if not re.match(r'^[a-zA-Z]+[0-9]+$', value):
            raise serializers.ValidationError(
                "Username must start with letters and end with numbers (e.g., 'alex123')."
            )
        return value

    def validate_password(self, value):
        if len(value) <= 8:
            raise serializers.ValidationError(
                "Password must be more than 8 characters long."
            )
        return value
    
class ProjectSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSubmission
        fields = ['id', 'tu_reg_no', 'email', 'project_file']

    def validate_project_file(self, value):
        max_size = 5 * 1024 * 1024 
        
        if value.size > max_size:
            raise serializers.ValidationError("File size must be less than 5MB.")

        valid_extensions = ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.jpeg', '.jpg']
        
        ext = os.path.splitext(value.name)[1].lower()
        
        if ext not in valid_extensions:
            raise serializers.ValidationError(
                f"Unsupported file format. Allowed formats are: {', '.join(valid_extensions)}"
            )

        return value