# W01: Prove: Tic-Tac-Toe
# Luke McLean


def main():
    squares = {
        1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

    board(squares)
    print("")
    keepPlaying = True

    while keepPlaying:
        if keepPlaying == True:
            player1Turn(squares)
            board(squares)
        if winner(squares) == False:
            print("")
            keepPlaying = False

        if keepPlaying == True:
            player2Turn(squares)
            board(squares)
        if winner(squares) == False:
            print("")
            keepPlaying = False


def board(squares):
    print("")
    for key, value in squares.items():
        if key == 3 or key == 6:
            print(value, end="\n")
            print("-+-+-")
        elif key == 9:
            print(value)
        else:
            print(value, end="|")


def player1Turn(squares):
    nextTurn = False
    while nextTurn == False:
        print("")
        choice = int(input("\nx's turn to choose a square (1-9): "))
        if choice not in squares:
            print("Please enter a valid number")
        elif squares[choice] == "O" or squares[choice] == "X":
            print("Please enter a different number")
        else:
            squares.update({choice: "X"})
            nextTurn = True


def player2Turn(squares):
    nextTurn = False
    while nextTurn == False:
        print("")
        choice = int(input("\no's turn to choose a square (1-9): "))
        if choice not in squares:
            print("Please enter a valid number")
        elif squares[choice] == "O" or squares[choice] == "X":
            print("Please enter a different number")
        else:
            squares.update({choice: "O"})
            nextTurn = True


def winner(squares):
    win = False
    for key, value in squares.items():
        # Player 1 Wins
        if squares[1] == "X" and squares[2] == "X" and squares[3] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[1] == "X" and squares[4] == "X" and squares[7] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[1] == "X" and squares[5] == "X" and squares[9] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[2] == "X" and squares[5] == "X" and squares[8] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[3] == "X" and squares[6] == "X" and squares[9] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[3] == "X" and squares[5] == "X" and squares[7] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[4] == "X" and squares[5] == "X" and squares[6] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[7] == "X" and squares[8] == "X" and squares[9] == "X":
            print("\nX wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False

        # Player 2 Wins
        elif squares[1] == "O" and squares[2] == "O" and squares[3] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[1] == "O" and squares[4] == "O" and squares[7] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[1] == "O" and squares[5] == "O" and squares[9] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[2] == "O" and squares[5] == "O" and squares[8] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[3] == "O" and squares[6] == "O" and squares[9] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[3] == "O" and squares[5] == "O" and squares[7] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[4] == "O" and squares[5] == "O" and squares[6] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False
        elif squares[7] == "O" and squares[8] == "O" and squares[9] == "O":
            print("\nO wins!")
            print("\nGood game. Thanks for playing!")
            win = True
            return False

        # Stale mate draw
        elif squares[1].isnumeric() == False and squares[2].isnumeric() == False and squares[3].isnumeric() == False and squares[4].isnumeric() == False and squares[5].isnumeric() == False and squares[6].isnumeric() == False and squares[7].isnumeric() == False and squares[8].isnumeric() == False and squares[9].isnumeric() == False and win == False:
            print("\nStale mate draw!")
            print("\nGood game. Thanks for playing!")
            return False

if __name__ == "__main__":
    print("Hello! Welcome to a game of Tic Tac Toe!")
    main()
