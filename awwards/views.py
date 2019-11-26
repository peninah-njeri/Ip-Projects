from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import datetime as dt
from .forms import NewProjectForm,ProfileForm,RateForm
from .models import Project,Profile,Rate
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    projects= Project.objects.all().order_by("-id")
    profiles =Profile.objects.all()
    current_user =request.user
    rate =Project.objects.all()
    return render(request, 'index.html',{"projects":projects,"profiles":profiles,"current_user":current_user,"rate":rate})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)
    projects = Project.objects.filter(upload_by = user)
    projects = Project.objects.all()
    return render(request, "profile.html", {"current_user":current_user,"projects":projects,"user":user,"user_object":user_object})

@login_required(login_url='/accounts/login/')
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




@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = Profile.objects.get(username__id=request.user.id)
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.upload_by = current_user
            project.save()
        return redirect('welcome')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def project(request,id):
    show_user = request.user
    project = Project.objects.get(id=id)
  
    return render(request,'project.html',{"project":project,"show_user":show_user})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_projects = Project.search_project(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"projects":searched_projects})   

@login_required(login_url='/accounts/login/')
def rate_project(request,id):
    current_user=request.user
    project=Project.objects.get(id=id)
    if request.method == 'POST':
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = current_user
            rate.project=project
            rate.total=int(form.cleaned_data['design'])+int(form.cleaned_data['content'])+int(form.cleaned_data['usability'])
            rate.avg= int(rate.total)/3
            RateForm.save()
        return redirect('index')
    else:
        form = RateForm()
    return render(request, 'rate.html',{"form": form, 'proj':project})




class ProfileList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


