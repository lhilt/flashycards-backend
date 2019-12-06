from django.urls import path

from . import cards, decks

# current path: api/v1/

urlpatterns = [
    path('decks/<int:deck_pk>/cards', cards.list_cards),
    path('decks/<int:deck_pk>/cards/new', cards.create_card),
    path('cards/<int:card_pk>/edit', cards.edit_card),
    path('cards/<int:card_pk>/delete', cards.delete_card),
    path('decks', decks.list_decks),
    path('decks/new', decks.create_deck),
    path('decks/<int:deck_pk>/edit', decks.edit_deck),
    path('decks/<int:deck_pk>', decks.delete_deck),
]
