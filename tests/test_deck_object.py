from nose import *
import unittest
import json
from manager.deck import Deck

class TestDeployDeckConstruction(unittest.TestCase):

    def setUp(self):
        self.primary_deck = self._create_starting_deck()

    def _create_starting_deck(self):
        with open('data/deployment.json') as read_file:
            cards = json.load(read_file)
        return Deck('deploy', cards, 'deploy')

    def test_length_starting_deck(self):
        print len(self.primary_deck.starting_deck)
        for card in self.primary_deck.starting_deck:
            print card
        assert len(self.primary_deck.starting_deck) == 8

class TestAEDeckConstruction(unittest.TestCase):

    def setUp(self):
        self.primary_deck = self._create_starting_deck()
        self.test_shuffle = self._create_starting_deck()

    def _create_starting_deck(self):
        with open('data/action.json') as read_file:
            cards = json.load(read_file)
        return Deck('ae', cards, 'ae')

    def test_length_starting_deck(self):
        assert len(self.primary_deck.starting_deck) == 26

    def test_shuffling_starting_deck(self):
        assert self.primary_deck.starting_deck != self.test_shuffle.starting_deck

    def test_drawing_a_card(self):
        card = self.primary_deck.deal_card()
        assert card == self.primary_deck.discard[0]

    def test_auto_shuffle_deck(self):
        for x in range(0, 26):
            self.primary_deck.deal_card()
        card = self.primary_deck.deal_card()
        assert card == self.primary_deck.discard[0]
        assert len(self.primary_deck.discard) == 1

    def test_add_card_to_deck(self):
        self.primary_deck.add_card({'this is a new card': 'hi'})
        assert len(self.primary_deck.discard) == 0
        sum_new_cards = sum([1 for card in self.primary_deck.current_deck if card.get('this is a new card', None) is not None])
        assert sum_new_cards == 1
