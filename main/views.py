from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import os

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def resume(request):
    return render(request,'main/resume.html')

def contact(request):
    return render(request,'main/contact.html')

def projects_overview(request):
    return render(request,'main/projects_overview.html')

def projects_trading(request):
    return render(request,'main/projects_trading.html')

def projects_landtrack(request):
    return render(request,'main/projects_landtrack.html')

def show_pdf(request):
    filepath = os.path.join('static','images', 'RothschildResume.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')