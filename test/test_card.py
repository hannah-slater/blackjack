import unittest
from src.card import Card


class CardTestCase(unittest.TestCase):

    def setUp(self):
        self.card = Card("Suit", "Name", 1)

    def tearDown(self): 
        pass

    def test_getCard(self):
        cardString = self.card.getCard()
        self.assertEqual(cardString, "Name of Suit")
    
    def test_value(self):
        cardValue = self.card.getValue()
        self.assertEqual(cardValue, 1)

if __name__ == '__main__':
    unittest.main()