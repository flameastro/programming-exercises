# Rules of the "Rock, Paper, Scissors" game are:
# Rock beats Scissors,
# Scissors beat Paper,
# Paper beats Rock,
# Two identical moves are a draw.
# Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.
# Examples:
# "scissors",     "paper"     --> "Player 1 won!"
# "scissors",     "rock"      --> "Player 2 won!"
# "paper",        "paper"     --> "Draw!"
def rps(p1, p2):
    if (p1 == "rock" and p2 == "rock") or (p1 == "paper" and p2 == "paper") or (p1 == "scissors" and p2 == "scissors"):
        return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    elif (p1 == "rock" and p2 == "paper") or (p1 == "paper" and p2 == "scissors") or (p1 == "scissors" and p2 == "rock"):
        return "Player 2 won!"


if __name__ == "__main__":
    print(rps("rock", "scissors"))  # Player 1 won!
    print(rps("paper", "scissors"))  # Player 2 won!
    print(rps("paper", "paper"))  # Draw!
