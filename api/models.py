from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="decks"
    )

    def __str__(self):
        return self.name


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name="cards"
    )
