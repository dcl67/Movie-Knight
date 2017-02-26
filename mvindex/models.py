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
    #year = models.CharField(max_length=100, blank=True, null=True)

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
class movie_titles(models.Model):
    movie1 = models.CharField(max_length=100, blank=True, null=True)
    movie2 = models.CharField(max_length=100, blank=True, null=True)
    movie3 = models.CharField(max_length=100, blank=True, null=True)
    movie4 = models.CharField(max_length=100, blank=True, null=True)
    movie5 = models.CharField(max_length=100, blank=True, null=True)
    movie6 = models.CharField(max_length=100, blank=True, null=True)
    movie7 = models.CharField(max_length=100, blank=True, null=True)
    movie8 = models.CharField(max_length=100, blank=True, null=True)
    movie9 = models.CharField(max_length=100, blank=True, null=True)
    movie10 = models.CharField(max_length=100, blank=True, null=True)

class Questionaire(models.Model):
    question1 = models.IntegerField(blank=True, null=True)
    question2 = models.IntegerField(blank=True, null=True)
    question3 = models.IntegerField(blank=True, null=True)
    question4 = models.IntegerField(blank=True, null=True)
    question5 = models.IntegerField(blank=True, null=True)
    question6 = models.IntegerField(blank=True, null=True)
    question7 = models.IntegerField(blank=True, null=True)
    question8 = models.IntegerField(blank=True, null=True)
    question9 = models.IntegerField(blank=True, null=True)
    question10 = models.IntegerField(blank=True, null=True)


class NewUser(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)