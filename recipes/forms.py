from django import forms

from djangoproject.mixins import DisabledForm
from recipes.models import Recipe


class RecipeBasicForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeCreateForm(RecipeBasicForm):
    pass

class RecipeEditForm(RecipeBasicForm):
    pass

class RecipeDeleteForm(DisabledForm, RecipeBasicForm):
    pass