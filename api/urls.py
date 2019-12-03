from django.urls import path

from . import cards, decks

# current path: api/v1/

urlpatterns = [
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards', cards.list_cards),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards', cards.create_card),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards', cards.edit_card),
    path('users/<int:user_pk>/decks/<int:deck_pk>/cards', cards.delete_card),
    path('users/<int:user_pk>/decks', decks.list_decks),
    path('users/<int:user_pk>/decks', decks.create_deck),
    path('users/<int:user_pk>/decks/<int:deck_pk>', decks.edit_deck),
    path('users/<int:user_pk>/decks/<int:deck_pk>', decks.delete_deck),
]
