
# Create your views here.
from django.shortcuts import render
from. models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONOpenAPIRenderer
from django.http import HttpResponse
# Create your views here.

# model object  - singel Data

def student_detail(request):
    stu = Student.objects.get(id = 1)
    print(stu)
    serializer =  StudentSerializer(stu)
    json_data = JSONOpenAPIRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type = 'apllication/json')


