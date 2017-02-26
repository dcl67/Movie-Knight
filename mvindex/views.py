from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from surprise import KNNBasic
from surprise import Dataset
from surprise import evaluate
from surprise import Reader
from surprise import SVD

import pandas as pd

import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

from .models import Movie, NewUser, movie_titles, Questionaire
from .forms import QuestionaireForm1
#   ELIMINATE BIAS IN THE QUESTIONS - MENTION THIS IN PRESENTATION

# Create your views here.
@csrf_exempt
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

@csrf_exempt
def Quiz(request):
    titles = movie_titles.objects.all()
    context = {
        'titles':titles,
    }
    return render(request, 'mvindex/questions.html', context)


def Predictor(request):
    #answers = get_object_or_404(Questionaire)
    #form = QuestionaireForm1
    question1 = request.POST['#1']
    question2 = request.POST['#2']
    question3 = request.POST['#3']
    question4 = request.POST['#4']
    question5 = request.POST['#5']
    question6 = request.POST['#6']
    question7 = request.POST['#7']
    question8 = request.POST['#8']
    question9 = request.POST['#9']
    question10 = request.POST['#10']

    #The function that makes the reccomendation
    def make_reccomendation(self, user_pref):

        #the filepath to the dataset
        file_path = 'ml-100k/u.data'
        #setting the Reader obj
        reader = Reader(line_format='user item rating timestamp', sep='\t')
        data = Dataset.load_from_file(file_path, reader=reader)

        # Retrieve the trainset.
        trainset = data.build_full_trainset()

        # pick an algorithm

        #we're using a K nearest-neighbors algorithm
        #algo = KNNBasic()

        #we're using a singular value decomposition algorithm
        algo = SVD()

        #train the algo on our data
        algo.train(trainset)

        #read the ratings file
        r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
        ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
         encoding='latin-1')

        #the as of now empty dict that will contain the raters and their likenesses
        rater_likeness = {}

        #loop through the ratings table, if our user and the rater agree, give '1 pt' to
        #the rater's likeness to our user. In the end the rater with the most
        #'likeness' wins out and their reccomendation will be queried
        for index, row in ratings.iterrows():
            if row['movie_id'] in user_pref and user_pref[row['movie_id']] == row['rating']:
                if not row['user_id'] in rater_likeness:
                    rater_likeness[row['user_id']] = 1
                else:
                    rater_likeness[row['user_id']] += 1

        #determine which rater in the dict has the highest likeness
        thing = 0
        for key, value  in rater_likeness.iteritems():
            if value >= thing:
                thing = value
                best_rater=key

        user_id = str(best_rater)  #we need this to be a string for the predict func

        #loop through the list of movies until we find one that our rater would
        #give more than a 4.6
        for i in range(1, 1683):
            item_id = str(i)
            if not i in user_pref:
                pred = algo.predict(user_id, item_id, r_ui=3, verbose=False)
                if pred.est >= 4.6:
                    break

        return i

    predictor = Predictor()
    test_pref = {1:question1, 2:question2, 3:question3, 4:question4, 5:question5, 6:question6, 7:question7, 8:question8,
    9:question9, 10:question10}
    reccomendation = predictor.make_reccomendation(test_pref)
    print("your reccomendation ID is " + str(reccomendation))
    context = {

    }
    return render( request, 'mvindex/results.html', context )