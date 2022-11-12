from player import Player
from dealer import Dealer


def main():
    """
    Main function creates a player and a dealer while initiating the game.
    """

    # Define the player
    player = Player()
    # Define the dealer
    dealer = Dealer(player)
    # Tell the dealer to play the game
    dealer.gameCycle()


if __name__ == "__main__":
    main()
