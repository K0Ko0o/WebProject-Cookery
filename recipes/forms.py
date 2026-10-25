from django import forms

from recipes.models import Recipe


class RecipeBasicForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeCreateForm(RecipeBasicForm):
    pass

class RecipeEditForm(RecipeBasicForm):
    pass

class RecipeDeleteForm(RecipeBasicForm):
    pass