import pandas as pd
import itertools

# Define the deck of 52 cards
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = list(itertools.product(suits, ranks))

# Define a function to determine the poker hand
def determine_poker_hand(cards):
    suits = [card[0] for card in cards]
    ranks = [card[1] for card in cards]
    rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
    is_flush = len(set(suits)) == 1
    sorted_ranks = sorted([int(rank) if rank.isdigit() else 11 if rank == 'Jack' else 12 if rank == 'Queen' else 13 if rank == 'King' else 1 for rank in ranks])  # Sort ranks by numerical value
    is_straight = len(set(sorted_ranks)) == 5 and (sorted_ranks[-1] - sorted_ranks[0] == 4)
    if is_flush and sorted_ranks == [1, 10, 11, 12, 13]:
        return 'Royal flush'
    if is_flush and is_straight:
        return 'Straight flush'
    if 4 in rank_count.values():
        return 'Four of a kind'
    if set(rank_count.values()) == {2, 3}:
        return 'Full house'
    if is_flush:
        return 'Flush'
    if is_straight or sorted_ranks == [1, 10, 11, 12, 13]:
        return 'Straight'
    if 3 in rank_count.values():
        return 'Three of a kind'
    if list(rank_count.values()).count(2) == 2:
        return 'Two pairs'
    if 2 in rank_count.values():
        return 'One pair'
    return 'Nothing in hand'

# Generate all permutations of 5 cards and save them along with the poker hand category
poker_hands = []
for perm in itertools.combinations(deck, 5):
    poker_hand = determine_poker_hand(perm)
    row = [card[0] for card in perm] + [card[1] for card in perm] + [poker_hand]
    poker_hands.append(row)

# Create a DataFrame from the generated data and save it as a CSV file
df = pd.DataFrame(poker_hands, columns=['Card1_Suit', 'Card2_Suit', 'Card3_Suit', 'Card4_Suit', 'Card5_Suit',
                                         'Card1_Rank', 'Card2_Rank', 'Card3_Rank', 'Card4_Rank', 'Card5_Rank',
                                         'Poker_Hand'])
df.to_csv('poker_hand_dataset.csv', index=False)

print("CSV file 'poker_hand_dataset.csv' generated successfully.")
