import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from .models import Card, Deck
from .forms import CardForm

# Create your views here.
## controllers for CARDS


@require_http_methods(['GET'])
@login_required
def list_cards(request, deck_pk):
    deck = Deck.objects.select_related('user').get(pk=deck_pk)
    if deck.user != request.user:
        raise PermissionDenied

    cards = Card.objects.filter(deck=deck)
    response = {'cards': list(cards.values())}
    return JsonResponse(response, status=200)


@require_http_methods(['POST'])
@login_required
def create_card(request, deck_pk):
    deck = Deck.objects.select_related('user').get(pk=deck_pk)
    if deck.user != request.user:
        raise PermissionDenied

    form = CardForm(json.loads(request.body))
    if form.is_valid():
        new_card_info = form.cleaned_data
        card = Card.objects.create(
            **new_card_info,
            deck=deck
        )
        res = {'card': model_to_dict(card)}
        return JsonResponse(res, status=201)


@require_http_methods(['PUT'])
@login_required
def edit_card(request, card_pk):
    card = get_object_or_404(
        Card.objects.select_related('deck__user'),
        pk=card_pk
    )
    if card.deck.user != request.user:
        raise PermissionDenied
    form = CardForm(json.loads(request.body), instance=card)
    if form.is_valid():
        card = form.save()
        return JsonResponse({'card': model_to_dict(card)}, status=200)
    else:
        return JsonResponse({'error': 'edit error'}, status=400)


@require_http_methods(['DELETE'])
@login_required
def delete_card(request, card_pk):
    card = Card.objects.select_related('deck__user').get(pk=card_pk)
    if card.deck.user != request.user:
        raise PermissionDenied
    card.delete()
    return JsonResponse({'message': 'delete successful'}, status=200)
