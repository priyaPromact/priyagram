
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from instaWeb.models import Activity, User, Photo
from django.shortcuts import render


def index(request):
    return render(request, 'instaWeb/index.html')