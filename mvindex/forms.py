from django import forms
from django.forms import ModelForm, RadioSelect

from .models import *

class QuestionaireForm(forms.ModelForm):

    class Meta:
        model = QuizResults