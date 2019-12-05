from django import forms

from .models import Card

class CardCreate(forms.ModelForm):
    class Meta:
        model = Card
        fields = {
            'front',
            'back',
        }