from django.urls import path
from . import views


urlpatterns = [
    path('add-rating/', views.push_rating, name='add-rating'),
]