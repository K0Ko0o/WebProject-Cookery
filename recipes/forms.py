from django import forms
from django.core.exceptions import ValidationError

from djangoproject.mixins import DisabledForm
from recipes.models import Recipe


class RecipeBasicForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter recipe name here"}),
            "description": forms.TextInput(attrs={"placeholder": "Enter recipe description here. Not required"}),
            "instructions": forms.TextInput(attrs={"placeholder": "Enter recipe instructions here"}),
            "time": forms.TextInput(attrs={"placeholder": "Enter recipe time in minutes here"}),
        }

    def clean_instructions(self):
        instructions = self.cleaned_data['instructions']

        if len(instructions) < 10:
            raise ValidationError("The instructions must be more detailed!")

        return instructions



class RecipeCreateForm(RecipeBasicForm):
    pass

class RecipeEditForm(RecipeBasicForm):
    pass

class RecipeDeleteForm(DisabledForm, RecipeBasicForm):
    pass