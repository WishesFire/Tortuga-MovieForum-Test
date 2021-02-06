from django.views.generic.base import View
from django.views.generic import ListView
from .models import Movie, Actor
from .views import GenreGet, GenderGet


class FilterMoviesView(GenreGet, ListView):
    paginate_by = 9

    def get_queryset(self):
        queryset = Movie.objects.filter(genres__in=self.request.GET.getlist('genre')).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        contex = super().get_context_data(*args, **kwargs)
        url_genre = ''.join([f'genre={g}&' for g in self.request.GET.getlist('genre')])
        contex['genre'] = url_genre
        return contex


class FilterActorView(GenderGet, View):
    def get_queryset(self):
        queryset = Actor.objects.filter(gender__in=self.request.GET.getlist('gender'))
        return queryset
