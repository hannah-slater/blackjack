import unittest
from src.player import Player
from src.deck import Deck

class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test")
        self.deck = Deck()

    def tearDown(self): 
        pass

    def test_CreateHand(self):
        #has two cards in hand
        self.player.createHand(self.deck)
        h = self.player.getHand()
        self.assertEqual(h.amountCards(), 2)

    def test_Hit(self):
        #gains a card, score is updated
        scoreAtStart = self.player.getValue()
        self.player.hit(self.deck)
        scoreAfter = self.player.getValue()
        h = self.player.getHand()
        self.assertEqual(h.amountCards(), 1)
        self.assertNotEqual(scoreAtStart, scoreAfter)

if __name__ == '__main__':
    unittest.main()