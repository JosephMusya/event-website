from django.contrib import admin

# Register your models here.
from .models import Event,Message,Profile
admin.site.register(Event)
admin.site.register(Message)
admin.site.register(Profile)