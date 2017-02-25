from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

class Rating(models.Model):
    rating = models.CharField(max_length=5, blank=True, null=True)

class Movie(models.Model):
    imdbid = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    rating = models.ForeignKey('Rating', blank=True, null=True)
    #Runtime = models.

    def __str__(self):
        return self.movie_name