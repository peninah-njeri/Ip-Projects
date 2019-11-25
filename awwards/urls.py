from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
     url('^$',views.index,name = 'index'), 
     url(r'^project/(\d+)', views.project, name = 'project'), 
     url(r'^profile/(\d+)', views.profile, name = 'profile'),
     url(r'^search/', views.search_results, name='search_results'),
     url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
     url(r'^new/project/', views.new_project, name = 'new-project'),
     url(r'^rate/(\d+)',views.rate_project,name ='rate'), 
]  

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)