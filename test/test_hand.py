import unittest
from src.hand import Hand
from src.deck import Deck
from src.card import Card

class HandTestCase(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()
        self.deck = Deck()

    def tearDown(self): 
        pass

    def test_CalculateValue(self):
        self.hand.addCard(self.deck, 1)
        self.hand.calculateValue()
        a = self.hand.getValue()
        self.assertEqual(a, 10)

    def test_Clear(self):
        self.hand.addCard(self.deck, 1)
        self.hand.clear()
        self.assertEqual(self.hand.getCards(), [])

    def test_KingAce(self):
        self.hand.addCardTest(Card("Suit", "King", 10))
        self.hand.addCardTest(Card("Suit", "Ace", 1))
        a = self.hand.getValue()
        self.assertEqual(a, 21)

    def test_KingQueenAce(self):
        self.hand.addCardTest(Card("Suit", "King", 10))
        self.hand.addCardTest(Card("Suit", "Queen", 10))
        self.hand.addCardTest(Card("Suit", "Ace", 1))
        a = self.hand.getValue()
        self.assertEqual(a, 21)

    def test_NineAceAce(self):
        self.hand.addCardTest(Card("Suit", "9", 9))
        self.hand.addCardTest(Card("Suit", "Ace", 1))
        self.hand.addCardTest(Card("Suit", "Ace", 1))
        a = self.hand.getValue()
        self.assertEqual(a, 21)

    def test_valid(self):
        self.hand.addCardTest(Card("Suit", "9", 9))
        a = self.hand.getValid()
        self.assertEqual(a, True)

    def test_edgeValid(self):
        self.hand.addCardTest(Card("Suit", "King", 10))
        self.hand.addCardTest(Card("Suit", "5", 5))
        self.hand.addCardTest(Card("Suit", "6", 6))
        a = self.hand.getValid()
        self.assertEqual(a, True)

    def test_notValid(self):
        self.hand.addCardTest(Card("Suit", "9", 9))
        self.hand.addCardTest(Card("Suit", "King", 10))
        self.hand.addCardTest(Card("Suit", "3", 3))
        a = self.hand.getValid()
        self.assertEqual(a, False)

if __name__ == '__main__':
    unittest.main()