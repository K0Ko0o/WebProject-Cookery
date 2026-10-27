from django import forms

from djangoproject.mixins import DisabledForm
from ingredients.models import Supermarket, Ingredient


class IngredientSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder' : "Search by ingredient name"
        })
    )
    category = forms.ModelChoiceField(
        queryset=Supermarket.objects.all(),
        required=False,
        empty_label='All supermarkets'
    )

class IngredientBaseForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter ingredient name here"}),
            "calories_per_100_grams": forms.TextInput(attrs={"placeholder": "How many categories does the ingredient have per 100 grams?"}),
            "supermarket": forms.TextInput(attrs={"placeholder": "Where did you buy this ingredient"}),
        }

class IngredientCreateForm(IngredientBaseForm):
    pass

class IngredientEditForm(IngredientBaseForm):
    pass

class IngredientDeleteForm(DisabledForm, IngredientBaseForm):
    pass

