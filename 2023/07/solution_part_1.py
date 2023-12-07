from pathlib import Path

input_text = Path("input.txt").read_text()

# input_text = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

lines = input_text.splitlines()
lines = [line.split() for line in lines]

HAND_TYPE_ORDER = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2),
    (1, 2, 2),
    (1, 1, 3),
    (2, 3),
    (1, 4),
    (5,),
]

CARD_ORDER = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]


def sort_hands(line):
    cards, bid = line
    cards = list(cards)

    hand_type = []
    for card in set(cards):
        hand_type.append(cards.count(card))

    hand_type = tuple(sorted(hand_type))

    return HAND_TYPE_ORDER.index(hand_type), *(CARD_ORDER.index(card) for card in cards)


lines = sorted(lines, key=sort_hands)

total = 0
for i, (cards, bid) in enumerate(lines, start=1):
    total += int(bid) * i

print("Answer:", total)
