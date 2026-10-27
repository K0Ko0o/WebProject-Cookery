from django import forms

from ingredients.models import Supermarket


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
