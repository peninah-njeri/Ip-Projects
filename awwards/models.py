from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to="photod/",null=True)
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = HTMLField(null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    

    def __str__(self):
        return self.username


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(username=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()



    def update_profile(self):

        ''' Method to update a profile in the database'''

        self.update()

    def delete_profile(self):

        ''' Method to delete a profile from the database'''

        self.delete()


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2500)
    link = models.CharField(max_length=2000)
    upload_date = models.DateField(auto_now_add=True,null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    view_rate=models.IntegerField(null=True)


    def __str__(self):
        return self.title


    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
    @classmethod
    def all_projects(cls):
        all_projects = cls.objects.all()
        return all_projects

    def get_one_project(self, post_id):
        return self.objects.get(pk=post_id)    


class Rate(models.Model):
    design = models.IntegerField()
    usability=models.IntegerField()
    content=models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Project=models.ForeignKey(Project)
    total= models.IntegerField()
    avg=models.IntegerField(null=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.comment

class         

