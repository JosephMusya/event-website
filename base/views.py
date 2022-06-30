from django.shortcuts import redirect, render

#http response is used to display info in the browser
from django.http import HttpResponse

from .models import Event, Message, Attendees

from django.contrib.auth import get_user_model,authenticate,login,logout

from .forms import CustomUserForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
# Create your views here.

#The request parameter is the request by the user, to be handled
# def hello(request):
#     message = 'Hello World This is my Hello World Displayed on a browser'
#     return HttpResponse(message)

# def home(request):
#     users = [
#         {'id':1,'name':'Josee','course':'Mechatronics'},
#         {'id':1,'name':'Amalia','course':'Mechatronics'},
#         {'id':1,'name':'Verol','course':'Electrical & electronics'},
#         {'id':1,'name':'Salome','course':'Mechatronics'},

#         ]
#     context = {'users':users}
#     return render(request,'base/home.html',context)

def home(request):
    events = Event.objects.all()
    users = User.objects.all()
    if request.user.is_authenticated:
        events_attending = Attendees.objects.filter(user = request.user)
        event_ids = []    
        for evts in events_attending:
            ids = evts.event.id
            event_ids.append(ids)
    else:
        event_ids = None
    context = {'events':events,'users':users,'event_ids':event_ids}

    return render(request,'base/homepage.html',context)

def event(request,pk):
    content = Event.objects.get(id=pk)
    attendees = Attendees.objects.filter(event=content)
    events_attending = Attendees.objects.filter(user = request.user)
    event_ids = []
    for events in events_attending:
        ids = events.event.id
        event_ids.append(ids)
    messages = Message.objects.filter(event_id=pk)
    if request.method == 'POST':
        message = Message()
        user = request.user
        message.body = request.POST.get('message')
        message.user = user
        message.event = Event.objects.get(id=pk)
        message.save()
    context = {'content':content,'messages':messages,'event_ids':event_ids,'attendees':attendees}
    return render(request,'base/event.html', context)

def registerUser(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form':form}
    return render(request, 'base/register.html', context)
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'account/login.html')
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def addEvent(request):
    attendee = Attendees()
    event_id = int(request.POST.get('event_id'))
    user_id = int(request.POST.get('user-id'))

    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)
    attendee.user = user
    attendee.event = event
    event.capacity = (event.capacity-1)
    if event.capacity <= 0:
        event.capacity = 0
    attendee.save()
    event.save()
    return redirect('/')

@login_required(login_url='login')
def createEvent(request):
    event = Event()
    if request.method == 'POST':        
        event.host = request.user
        event.topic = request.POST.get('Topic')
        event.location = request.POST.get('Location')
        event.about = request.POST.get('About')
        event.date_start = request.POST.get('Date1')
        event.date_end = request.POST.get('Date2')
        event.capacity = request.POST.get('capacity')

        event.pic = request.POST.get('Image')
        
        event.save()
        
    return render(request,'base/create_event.html')

@login_required(login_url='login')
def profile(request,pk):
    user = User.objects.get(pk=pk)
    # profile = Profile.objects.get(pk=pk)
    events = Event.objects.filter(host=pk)
    context = {'user':user, 'events':events}
    return render(request,'base/profile.html',context)

@login_required(login_url='login')
def viewAccount(request,pk):
    user = User.objects.get(pk=pk)
    events_hosted = Event.objects.filter(host=user)
    context = {'user':user,'events_hosted':events_hosted}
    return render(request,'base/view_profile.html',context)

@login_required(login_url='login')
def revokeEvent(request):
    event_id = int(request.POST.get('event_id'))
    user_id = int(request.POST.get('user-id'))
    user = User.objects.get(id=user_id)
    user_event = Attendees.objects.filter(user=user).filter(event=event_id)
    user_event.delete()
    event = Event.objects.get(id=event_id)
    event.capacity = event.capacity+1    
    event.save()
    return redirect('/')
    