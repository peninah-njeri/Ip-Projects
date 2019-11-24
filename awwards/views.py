from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
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


def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
            return redirect('index')
                 
    else:
        form=ProfileForm(instance=request.user.profile)
     
    return render(request,'edit_profile.html',locals())


def project(request,id):
    show_user = request.user
    project = Project.objects.get(id=id)
  
    return render(request,'project.html',{"project":project,"show_user":show_user})


def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_projects = Project.search_project(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"projects":searched_projects})    