# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from forms import IngredientForm
from models import Recipe
import sqlite3, random

# Create your views here.
class home(TemplateView):
    def get(self, request):
        return render(request, 'home.html', locals())
class profile(TemplateView):
    def get(selfself, request):
        return render(request, 'profile.html', locals())
class recipequery(TemplateView):
    def get(self, request):
        form = IngredientForm()
        return render(request, 'simplerecipequery.html', locals())


    def post(self, request):
        form = IngredientForm(request.POST)
        return render(request,  'home.html', {'form': form})

class recipecards(TemplateView):
    def get(self, request):
        return render(request, 'recipecards.html', locals())
    def post(self, request):
        requestform = IngredientForm(request.POST)
        if requestform.is_valid():
            ingredient1 = requestform.cleaned_data['ingredient1']
            ingredient2 = requestform.cleaned_data['ingredient2']
            ingredient3 = requestform.cleaned_data['ingredient3']
        if len(requestform.cleaned_data):
            recipes = Recipe.objects.all()
            for element in recipes:
                print(element)
            print(recipes)
            #recipecard = random.choice(recipes)
        return render(request, 'recipecards.html', locals())