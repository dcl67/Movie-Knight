from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

"""
class Rating(models.Model):
    rating = models.CharField(max_length=5, blank=True, null=True)
"""

class Movie(models.Model):
    imdbid = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    rating = models.CharField(max_length=5, blank=True, null=True)
    runtime = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    actors = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

"""
class Answer(models.Model):
    question = models.ForeignKey("Question")


class ChoiceAnswer(Answer):
    answer = models.IntegerField(max_length=1, choices=CHOICES)
    def __unicode__(self):
        return u'%s: %s'%(self.question, self.answer)


class BooleanAnswer(Answer):
    answer= models.BooleanField(choices=((True,'yes'),(False,'no')))
    def __unicode__(self):
        return u'%s: %s'%(self.question, self.answer)


class Question(models.Model):
    question = models.CharField(max_length=255)
    answer_type = models.ForeignKey(ContentType)

    def __unicode__(self):
        return u'%s'%self.question
"""

class QuizResults(models.Model):
    action = models.IntegerField(blank=False, null=False)
    horror = models.IntegerField(blank=False, null=False)
    fantasy = models.IntegerField(blank=True, null=True)
    animated = models.IntegerField(blank=True, null=True)
    thriller = models.IntegerField(blank=True, null=True)
    comedy = models.IntegerField(blank=True, null=True)
    adventure = models.IntegerField(blank=True, null=True)
    romance = models.IntegerField(blank=True, null=True)
    war = models.IntegerField(blank=True, null=True)
    history = models.IntegerField(blank=True, null=True)

class NewUser(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)