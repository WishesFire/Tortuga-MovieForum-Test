from django.shortcuts import render, get_object_or_404
from .services import pagination_page, search_movie
from .models import Movie, Actor, Genre, Gender
from django.views.generic.base import View


class MainPage(View):
    def get(self, request):
        return render(request, 'main_page.html')


class GenreGet:
    def get_genres(self):
        return Genre.objects.all()


class GenderGet:
    def get_gender(self):
        return Gender.objects.all()


class MoviesView(GenreGet, View):
    def get(self, request):
        movies = Movie.objects.all()
        page, movies = pagination_page(request, movies)

        return render(request, 'movies/movie-list.html', {'page_obj': page, 'movie_list': movies})


class MovieDetailView(View):
    def get(self, request, slug):
        movie = get_object_or_404(Movie, url=slug)
        return render(request, 'movies/movie-detail.html', {'movie': movie})


class ActorsView(GenderGet, View):
    def get(self, request):
        actors = Actor.objects.all()
        return render(request, 'actors/actor-detail.html', {'actor_list': actors})


class ActorDetailView(View):
    def get(self, request, slug):
        actor = get_object_or_404(Actor, url=slug)
        return render(request, 'actors/actor-detail.html', {'actor': actor})


class SearchView(View):
    def get(self, request):
        form, query, results = search_movie(request)
        return render(request, 'movies/movie-search-list.html', {'form': form, 'query': query, 'results': results})