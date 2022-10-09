from django.shortcuts import render
from .models import *
from user.models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request):
    filmler = Movie.objects.all()
    izleyen = Izlenenler.objects.get(user = request.user)
    izlenen = izleyen.izlenen.all()
    
    # Search
    search_movie = ''
    if request.GET.get('search_movie'):
        search_movie = request.GET.get('search_movie')
        filmler = filmler.filter(
            Q(isim__icontains = search_movie) |
            Q(kategori__name__icontains = search_movie)
            )
    context = {
        'izlenenler':izlenen,
        'filmler':filmler,
        'search_movie':search_movie
    }

    return render(request, 'browse-index.html', context)

def profiles(request):
    kullanicilar = Profiles.objects.filter(owner = request.user)
    context = {
        'kullanici':kullanicilar
    }
    return render(request, 'browse.html', context)