from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib import admin
from .models import Event,Message,Attendees
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

# Register your models here.
admin.site.register(Event)
admin.site.register(Message)
admin.site.register(Attendees)