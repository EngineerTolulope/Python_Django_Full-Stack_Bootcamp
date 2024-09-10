#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# Welcome to the "War" card game project. The game is designed for two players:
# you and the computer. The objective is to win all the cards from the opponent.
# The basic rules are:
# 1. The deck is divided evenly, each player gets 26 cards.
# 2. Each player plays a card; the higher card wins both.
# 3. In case of a tie, a "War" occurs, and additional cards are used to determine the winner.
# 4. The game continues until one player has all the cards or one player runs out of cards.

from random import shuffle

SUITS = 'Hearts Diamonds Spades Clubs'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    Represents a deck of 52 playing cards.
    Provides methods to shuffle and split the deck into two halves.
    """
    def __init__(self):
        print("Creating New Ordered Deck")
        self.cards = [(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        print("Shuffling Cards")
        shuffle(self.cards)

    def split(self):
        return self.cards[:26], self.cards[26:]

class Hand:
    """
    Represents a player's hand of cards.
    Provides methods to add cards and remove the top card.
    """
    def __init__(self, cards):
        self.cards = cards

    def __str__(self) -> str:
        return f"Contains {len(self.cards)} cards"

    def add(self, cards):
        self.cards.extend(cards)

    def remove_card(self):
        return self.cards.pop()

    def has_enough_cards_for_war(self):
        return len(self.cards) >= 4

class Player:
    """
    Represents a player in the game.
    Each player has a name and a hand of cards.
    Provides methods to play a card, prepare for war, and check if the player still has cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} plays: {drawn_card}")
        return drawn_card

    def prepare_for_war(self):
        war_cards = []
        if self.hand.has_enough_cards_for_war():
            for _ in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards
        else:
            return self.hand.cards  # Return all remaining cards if not enough for full war

    def has_cards(self):
        return len(self.hand.cards) > 0

def determine_winner(card1, card2):
    """
    Determines the winner based on the rank of the cards.
    """
    return RANKS.index(card1[1]) > RANKS.index(card2[1])

def play_game():
    print("Welcome to War, let's begin...")

    # Initialize deck and players
    deck = Deck()
    deck.shuffle()
    half1, half2 = deck.split()

    computer = Player("Computer", Hand(half1))
    user_name = input("What is your name? ")
    user = Player(user_name, Hand(half2))

    total_rounds = 0
    war_count = 0

    while user.has_cards() and computer.has_cards():
        total_rounds += 1
        print("\nNew Round!")
        print(f"{user.name} has {len(user.hand.cards)} cards")
        print(f"{computer.name} has {len(computer.hand.cards)} cards")

        table_cards = [computer.play_card(), user.play_card()]

        while table_cards[0][1] == table_cards[1][1]:
            war_count += 1
            print("War!")
            # Prepare for war
            table_cards.extend(user.prepare_for_war())
            table_cards.extend(computer.prepare_for_war())

            if not user.has_cards() or not computer.has_cards():
                print("A player ran out of cards during the war.")
                break

            table_cards.extend([computer.play_card(), user.play_card()])

        if determine_winner(table_cards[-2], table_cards[-1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

    print(f"\nGame over! Total rounds: {total_rounds}")
    print(f"Wars occurred: {war_count}")
    print(f"Does the computer still have cards? {'Yes' if computer.has_cards() else 'No'}")
    print(f"Does {user.name} still have cards? {'Yes' if user.has_cards() else 'No'}")

# Run the game
if __name__ == "__main__":
    play_game()
