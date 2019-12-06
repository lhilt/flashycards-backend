from django.urls import path

from . import cards, decks

# current path: api/v1/

urlpatterns = [
    path('', cards.testing),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards', cards.list_cards),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards/new', cards.create_card),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards/<int:card_pk>/edit', cards.edit_card),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards/<int:card_pk>/delete', cards.delete_card),
    path('users/<int:user_pk>/decks', decks.list_decks),
    path('users/<int:user_pk>/decks/new', decks.create_deck),
    path('users/<int:user_pk>/decks/<int:deck_pk>', decks.edit_deck),
    path('users/<int:user_pk>/decks/<int:deck_pk>', decks.delete_deck),
]
