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
    "J",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "Q",
    "K",
    "A",
]


def sort_hands(line):
    cards, bid = line
    cards = list(cards)

    card_counts = {}
    for card in set(cards):
        card_counts[card] = cards.count(card)

    if "J" in card_counts and len(card_counts) > 1:
        j_count = card_counts.pop("J")
        best_card = max(card_counts, key=lambda x: card_counts[x])
        card_counts[best_card] += j_count

    hand_type = tuple(sorted(card_counts.values()))

    return HAND_TYPE_ORDER.index(hand_type), *(CARD_ORDER.index(card) for card in cards)


lines = sorted(lines, key=sort_hands)

total = 0
for i, (cards, bid) in enumerate(lines, start=1):
    total += int(bid) * i

print("Answer:", total)
