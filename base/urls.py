from django.urls import path #The url path
from . import views #import views from the current folder to map the url

from django.conf import settings
from django.conf.urls.static import static
#Create the urls
urlpatterns = [
    path('', views.home, name='home'),
    path('event/<str:pk>', views.event, name='event'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerUser, name='register'),
    path('delete-msg/',views.deleteMsg, name='delete-msg'),
    path('create-event/',views.createEvent, name='create-event'),
    path('profile/<str:pk>',views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
