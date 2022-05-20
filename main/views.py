from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import os

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def projects(request):
    return render(request,'main/projects.html')

def resume(request):
    return render(request,'main/resume.html')

def contact(request):
    return render(request,'main/contact.html')

def project_overview(request):
    return render(request,'main/contact.html')

def show_pdf(request):
    filepath = os.path.join('static','images', 'RothschildResume.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')