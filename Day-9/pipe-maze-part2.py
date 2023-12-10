with open('camel-cards-input.txt', 'r') as input_file:
    lines = input_file.readlines()
hand_bid_tuples = []
for line in lines:
    hand, bid = line.split()
    hand_bid_tuples.append((hand, int(bid)))
def rank(hand):
    counts = [hand.count(card) for card in hand]
    print(counts)
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts: # full house
            return 4
        return 3
    if counts.count(2) == 4: # two pair
        return 2
    if 2 in counts:
        return 1
    return 0
def replace(hand):
    if hand == "":
        return [""]
    return [
        replaced + remaining
        for replaced in ("23456789TQKA" if hand[0] == "J" else hand[0]) # replace J with all other possible cards
        for remaining in replace(hand[1:])
    ]
def rank_wildcard(hand):
    return max(map(rank, replace(hand)))
ranks = {"T": "A", "J": "/", "Q": "C", "K": "D", "A": "E"} # map face cards to letters in order, J becomes / because it has lower 
def hand_strength(hand):
    return (rank_wildcard(hand), [ranks.get(card, card) for card in hand]) 
hand_bid_tuples.sort(key=lambda hand_bid: hand_strength(hand_bid[0]))
result = 0
for rank, (hand, bid) in enumerate(hand_bid_tuples, 1):
    result += rank * bid
print(result)