from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('projects/overview',views.projects_overview,name='projects_overview'),
    path('projects/trading',views.projects_trading,name='projects_trading'),
    path('projects/landtrack',views.projects_landtrack,name='projects_landtrack'),
    path('blog/',views.blog,name='blog'),
    path('resume/',views.resume,name='resume'),
    path('contact/',views.contact,name='contact'),
    ]