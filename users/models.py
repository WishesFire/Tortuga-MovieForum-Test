from django.db import models
from content.models import Genre
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='favorite_genre')