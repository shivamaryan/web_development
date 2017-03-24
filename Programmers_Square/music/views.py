from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums=Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})         #HttpRequest is actually being sent in backg. owing to built in

def detail(request, album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album} ) #using context would raise local varialbe issues
