from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from content.models import Movie

User = get_user_model()
MARKS_RATING = {
    1: '🤮',
    2: '🤢',
    3: '😴',
    4: '🙄',
    5: '🤔',
    6: '🙄',
    7: '😏',
    8: '😄',
    9: '🤑',
    10: '👑'
}


class RatingStar(models.Model):
    """
        Rating: Evaluation of the film in general and users
                Unit of designation
    """
    star_rating = models.PositiveSmallIntegerField(default=0, blank=True,
                                                   validators=[MaxValueValidator(10), MinValueValidator(0)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
