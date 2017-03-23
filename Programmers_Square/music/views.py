from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums=Album.objects.all()
    context = {'all_albums': all_albums}

    return render(request, 'music/index.html', context)         #HttpRequest is actually being sent in backg. owing to built in

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id)+"</h2>")