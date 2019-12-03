import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Card

# Create your views here.
## controllers for CARDS

@require_http_methods(['GET'])
def list_cards(request, user_pk, deck_pk):
    cards = Card.objects.filter(deck=deck_pk)
    response = {'cards': list(cards.values())}
    return JsonResponse(response, status=200)


@require_http_methods(['POST'])
def create_card(request, user_pk, deck_pk):
    new_card_info = json.loads(request.body)
    card = Card.objects.create(new_card_info)
    return JsonResponse({}, status=201)


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
