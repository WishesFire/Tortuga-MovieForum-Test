from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .forms import SearchForm
from .models import Movie


def pagination_page(request, index_model):
    paginator = Paginator(index_model, 9)
    page = request.GET.get('page', 1)

    try:
        movie_card = paginator.page(page)
    except PageNotAnInteger:
        movie_card = paginator.page(1)
    except EmptyPage:
        movie_card = paginator.page(paginator.num_pages)

    return page, movie_card


def search_movie(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        search_vector = SearchVector('name')
        search_query = SearchQuery(query)
        results = Movie.objects.annotate(search=search_vector,
                                         rank=SearchRank(search_vector, search_query))\
                                         .filter(search=search_query).order_by('-rank')

        return form, query, results
