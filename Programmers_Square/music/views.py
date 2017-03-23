from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums=Album.objects.all()
    template =loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
   # html=''                                            the following lines moved to the template file
    #for album in all_albums:                           cheers
     #   url='/music/'+str(album.id)+'/'
      #  html +='<a href="'+ url +'">'+album.album_title+'</a> <br>'    cheers uptil here
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id)+"</h2>")