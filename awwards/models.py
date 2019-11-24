from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField()
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = HTMLField(null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    

    def __str__(self):
        return self.username

    def update_profile(self):

        ''' Method to update a profile in the database'''

        self.update()

    def delete_profile(self):

        ''' Method to delete a profile from the database'''

        self.delete()


class Project(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2500)
    link = models.CharField(max_length=2000)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


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

