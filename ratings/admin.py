from django.contrib import admin
from .models import RatingStar


@admin.register(RatingStar)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'star_rating', 'movie')