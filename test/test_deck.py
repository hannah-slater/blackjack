import unittest
from src.deck import Deck
from src.card import Card

class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
    
    def test_draw(self):
        drawCard = self.deck.draw()
        self.assertIsInstance(drawCard, Card)

if __name__ == '__main__':
    unittest.main()
