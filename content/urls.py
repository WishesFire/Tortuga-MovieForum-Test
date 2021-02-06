from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),
    path('movies/', views.MoviesView.as_view(), name='movies-list'),
    path('actors/', views.ActorsView.as_view(), name='actors-list'),
    path('movies/<slug:slug>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('actors/<slug:slug>/', views.ActorDetailView.as_view(), name='actor-detail')
]