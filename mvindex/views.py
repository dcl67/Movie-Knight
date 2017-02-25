from django.shortcuts import render

from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie':movie,
    }
    return render(request, 'mvindex/index.html', context)
