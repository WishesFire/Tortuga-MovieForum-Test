from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from django.urls import reverse


class Gender(models.Model):
    """
        Gender: Gender actor
    """
    name = models.CharField()

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.name


class Actor(models.Model):
    """
        Actors: Information about current actor
    """
    name = models.CharField('Name and Surname', max_length=50)
    slug = models.SlugField(max_length=50, null=False, unique=True)
    gender = models.ManyToManyField(Gender, verbose_name="genders", related_name='actor_gender')
    age = models.PositiveSmallIntegerField('Age', default=0)
    birthday = models.DateField("Birthday", default=now())
    description = models.TextField(max_length=250)
    main_picture = models.ImageField('Main photo of the actor', upload_to='actors/', blank=True, null=True)

    class Meta:
        db_table = 'actor'
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor-detail", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Genre(models.Model):
    """
        Genres: Genres for film
    """
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=60, null=False, unique=True)

    class Meta:
        db_table = 'genre'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
        Films: Set of content
    """
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, null=False, unique=True)
    description = models.TextField(max_length=250)
    genres = models.ManyToManyField(Genre, verbose_name="genres", related_name='movie_genres')
    public_date = models.DateTimeField('Date published', default=now())
    main_image = models.ImageField('Pictures', upload_to='content/', blank=True, null=True)
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name='film_actor')
    budget = models.PositiveIntegerField('Budget', default=0)
    fees = models.PositiveIntegerField('Fees', default=0)

    class Meta:
        db_table = 'movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class FootageMovie(models.Model):
    image = models.ImageField('Footage from film', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')


class FootageActor(models.Model):
    image = models.ImageField('Photos of the actor', upload_to='actor_shots/')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='images')


#
# Comment System
#

class Comment(models.Model):
    pass