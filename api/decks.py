import json

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from .models import Deck
from .forms import DeckForm

# Create your views here.
## controllers for DECKS

@require_http_methods(['GET'])
@login_required
def list_decks(request):
    decks = Deck.objects.filter(user=request.user)
    response = {'decks': list(decks.values())}
    return JsonResponse(response, status=200)


@require_http_methods(['POST'])
@login_required
def create_deck(request):
    form = DeckForm(json.loads(request.body))
    if form.is_valid():
        deck = form.save(commit=False)
        deck.user = request.user
        deck.save()
        return JsonResponse({'deck': model_to_dict(deck)}, status=201)
    else:
        return JsonResponse({'error': 'invalid form input'}, status=400)


@require_http_methods(['PUT'])
@login_required
def edit_deck(request, deck_pk):
    deck = get_object_or_404(
        Deck.objects.select_related('user'),
        pk=deck_pk
    )
    if deck.user != request.user:
        raise PermissionDenied
    form = DeckForm(json.loads(request.body), instance=deck)
    if form.is_valid():
        deck = form.save()
        return JsonResponse({'deck': model_to_dict(deck)}, status=200)
    else:
        return JsonResponse({'error': 'edit error'}, status=400)


@require_http_methods(['DELETE'])
@login_required
def delete_deck(request, deck_pk):
    deck = get_object_or_404(
        Deck.objects.select_related('user'),
        pk=deck_pk
    )
    if deck.user != request.user:
        raise PermissionDenied
    deck.delete()
    return JsonResponse({'message': 'delete successful'}, status=200)
