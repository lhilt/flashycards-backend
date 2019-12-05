import json

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import Deck

# Create your views here.
## controllers for DECKS

@require_http_methods(['GET'])
@login_required
def list_decks(request, user_pk):
    decks = Deck.objects.filter(user=user_pk)
    response = {'decks': list(decks.values())}
    return JsonResponse(response, status=200)


@require_http_methods(['POST'])
def create_deck(request, user_pk):
    new_deck_info = json.loads(request.body)
    deck = Deck.objects.create(new_deck_info)
    return JsonResponse({}, status=201)


@require_http_methods(['PUT'])
def edit_deck(request, user_pk, deck_pk):
    deck = Deck.objects.get(pk=deck_pk)
    new_info = json.loads(request.body)

    Deck.objects.filter(pk=deck_pk).update(**new_info)
    return JsonResponse(new_info, status=200)


@require_http_methods(['DELETE'])
def delete_deck(request, user_pk, deck_pk):
    deck = Deck.objects.get(pk=deck_pk)
    deck.delete()
    return JsonResponse({}, status=200)
