from django.urls import path
from . import filters
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),
    path('movies/filter_genre/', filters.FilterMoviesView.as_view(), name='filter_genre'),
    path('actors/filter_gender/', filters.FilterActorView.as_view(), name='filter_gender'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('movies/', views.MoviesView.as_view(), name='movies-list'),
    path('actors/', views.ActorsView.as_view(), name='actors-list'),
    path('movies/<slug:slug>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('actors/<slug:slug>/', views.ActorDetailView.as_view(), name='actor-detail')
]