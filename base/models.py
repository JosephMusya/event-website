from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class Event(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    topic = models.CharField(max_length=50,blank=False,null=False)
    location = models.CharField(max_length=100,blank=False,null=False)
    about = models.TextField(max_length=500,blank=True,null=True)
    date_start = models.CharField(max_length=50,null=True)
    date_end = models.CharField(max_length=50,null=True)
    capacity = models.IntegerField(null=True)    
    pic = models.ImageField(upload_to='',default='media/default.jpg')    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.topic
    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return str(self.user) + ' message'

class Attendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    def __str__(self):
        return str(self.user)+' '+str(self.event)

# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     events = models.ForeignKey(Event,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user.username
        