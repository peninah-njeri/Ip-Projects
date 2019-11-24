from django.conf.urls import url
from . import views


urlpatterns=[
     url('^$',views.index,name = 'index'), 
     url(r'^project/(\d+)', views.project, name = 'project'), 

]    