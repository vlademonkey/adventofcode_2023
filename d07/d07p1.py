import functools
import numpy

CARD_TO_NUM = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


@functools.total_ordering
class CCHand:
    def __init__(self, cards: str, bid: int):
        self.bid = int(bid)
        self.text = cards
        self.cards = []
        for c in cards:
            c = CARD_TO_NUM[c] if c in CARD_TO_NUM else int(c)
            self.cards.append(c)

        # Calculate hand strength
        cards, counts = numpy.unique(self.cards, return_counts=True)
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
        print(f"{self.text=} {self.cards=} {self.strength=} {self.bid=}")

    def __eq__(self, other):
        eqret = self.strength == other.strength and self.cards == other.cards
        print(f"EQ: {self.text=} {other.text=} RET={eqret}")
        return self.strength == other.strength and self.cards == other.cards

    def __lt__(self, other):
        if self.strength != other.strength:
            ltret = self.strength < other.strength
        else:
            for elem1, elem2 in zip(self.cards, other.cards):
                if elem1 != elem2:
                    ltret = elem1 < elem2
        print(f"LT: {self.text=}({self.strength}) {other.text=}({other.strength}) RET={ltret}")
        if self.strength != other.strength:
            return self.strength < other.strength
        for elem1, elem2 in zip(self.cards, other.cards):
            # print(f"{elem1=} {elem2=}")
            if elem1 != elem2:
                return elem1 < elem2


hands = []
with open("input-t1.txt") as fin:
    for line in fin:
        hand, bid = line.strip().split(" ")
        print(f"{hand=} {bid=}")
        hands.append(CCHand(hand, bid))

score = 0
for idx, hand in enumerate(sorted(hands)):
    print(f"{idx=} {hand.text} {hand.bid}")
    score += idx + 1 * hand.bid

print(score)
