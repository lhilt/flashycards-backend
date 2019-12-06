from django import forms

from .models import Card, Deck


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = {
            'front',
            'back',
        }


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = {
            'name',
            'description',
        }