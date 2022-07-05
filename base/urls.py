from django.urls import path, include #The url path
# from . import views #import views from the current folder to map the url
from .views import *

from django.conf import settings
from django.conf.urls.static import static
#Create the urls
urlpatterns = [
    path('', home, name='home'),    
    path('event/<str:pk>', event, name='event'),
    path('accounts/login/',loginUser, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('register/',registerUser, name='register'),
    path('add-event/',addEvent, name='add-event'),
    path('revoke-event/',revokeEvent),
    path('create-event/',createEvent, name='create-event'),
    path('profile/<str:pk>',profile, name='profile'),
    path('account/<str:pk>',viewAccount, name='my-account'),
    path('send-message/',sendMessage,name='send-message'),
    path('delete-message/',deleteMessage,name='delete-message'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
