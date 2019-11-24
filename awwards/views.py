from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Project,Profile,Rate
# Create your views here.


def index(request):
    projects= Project.objects.all().order_by("-id")
    profiles =Profile.objects.all()
    current_user =request.user
    rate =Project.objects.all()
    return render(request, 'index.html',{"projects":projects,"profiles":profiles,"current_user":current_user,"rate":rate})

def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)
    projects = Project.objects.filter(upload_by = user)
    projects = Project.objects.all()
    return render(request, "profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object})


def project(request,id):
    show_user = request.user
    project = Project.objects.get(id=id)
  
    return render(request,'project.html',{"project":project,"show_user":show_user})