__author__ = 'Die Hu, mandihu@live.unc.edu, Onyen = mandihu'

import random

# Define main function.
def main():
    print("Play Blackjack!")

    # Play the game first time.
    play()

    # Ask the player whether they would like to play again.
    play_again = input("Would you like to play again? (y/n) ")

    # Validation.
    while (play_again != "y" and play_again != "n"):
        print(play_again, "is not a choice.")
        play_again = input("Please choose from \"y\" or \"n\": ")

    # If the player want to play again, call the play function to play again.
    while play_again == "y":
        play()
        play_again = input("Would you like to play again? (y/n) ")

        while (play_again != "y" and play_again != "n"):
            print(play_again, "is not a choice.")
            play_again = input("Please choose from \"y\" or \"n\": ")

def play():

    # Get the player's score.
    player = get_player_score()

    # Only when player's score is equal or less than 21 should we get the dealer's score.
    # Because when player's score is greater than 21, the player will lose the game directly
    if player <= 21:
        dealer = get_dealer_score()

        # Only when dealer's score is equal or less than 21 should we compare player's and dealer's scores.
        # Because when dealer's score is greater than 21 and
        # player's score has already been proved to be equal or less than 21,
        # the dealer will lose the game directly
        if dealer <=21:

            # Compare scores.
            player_vs_dealer(player,dealer)



def get_player_score():

    # Deal two cards and add their value.
    total_player = deal_card() + deal_card()

    # Ask the player to HIT(y) or STAY(n).
    print("Your hand of two cards has a total value of ", total_player,".", sep="")
    hit_or_stay = input("Would you like to take another card? (y/n) ")

    # Validation.
    while (hit_or_stay != "y" and hit_or_stay != "n"):
        print(hit_or_stay, "is not a choice.")
        hit_or_stay = input("Please choose from \"y\" or \"n\":")

    # When the play chooses HIT(y), deal one more card.
    while hit_or_stay == "y":
        total_player += deal_card()

        # When the player's current is equal and less than 21, ask he/she to HIT(y) or STAY(n).
        if total_player <= 21:
            print("Your hand of two cards has a total value of ", total_player, ".", sep="")
            hit_or_stay = input("Would you like to take another card? (y/n) ")

            # Validation.
            while (hit_or_stay != "y" and hit_or_stay != "n"):
                print(hit_or_stay, "is not a choice.")
                hit_or_stay = input("Please choose from \"y\" or \"n\":")

        # When the player's score is greater than 21, the player go bust and loses.
        else:
            print("You BUSTED with a total value of ", total_player, ".", sep="")
            print("***** You lose! *****")
            return total_player

    # If the player choose STAY(n), return total score of the player.
    if hit_or_stay == "n":
        print("You have stopped taking more cards with a hand value of ", total_player, ".", sep="")
        return total_player


def deal_card():

    # Deal a value ranging from 1 to 13(inclusive).
    card = random.randint(1,13)

    # If card's value equals to 11, 12, or 13, make card's value equals to 10.
    if card == 11 or card == 12 or card ==13:
        card = 10
        return card

    return card

def get_dealer_score():

    # Deal two cards and add their value.
    total_dealer = deal_card() + deal_card()

    # While the dealer's total score is less than 16, deal another card.
    while total_dealer < 16:
        total_dealer += deal_card()

        # If dealer's total score is greater than 21, the dealer loses and the player wins.
        if total_dealer > 21:
            print("The dealer BUSTED with a total value of ", total_dealer, ".", sep="")
            print("***** You win! *****")
            return total_dealer

    # If dealer's total score is equal or greater then 16, stop deal card to the dealer.
    if total_dealer >= 16:
        print("The dealer was dealt a hand value of ", total_dealer, ".", sep="")
        return total_dealer

def player_vs_dealer(player,dealer):

    # If player's score is greater than dealer's, the player wins.
    if player > dealer:
        print("***** You win! *****")

    # If player's score is equal or less than dealer's, the player loses.
    else:
        print("***** You lose! *****")

main()



