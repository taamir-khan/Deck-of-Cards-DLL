import random
from DoublyLinkedList import DoublyLinkedList, Node

class DeckOfCards:
    def __init__(self, cards):
        self.deck = DoublyLinkedList()
        self.set = set()
        for i in cards:
            self.deck.add_first(i)
        for i in cards:
            self.set.add(i)

    def deal_top(self):
        if len(self.deck) == 0: 
            raise RuntimeError("Can't deal from an empty deck")
        else: 
            removed = self.deck.remove_first()
            self.set.remove(removed)
            return removed
    
    def deal_bottom(self):
        if len(self.deck) == 0: 
            raise RuntimeError("Can't deal from an empty deck")
        else: 
            removed = self.deck.remove_last()
            self.set.remove(removed)
            return removed
    
    def is_cheating(self, card):
        return card not in self.set


