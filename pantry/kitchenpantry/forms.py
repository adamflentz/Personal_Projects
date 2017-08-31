from django import forms

class IngredientForm(forms.Form):
    ingredient1 = forms.CharField(label='Ingredient 1', max_length=1000)
    ingredient2 = forms.CharField(label='Ingredient 2', max_length=1000, required=False)
    ingredient3 = forms.CharField(label='Ingredient 3', max_length=1000, required=False)