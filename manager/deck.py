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

    def _shuffle(self, cards):
        return random.sample(cards, len(cards))
    
    def _create_starting_deck(self, type):
        if type == 'ae':
            number_of_blitz_total = 10
            number_to_choose = 2
            blitz_cards = [card for card in self.full_deck if card['blitz'] is True] * number_of_blitz_total
            non_blitz_cards = [card for card in self.full_deck if card['blitz'] is not True]
            ready_deck = non_blitz_cards + random.sample(blitz_cards, len(blitz_cards))[0:number_to_choose]
            return self._shuffle(ready_deck)
        elif type == 'deploy':
            non_unique_deploys = [card for card in self.full_deck if card['unique'] is False] 
            cost_6_cards = [card for card in non_unique_deploys if card['cost'] <= 6]
            return self._shuffle(cost_6_cards)
        elif type == 'class':
            zero_cost_cards = [card for card in self.full_deck if card['cost'] == 0]
            cards = self._shuffle(zero_cost_cards)
            self.full_deck = [card for card in self.full_deck if card['class'] == cards[0]['class']]
            return [cards[0]]
        else:
            return ValueError('Please select correct type of deck')

    def deal_card(self):
        if len(self.current_deck) == 0:
            self.current_deck = self._shuffle(self.discard)
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
        self.current_deck = self._shuffle(new_deck)
