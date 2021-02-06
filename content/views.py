from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor
from django.views.generic.base import View


class MainPage(View):
    def get(self, request):
        return render(request, 'main_page.html')


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie-list.html', {'movie_list': movies})


class MovieDetailView(View):
    def get(self, request, slug):
        movie = get_object_or_404(Movie, url=slug)
        return render(request, 'movies/movie-detail.html', {'movie': movie})


class ActorsView(View):
    def get(self, request):
        #TODO Сортировка по оценке
        pass


class ActorDetailView(View):
    def get(self, request, slug):
        movie = get_object_or_404(Actor, url=slug)
        return render(request, 'actors/actor-detail.html', {'actor': movie})