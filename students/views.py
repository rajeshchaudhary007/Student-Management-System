from django.shortcuts import render
from .models import Students
# Create your views here.
def home(request):
    student = Students.objects.all()
    return render(request, 'students/home.html',{'studnet':student})