# Greg Geary
# User VS Computer game of Blackjack


from random import shuffle

class Card:
    """
    This is the header for the class Card.
    Any new card objects created will use the Card(card_num) method,
    which will be used to create card objects with a suit, rank, and value.
    Cards start facing down.
    """
    # class member variables - shared by all objects.
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    ranks = ["Jack", "Queen", "King"]

    def __init__(self, card_num):
        """
        __init__ will be run whenever a new card object is created
        ie: Card() is executed.
        Takes in 2 parameters, card_num(any number between 0 and 51),
        self(giving the object the ability to call it's own methods)
        """
    # Sets the Card's instance variables:
    # Cards start facing down
        self._facing_up = False

    # Sets its "suit" using the shared suits list.
    # Integer division of the initial card num determines the suit.
    # 1-13 spades, 14-26 hearts, 27-39 clubs, 40-52 diamonds
        self._suit = Card.suits[card_num // 13]

        # Use modules 13 to determine the card's "rank"
        # (e.g., Ace, King, Queen, Jack, 1, 2, ...)
        # and point "value" (2-10,11)
        num = card_num % 13
        # If num%13 == 0, its an Ace.
        if num == 0:
            self._rank = "Ace"
            self._value = 11
        # Jack if 10, Queen if 11, King if 12
        elif num in [10, 11, 12]:
            # access shared rank list to set ranks of J, Q, and K
            self._rank = Card.ranks[num - 10]
            self._value = 10
        # Else rank and value is it's number +1
        # (card 1, refers to 2 of spades worth 2 points)
        else:
            self._rank = str(num + 1)
            self._value = num + 1

    # a "getter" for the suit type. Returns the string value of the suit
    def get_suit(self):
        return self._suit

    # a "getter" for the rank, returns string of rank
    def get_rank(self):
        return self._rank

    # value getter, returns int value
    def get_value(self):
        return self._value

    # facing_up getter, return boolean
    def get_face_up(self):
        return self._facing_up
    """
        setters for rank, value, and suit are not implemented
        since card suits, values and ranks cannot be changed.
        two setters are implements for "facing up " attribute,
         face_down() and face_up()
    """
    # turns card face down
    def face_down(self):
        self._facing_up = False

    # turns card face_up
    def face_up(self):
        self._facing_up = True
    """
    Overwrites the built-in str() function for the Card class
    Without it the print method would simply print the
    "memory address" of the object
    With it, if the card is facing up it prints its rank and suit,
    else it prin ts "<facedown>"
    """

    def __str__(self):
        # If the card is facing up, print rank of suit
        if self._facing_up:
            return self._rank + " of " + self._suit
        # If face down print <facedown>
        else:
            return "<facedown>"


class ChipBank:
    """
    Header for class ChipBank
    Used to store a dollar amount
    """

    # Initializes the chipbank with a dollar value
    def __init__(self, value):
        self._value = value

    # Tries to withdraw the amount from the current saved value.
    # If one tries to with draw more than they have,
    # they will only get as much as they have.
    # Returns the total amount withdrawn (the amount asked for,
    # or the total amount they had)
    def withdraw(self, amount):
        total = self._value
        self._value -= amount
        if self._value < 0:
            self._value = 0
            return total  # returns original balance
        return amount  # only return amount if they had enough to take it all

    # adds amount to total value and saves it
    def deposit(self, amount):
        self._value += amount

    # returns the total value of bank
    def get_balance(self):
        return self._value

    # Overwrites the built in str() function for the ChipBank class.
    # Prints the amount and types of chips stored in bank
    def __str__(self):
        return "%d blacks, %d greens, %d reds, %d blues - totaling $%d" % \
               (self._value // 100,
                self._value % 100 // 25,
                self._value % 25 // 5,
                self._value % 5,
                self._value)


class BlackjackHand:

    def __init__(self, type_player):
        self.hand_value = 0
        self.hand = []
        self.type_player = type_player

    def add_card(self, new_card):
        self.hand.append(new_card)

    def __str__(self):
        print(self.type_player + " hand is : ")
        for card in self.hand:
            if card.get_face_up():
                print(str(card.get_rank()) + " of " + str(card.get_suit()))
            else:
                print('<face down>')

    def get_value(self):
        self.hand_value = 0
        num_aces = 0

        for card in self.hand:
            num = card.get_value()
            self.hand_value = self.hand_value + num
            if card.get_rank() == 'Ace':
                num_aces = num_aces + 1

        while self.hand_value > 21 and num_aces > 0:
            self.hand_value = self.hand_value - 10
            num_aces = num_aces - 1

        return self.hand_value

    def face_up_first(self):
        self.hand[0].face_up()


class Blackjack:

    def __init__(self, starting_dollars):
        self.starting_dollars = starting_dollars
        self.bank = ChipBank(self.starting_dollars)
        self.deck = []
        self.wager = None
        self.player_hand = None
        self.dealer_hand = None

        self._active = False

        for i in range(0, 51):
            card = Card(i)
            self.deck.append(card)

        shuffle(self.deck)

    def draw(self):
        # Pop two cards for players hand
        card = self.deck.pop()
        card.face_up()
        self.player_hand.add_card(card)
        card = self.deck.pop()
        card.face_up()
        self.player_hand.add_card(card)

        # Pop two cards for dealers hand
        card = self.deck.pop()
        self.dealer_hand.add_card(card)
        card = self.deck.pop()
        card.face_up()
        self.dealer_hand.add_card(card)

    def start_hand(self, wager):
        self.wager = wager
        self.player_hand = BlackjackHand('player')
        self.dealer_hand = BlackjackHand('dealer')
        self.draw()
        self.player_hand.__str__()
        self.dealer_hand.__str__()
        self._active = True
    """
    This method should be called when a winner has been determined.
    This method is passed a parameter outcome,
    which will be “win”, “lose”, or “push” depending
    on if the player won, the dealer won, or their was a tie.
    If the player wins they should be given double their wager back.
    A push should refund the original wager, and a lose should
    result in no money being deposited.
    This method is also responsible for setting the two hands and
    the wager back to None.
    This method should be called by any of the other methods in which a
    winner is found.
    """
    def end_hand(self, outcome):

        # If the player wins they should be given double their wager back.
        if outcome == "win":
            self.bank.deposit(2*self.wager)
        elif outcome == "push":
            self.bank.deposit(self.wager)
        else:
            self.bank.withdraw(self.wager)

        # Set the two hands and the wager back to None
        self.wager = None
        self.player_hand = None
        self.dealer_hand = None
        self._active = False

    def game_active(self):
        return self._active
    """
    The player chooses to hit. Draw a card for the player,
    and display the player’s new hand. If they exceed 21 they bust,
    and if they get 21 exactly they are forced to stand.
    This method takes no parameters, and has no return value.
    """
    def hit(self):
        # Draws a card for the player
        card = self.deck.pop()
        self.player_hand.add_card(card)
        card.face_up()

        # Display players new hand
        self.player_hand.__str__()

        # Check if value exceeds 21 then bust
        if self.player_hand.get_value() > 21:
            print('You busted.')
            self.end_hand("lose")
        # If 21 exactly forced to stand
        elif self.player_hand.get_value() == 21:
            print('You win.')
            self.end_hand("win")
    """
    The player stands, and the dealer flips their hidden card face up,
    and begins the process of drawing.
    The dealer only draws if their hands current value is 16 or less.
    If the dealer draws over 21, they bust and the player wins.
    After the dealer is done drawing, and neither has busted,
    the higher valued hand wins. Ties can occur, and are called “pushes.”
    This method has no parameters and no return value.
    """
    def stand(self,):
        self.dealer_hand.face_up_first()

        if self.dealer_hand.get_value() <= 15:
            card = self.deck.pop()
            card.face_up()
            self.dealer_hand.add_card(card)

        elif (self.dealer_hand.get_value()) < 21:
            print("Dealer Loses")
            self.end_hand("win")

        if (self.player_hand.get_value()) < (self.dealer_hand.get_value()):
            print('You lose')
            self.end_hand('lose')

        elif self.player_hand.get_value() > self.dealer_hand.get_value():
            print('You win!')
            self.end_hand("win")

        self.dealer_hand.__str__()

        if (self.dealer_hand.get_value()) > 21:
            print('Dealer busted.')
            self.end_hand("win")

        elif (self.player_hand.get_value()) > 21:
            print('Player busted.')
            self.end_hand("lose")

        # If 21 exactly forced to stand
        if (self.player_hand.get_value()) == 21:
            print('You win.')
            self.end_hand("win")
        elif (self.dealer_hand.get_value()) == 21:
            print("You Lose.")
            self.end_hand("lose")


# Main method to run tests
def main():
    if __name__ == "__main__":
        blackjack = Blackjack(250)
        while blackjack.bank._value > 0:
            print("Your remaining chips: " + str(blackjack.bank))
            wager = int(input("How much would you like to wager?"))
            blackjack.start_hand(wager)
            while blackjack.game_active():
                choice = input("STAND or HIT: ").upper()
                if choice == "STAND":
                    blackjack.stand()
                elif choice == "HIT":
                    blackjack.hit()
            print()
    print("Out of Money! The casino Wins!")


main()
