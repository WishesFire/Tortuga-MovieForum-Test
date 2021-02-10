from .models import RatingStar
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def push_rating(request, imdb_id):
    user = request.user
    movie_id = request.POST.get('el_id')
    val = request.POST.get('val')
    RatingStar.objects.update_or_create(user=user, movie_id=movie_id, star_rating=int(val))