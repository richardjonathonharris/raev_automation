import random

class Deck(object):
    
    def __init__(self, name, cards, type):
        self.name = name
        self.full_deck = self._populate_deck(cards)
        self.starting_deck = self._create_starting_deck(type)
        self.current_deck = self.starting_deck
        self.discard = []

    def _populate_deck(self, cards):
        return [card for card in cards]
    
    def _create_starting_deck(self, type):
        if type == 'ae':
            number_of_blitz_total = 10
            number_to_choose = 2
            blitz_cards = [card for card in self.full_deck if card['blitz'] is True] * number_of_blitz_total
            non_blitz_cards = [card for card in self.full_deck if card['blitz'] is not True]
            ready_deck = non_blitz_cards + random.sample(blitz_cards, len(blitz_cards))[0:number_to_choose]
            return random.sample(ready_deck, len(ready_deck))
        else:
            return ValueError('Please select correct type of deck')

    def deal_card(self):
        if len(self.current_deck) == 0:
            self.current_deck = random.sample(self.discard, len(self.discard))
            self.discard = []
        else:
            pass
        chosen_card = self.current_deck.pop(0)
        self.discard.append(chosen_card)
        return chosen_card

    def add_card(self, new_card):
        new_deck = self.current_deck
        if len(self.discard) > 0:
            self.new_deck.append([card for card in self.discard])
            self.discard = []
        new_deck.append(new_card)
        self.current_deck = random.sample(new_deck, len(new_deck))
