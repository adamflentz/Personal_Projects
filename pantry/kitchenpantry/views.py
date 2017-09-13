# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from forms import IngredientForm
from models import Recipe
import sqlite3, random, json, itertools

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
            ingredientlist = []
            ingredientlist.append(requestform.cleaned_data['ingredient1'])
            if requestform.cleaned_data['ingredient2'] != '':
                ingredientlist.append(requestform.cleaned_data['ingredient2'])
            if requestform.cleaned_data['ingredient3'] != '':
                ingredientlist.append(requestform.cleaned_data['ingredient3'])
            if len(ingredientlist) == 1:
                recipes = Recipe.objects.all().filter(ingredients__contains=ingredientlist[0])
            elif len(ingredientlist) == 2:
                recipes = Recipe.objects.all().filter(ingredients__contains=ingredientlist[0]).filter(ingredients__contains=ingredientlist[1])
            elif len(ingredientlist) == 3:
                recipes = Recipe.objects.all().filter(ingredients__contains=ingredientlist[0])\
                    .filter(ingredients__contains=ingredientlist[1])\
                    .filter(ingredients__contains=ingredientlist[2])
                if len(recipes) != 0:
                    outputmessage = "Showing Recipes for " + ingredientlist[0] + ", " + ingredientlist[1] + ", " + "and " + ingredientlist[2]
            if len(recipes) == 0:
                outputmessage = "No Available Matches for All Three Ingredients"
                error = True
                print(recipes)
            else:
                error = False
                recipecard = random.choice(recipes)
                recipe_ingredientlist = json.loads(recipecard.ingredients)
                numitems = len(recipe_ingredientlist)
                print(recipecard.name)
                print type(recipe_ingredientlist)
                print(recipe_ingredientlist[1])


        return render(request, 'recipecards.html', locals())