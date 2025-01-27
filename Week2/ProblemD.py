import sys

input_data = sys.stdin.read()
lines = input_data.splitlines()

N = int(lines[0])
K = int(lines[1])

face_down_cards = set(range(1, N + 1))
card_to_picture = {}
unmatched_cards = {}
matched_pairs = 0

for i in range(2, 2 + K):
    C1, C2, P1, P2 = lines[i].split()
    C1, C2 = int(C1), int(C2)
    if P1 == P2:
        face_down_cards.discard(C1)
        face_down_cards.discard(C2)
        unmatched_cards.pop(C1, None)
        unmatched_cards.pop(C2, None)
        matched_pairs += 1
    else:
        card_to_picture[C1] = P1
        card_to_picture[C2] = P2
        unmatched_cards[C1] = P1
        unmatched_cards[C2] = P2

# Find pairs
pairs = []
used_cards = set()
for card in list(face_down_cards):
    if card in card_to_picture and card not in used_cards:
        picture = card_to_picture[card]
        for other_card in list(face_down_cards):
            if other_card != card and other_card in card_to_picture and card_to_picture[other_card] == picture and other_card not in used_cards:
                pairs.append((card, other_card))
                used_cards.add(card)
                used_cards.add(other_card)
                unmatched_cards.pop(card, None)
                unmatched_cards.pop(other_card, None)
                break

possible_pairs = 0
if (N - ((len(pairs) + matched_pairs) * 2)) == len(unmatched_cards) * 2:
        possible_pairs = len(unmatched_cards)

print(len(pairs) + possible_pairs)