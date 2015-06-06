
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from instaWeb.models import Activity, User, Photo
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return render(request, 'instaWeb/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
            if request.user.is_authenticated():
                return HttpResponseRedirect('/instaWeb/home/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'instaWeb/index.html',{'invalid': 'invalid'})

    else:
        return render(request, 'instaWeb/index.html')

def home(request):
    return render(request, 'instaWeb/home.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')