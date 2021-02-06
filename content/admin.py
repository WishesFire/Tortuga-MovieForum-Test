from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Movie, Actor, Genre, FootageMovie, FootageActor


class MovieInstanceInline(admin.TabularInline):
    model = Movie
    extra = 1
    readonly_fields = ('show_main_image', )

    def show_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url}> width="100" height="110"')

    show_main_image.short_description = "Main photo for film"


class FootageMovieInline(admin.TabularInline):
    model = FootageMovie
    extra = 1
    readonly_fields = ('show_footage', )

    def show_footage(self, obj):
        return mark_safe(f'<img src={obj.image.url}> width="60" height="70"')

    show_footage.short_description = "Footage for film"


class FootageActorInline(admin.TabularInline):
    model = FootageActor
    extra = 1
    readonly_fields = ('show_pictures', )

    def show_pictures(self, obj):
        return mark_safe(f'<img src={obj.image.url}> width="60" height="70"')

    show_pictures.short_description = "Photos for actor"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'show_main_image')
    list_filter = ('genres', 'public_date')
    search_fields = ('name', 'genres__name')
    readonly_fields = ('show_main_image', )
    inlines = [FootageMovieInline, ]
    save_on_top = True
    save_as = True
    fieldsets = (
        ('Title', {
            "fields": (("name", "slug"), )
        }),
        ('Information', {
            "fields": ('description', 'public_date')
        }),
        ('Pictures', {
            "fields": (('main_image', 'footage'), )
        }),
        ('Actors', {
            "fields": (("actors", "genres"), )
        }),
        ('Money', {
            "fields": (('budget', 'fees'),)
        }),
    )

    def show_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url}> width="50" height="60"')

    show_main_image.short_description = "Main photo for film"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'show_main_image')
    list_display_links = ('name',)
    list_filter = ('name', 'age')
    search_fields = ('name', 'genres')
    readonly_fields = ('show_main_image', )
    inlines = [FootageActorInline, ]
    save_on_top = True

    def show_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_picture.url}> width="100" height="100"')

    show_main_image.short_description = "Main photo"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    #inlines = [MovieInstanceInline]
    #TODO відображати фільми до цього жанру


admin.site.site_title = "Tortuga"
admin.site.site_header = "Tortuga"
