from django import forms

from .models import Cheese

class CheeseForm(forms.ModelForm):
    class Meta:
        model = Cheese
