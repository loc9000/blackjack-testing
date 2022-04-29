from multiprocessing.sharedctypes import Value
import unittest
from blackjack import Hand, Player, Dealer, Card, Deck, Blackjack

class TestBlackjack(unittest.TestCase):

    def test_card_attributes(self):
        card = Card("Spade", 4)
        card1 = Card("Heart", 7)

        self.assertEqual(str(card), '<Card: [Spade 4]>')

        self.assertEqual(card1.rank, 7)
        self.assertEqual(card1.suit, 'Heart')
        
    def test_hand_is_a_list(self):
        hand = Hand()

        self.assertTrue(hand, [])
    
    def test_deck_size(self):
        deck = Deck()

        self.assertEqual(len(deck.cards), 52)
        self.assertNotEqual(len(deck.cards), 42)

    def test_hand_total(self):
        hand = Hand()
        hand.holding = [Card('Heart', 7), Card('Spade', 4)]

        self.assertEqual(hand.get_total(), 11)

    def test_game_over(self):
        human = Player()
        hand = Hand()
        blackjack = Blackjack()
        hand.holding = [Card('Heart', 7), Card('Spade', 7), Card('Heart', 10)]

        self.assertTrue(human.game_over)
        