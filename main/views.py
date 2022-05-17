from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def projects(request):
    return render(request,'main/projects.html')

def resume(request):
    return render(request,'main/resume.html')