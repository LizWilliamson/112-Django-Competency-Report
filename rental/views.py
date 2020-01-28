from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Movie, Genre

# Create your views here.

def index(request):
    return render(request, 'views/index.html')

def catalog(request):
    movies = Movie.objects.all()
    #titles = ', '.join([m.title for m in movies])
    #return HttpResponse(titles)
    return render(request, 'views/catalogtest.html', { 'title': 'FROM BACKEND', 'movies': movies })

def test(request):
    return HttpResponse("This is a test page!")

def develop(request):
    return HttpResponse("<h1>Liz<h1>")

def details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'views/details.html', { 'id': movie_id, 'movie': movie})
    except Movie.DoesNotExist:
        raise Http404()

