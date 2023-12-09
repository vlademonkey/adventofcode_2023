import functools
import numpy

CARD_TO_NUM = {
    "T": 10,
    "Q": 12,
    "J": 0,  # Joker!
    "K": 13,
    "A": 14,
}


@functools.total_ordering
class CCHand:
    def __init__(self, cards: str, bid: int):
        self.bid = int(bid)
        self.text = cards
        self.cards = []
        self.num_jokers = 0
        for c in cards:
            c = CARD_TO_NUM[c] if c in CARD_TO_NUM else int(c)
            if c == 0:
                self.num_jokers += 1
            self.cards.append(c)

        # print(f"{self.text=} {self.cards=} {self.num_jokers=}")

        # Calculate hand strength
        cards_no_jokers = numpy.array([card for card in self.cards if card != 0])
        if len(cards_no_jokers) == 0:  # All jokers edge-case.
            counts = [5]
        else:
            _, counts = numpy.unique(cards_no_jokers, return_counts=True)
            max_idx = counts.argmax(axis=0)  # Max card count
            counts[max_idx] += self.num_jokers  # Add jokers
            counts = list(counts)

        self.strength = 0
        if 5 in counts:  # Five of a kind
            self.strength = 7
        elif 4 in counts:  # Four of a kind
            self.strength = 6
        elif 3 in counts and 2 in counts:  # Full house
            self.strength = 5
        elif 3 in counts:  # Three of a kind
            self.strength = 4
        elif 2 in counts and counts.count(2) == 2:
            self.strength = 3  # Two pairs
        elif 2 in counts:
            self.strength = 2  # One pair
        else:
            self.strength = 1

    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        if self.strength != other.strength:
            return self.strength < other.strength
        for elem1, elem2 in zip(self.cards, other.cards):
            if elem1 != elem2:
                return elem1 < elem2


hands = []
with open("input.txt") as fin:
    for line in fin:
        hand, bid = line.strip().split(" ")
        hands.append(CCHand(hand, bid))

score = 0
for idx, hand in enumerate(sorted(hands)):
    # print(f"{hand.text=} {hand.strength=}")
    score += (idx + 1) * hand.bid

print(score)
