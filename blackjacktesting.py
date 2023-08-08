import unittest
from blackjack import Shoe, BlackjackGame

class TestShoe(unittest.TestCase):
    def test_draw_card(self):
        shoe = Shoe(num_decks=1)
        initial_length = len(shoe.cards)
        shoe.draw_card()
        self.assertEqual(len(shoe.cards), initial_length - 1)

    def test_shoe_reset(self):
        shoe = Shoe(num_decks=1, penetration=1)
        shoe.draw_card()
        self.assertEqual(len(shoe.cards), 52)

class TestHandManagement(unittest.TestCase):
    def test_add_card(self):
        game = BlackjackGame()
        game.deal()
        self.assertEqual(len(game.player_hand.cards), 2)
        self.assertEqual(len(game.dealer_hand.cards), 2)

    def test_hit(self):
        game = BlackjackGame()
        game.deal()
        game.hit(game.player_hand)
        self.assertEqual(len(game.player_hand.cards), 3)

class TestGameplayFeatures(unittest.TestCase):
    def test_split(self):
        game = BlackjackGame()
        # Force a pair to the player's hand for testing
        game.player_hand.add_card({'rank': '8', 'suit': 'Hearts'})
        game.player_hand.add_card({'rank': '8', 'suit': 'Clubs'})
        game.split(game.player_hand)
        self.assertEqual(len(game.split_hands), 2)

    def test_insurance(self):
        game = BlackjackGame()
        game.dealer_hand.add_card({'rank': 'A', 'suit': 'Spades'})
        self.assertTrue(game.offer_insurance())
        game.take_insurance(10)
        self.assertEqual(game.insurance_bet, 10)
