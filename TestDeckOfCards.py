from DeckOfCards import DeckOfCards
import random
import unittest
random.seed(622)
class TestDeckOfCards(unittest.TestCase):
    def test_deal_top(self):
        cards = ['Four of Hearts', 'Queen of Diamonds', 'Ace of Spades']
        deck = DeckOfCards(cards)
        self.assertEqual(deck.deal_top(), 'Ace of Spades')

    def test_deal_bottom(self):
        cards = ['Jack of Spades', 'Queen of Clubs', 'Ace of Diamonds']
        deck = DeckOfCards(cards)
        self.assertEqual(deck.deal_bottom(), "Jack of Spades")

    def test_empty_deck_top(self):
        cards = []
        deck = DeckOfCards(cards)
        with self.assertRaises(RuntimeError):
            deck.deal_top() == "Can't deal from an empty deck"   

    def test_empty_deck_bot(self):
        cards = []
        deck = DeckOfCards(cards)
        with self.assertRaises(RuntimeError):
            deck.deal_bottom() == "Can't deal from an empty deck"

    def test_is_cheating(self):
        cards = ['Four of Hearts', 'Queen of Diamonds', 'Ace of Spades']
        deck = DeckOfCards(cards)
        deck.deal_top()
        self.assertEqual(deck.is_cheating("Ace of Spades"), True)
        self.assertEqual(deck.is_cheating("Queen of Diamonds"), False)
        
unittest.main()