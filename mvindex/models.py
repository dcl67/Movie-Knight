from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

class Movie(models.Model):

    movie_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.movie