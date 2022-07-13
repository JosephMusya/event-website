from django.http import JsonResponse
from django.shortcuts import redirect, render

#http response is used to display info in the browser
# from django.http import HttpResponse

from .models import Event, Message, Attendees

from django.contrib.auth import get_user_model,authenticate,login,logout

from .forms import CustomUserForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.db.models import Q
from datetime import datetime

def home(request):        
    users = User.objects.all()
    available_events = []
    if request.user.is_authenticated:
        events_attending = Attendees.objects.filter(user = request.user)
        event_ids = []    
        for evts in events_attending:
            ids = evts.event.id
            event_ids.append(ids)
    else:
        event_ids = None
        
    if request.method == "GET":
        q = request.GET.get('search') if request.GET.get('search') != None else ''
        available_events = Event.objects.filter(
            Q(topic=q)
        )
        if available_events:
            context = {'events':available_events,'users':users,'event_ids':event_ids}
            return render(request,'base/homepage.html',context)
        else:
            available_events = Event.objects.all()              
            context = {'events':available_events,'users':users,'event_ids':event_ids}        
            return render(request,'base/homepage.html',context)

def event(request,pk):
    content = Event.objects.get(id=pk)
    attendees = Attendees.objects.filter(event=content)
    event_ids = []
    messages = Message.objects.filter(event_id=pk)
    if request.user.is_authenticated:
        events_attending = Attendees.objects.filter(user = request.user)        
        for events in events_attending:
            ids = events.event.id
            event_ids.append(ids)
    
    
    context = {'content':content,'messages':messages,'event_ids':event_ids,'attendees':attendees}
    return render(request,'base/event.html', context)

def registerUser(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, user)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'base/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user:
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
        event.pic = request.FILES['image']
        
        event.save()
        
        return redirect('home')
        
    return render(request,'base/create_event.html')

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
    if request.user == user:
        user_event.delete()
        event = Event.objects.get(id=event_id)
        event.capacity = event.capacity+1    
        event.save()
    return redirect('/')

@login_required(login_url='login')
def sendMessage(request):
    user_id = int(request.POST.get('user_id'))
    event_id = int(request.POST.get('event_id'))
    msg = str(request.POST.get('message'))
    user = User.objects.get(pk=user_id)
    event = Event.objects.get(pk=event_id)
    if request.user == user:
        message = Message()
        message.user = user
        message.event = event
        message.body = msg
        message.save()
    return redirect('/')

@login_required(login_url='login')
def deleteMessage(request):
    msg_id = int(request.POST.get('msg_id'))
    user_id = int(request.POST.get('user_id'))
    message = Message.objects.get(pk=msg_id)
    user = User.objects.get(pk=user_id)
    if request.user == user:
        message.delete()      
    return redirect('/')

def deleteEvent(request):
    event_id = int(request.POST.get('event_id'))
    host = int(request.POST.get('host'))
    user = User.objects.get(id=host)
    
    if request.user == user:
        event = Event.objects.filter(host=user).filter(id=event_id)
        event.delete()
def searchEvent(request):
    events = Event.objects.filter().values_list('topic',flat=True)
    event_list = list(events)
    return JsonResponse (event_list, safe=False)
