from django import forms
from django.forms import ModelForm, RadioSelect

from .models import *

class QuestionaireForm1(forms.ModelForm):

    class Meta:
        model = Questionaire
        fields = ['question1', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10']