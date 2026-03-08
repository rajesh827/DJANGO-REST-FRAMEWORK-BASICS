from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import PatientSerializer
from .serializers import CustomUserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ProjectSubmissionSerializer
from .models import Student

class PatientCreateAPIView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Patient data created and stored successfully.",
                    "data": serializer.data
                }, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User stored successfully!", 
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSubmissionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Project submitted successfully.",
                    "data": serializer.data
                }, 
                status=status.HTTP_201_CREATED
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            student = Student.objects.get(username=username)
            
            if student.verify_password(password):
                
                refresh = RefreshToken()
                refresh['user_id'] = student.id     
                refresh['username'] = student.username 
                
                # Return the JWT token
                return Response({
                    'message': 'Login successful',
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)
            
            else:
                return Response(
                    {'error': 'Invalid username/password'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
        except Student.DoesNotExist:
            return Response(
                {'error': 'Invalid username/password'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )