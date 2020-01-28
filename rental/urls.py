from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('developer', views.develop, name='develop'),
    path('catalog', views.catalog, name='catalog'),
    path('details/<int:movie_id>', views.details, name='details'),
]