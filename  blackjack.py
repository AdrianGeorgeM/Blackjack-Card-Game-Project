# Import the random module. This module implements pseudo-random number generators for various distributions.
import random

# Create an empty list to hold the deck of cards.
cards = []

# Define the suits and ranks that make up a deck of cards.
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Use a nested loop to create the deck of cards.
for suit in suits:
    for rank in ranks:
        # Append each card as a list of [suit, rank] to the cards list.
        cards.append([suit, rank])


# Define a function to shuffle the deck of cards.
def shuffle_cards():
    # The shuffle() function randomizes the items of a list in place.
    random.shuffle(cards)


# Define a function to deal a specified number of cards.
def deal_card(number):
    # Create an empty list to hold the dealt cards.
    cards_dealt = []
    for i in range(number):
        # Remove the last card from the deck and store it in the card variable.
        card = cards.pop()
        # Append the dealt card to the cards_dealt list.
        cards_dealt.append(card)
    # Return the cards_dealt list.
    return cards_dealt


# Define a function to calculate the value of a hand of cards.
def get_value(hand):
    # Initialize the total value of the hand and the number of aces in the hand.
    value = 0
    aces = 0
    # Loop through each card in the hand.
    for card in hand:
        # Get the rank of the card.
        rank = card[1]
        # If the rank is an Ace, add 11 to the value and increase the count of aces.
        if rank == "A":
            value += 11
            aces += 1
        # If the rank is a face card (Jack, Queen, or King), add 10 to the value.
        elif rank in ["J", "Q", "K"]:
            value += 10
        # Otherwise, convert the rank to an integer and add it to the value.
        else:
            value += int(rank)
    # If the value is over 21 and there's an Ace in the hand, reduce the value by 10 for each Ace until it's 21 or less.
    while value > 21 and aces:
        value -= 10
        aces -= 1
    # Return the value of the hand.
    return value


# Shuffle the deck of cards before starting the game.
shuffle_cards()

# Deal two cards each to the player and the dealer.
player_hand = deal_card(2)
dealer_hand = deal_card(2)

# Print the player's hand and one of the dealer's cards.
print("Player hand: ", player_hand)
print("Dealer shows: ", dealer_hand[0])

# Start the player's turn.
while True:
    # Ask the player if they want to hit or stay.
    action = input("Do you want to hit or stay? (h/s): ")
    if action.lower() == "h":
        # If the player chooses to hit, deal another card and add it to their hand.
        player_hand.extend(deal_card(1))
        print("Player hand: ", player_hand)
        # If the value of the player's hand is over 21, they bust and the game ends.
        if get_value(player_hand) > 21:
            print("Player busts! Dealer wins.")
            break
    else:
        # If the player chooses to stay, end their turn.
        break

# If the player hasn't busted, start the dealer's turn.
if get_value(player_hand) <= 21:
    # The dealer must hit until they have 17 or more.
    while get_value(dealer_hand) < 17:
        dealer_hand.extend(deal_card(1))
    print("Dealer hand: ", dealer_hand)
    # If the value of the dealer's hand is over 21, they bust and the player wins.
    if get_value(dealer_hand) > 21:
        print("Dealer busts! Player wins.")
    # If neither the player nor the dealer has busted, compare their hands to determine the winner.
    elif get_value(dealer_hand) > get_value(player_hand):
        print("Dealer wins.")
    elif get_value(dealer_hand) < get_value(player_hand):
        print("Player wins.")
    else:
        print("It's a draw.")
