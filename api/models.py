from django.db import models
from tastypie.resources import ModelResource, fields, ALL
from rental.models import Movie, Genre
from tastypie.authorization import Authorization

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = "genres"
        allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()

# Create your models here.

class MovieResource(ModelResource):
    genre = fields.ToOneField(GenreResource, 'genre', full=True)
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering: ['release_year', 'title', 'price', 'director', 'star']
        allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()
        filtering = {
            'price': ALL,
            'title': ALL,
            'release_year': ALL,
        }
        
