import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

from .models import Card, Deck
from .forms import CardCreate

# Create your views here.
## controllers for CARDS

def testing(request):
    return render(request, 'testing.html')


@require_http_methods(['GET'])
def list_cards(request, user_pk, deck_pk):
    cards = Card.objects.filter(deck=deck_pk)
    response = {'cards': list(cards.values())}
    return JsonResponse(response, status=200)


@require_http_methods(['POST'])
def create_card(request, user_pk, deck_pk):
    form = CardCreate(json.loads(request.body))
    if form.is_valid():
        new_card_info = form.cleaned_data
        card = Card.objects.create(
            **new_card_info,
            deck=Deck.objects.get(pk=deck_pk)
        )
        res = {'card': new_card_info}
        return JsonResponse(res, status=201)


@require_http_methods(['PUT'])
def edit_card(request, user_pk, deck_pk, card_pk):
    card = Card.objects.get(pk=card_pk)
    new_info = json.loads(request.body)

    Card.objects.filter(pk=card_pk).update(**new_info)
    return JsonResponse(new_info, status=200)


@require_http_methods(['DELETE'])
def delete_card(request, user_pk, deck_pk, card_pk):
    card = Card.objects.get(pk=card_pk)
    card.delete()
    return JsonResponse({}, status=200)
