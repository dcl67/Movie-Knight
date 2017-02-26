from django.contrib import admin

from .models import Movie, movie_titles, Questionaire, NewUser

# Register your models here.
admin.site.register(Movie)
admin.site.register(movie_titles)
admin.site.register(Questionaire)
admin.site.register(NewUser)