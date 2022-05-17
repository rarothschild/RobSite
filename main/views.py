from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home</h1>')

def projects(request):
    return HttpResponse('<h1>Projects</h1>')

def resume(request):
    return HttpResponse('<h1>Resume</h1>')