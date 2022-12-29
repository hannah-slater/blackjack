import unittest
from src.dealer import Dealer
from src.player import Player
from src.deck import Deck

class DealerTestCase(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer("Dealer")
        self.player = Player("player")
        self.player2 = Player("player")
        self.deck = Deck()
        self.dealer.createHand(self.deck) #K, Q
        self.player.createHand(self.deck) #J, 10
        self.player2.createHand(self.deck) #9, 8

    def tearDown(self): 
        pass

    def test_Evaluate(self):
        a = self.dealer.evaluate(self.player)
        self.assertEqual(a, "DRAW")
    
    def test_Evaluate2(self):
        a = self.dealer.evaluate(self.player2)
        self.assertEqual(a, "LOSE")

if __name__ == '__main__':
    unittest.main()