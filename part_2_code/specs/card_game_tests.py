import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def test_check_for_ace(self):
        ace = Card("red", 1)
        game = CardGame()
        self.assertEqual(1, game.check_for_ace(ace))

    def test_highest_card(self):
        card1 = Card("black", 5)
        card2 = Card("red", 2)
        game = CardGame()
        self.assertEqual(card1, game.highest_card(card1, card2))

    def test_cards_total(self):
        card1 = Card("black", 5)
        card2 = Card("red", 2)
        card3 = Card("black", 6)
        cards = [card1, card2, card3]
        game = CardGame()
        self.assertEqual("You have a total of 13", game.cards_total(cards))