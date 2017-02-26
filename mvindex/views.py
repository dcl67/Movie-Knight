from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import Movie, NewUser
#   ELIMINATE BIAS IN THE QUESTIONS - MENTION THIS IN PRESENTATION

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie':movie,
    }
    return render(request, 'mvindex/index.html', context)

def Create_View(request):
    return render(request, 'mvindex/create.html', context=None)

def Create_New_User(request):
    new_user = User.objects.create_user(NewUser.username, email=None, password=NewUser.password)
    return HttpResponseRedirect('/')

def Login(request):
    return render(request, 'mvindex/movie.html', context=None)