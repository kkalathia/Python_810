"""Implement a Rock/Papers/Scissors game where a human plays against the computer who randomly chooses a move."""
import random
def human_move() ->str:
    """ Ask the user for R, P, or S.  Loop until given a valid input """
    u_input: str = input("Please choose 'R' for Rock,'P' for Paper,'S' for Scissor or 'Q' to Quit : ")
    user_input = u_input.lower()
    return user_input

def computer_move() -> str:
    """ return the computer's random choice using random.choice """
    computer_c: str = (random.choice(['r', 'p', 's']))
    return computer_c

def play_game() -> bool:
    """ play Rock/Paper/Scissors
            The human may enter 'Q' or 'q' any time to stop the game.
            Get the human's move, the computer's move, and print a message with the winner.
            Return a bool to specify if the human wants to play again,
            i.e. False when the human wants to quit or True to play again
        """
    while True:
        u_input=human_move()
        print(f"You choose : {u_input}")
        computer_c = computer_move()
        print(f"I choose : {computer_c}")
        if u_input == computer_c:
            print(f"Tie:we both chose {u_input} ")

        elif u_input == 's':
            if computer_c == 'p':
                print(f"{u_input} beats {computer_c} - You Win!")
            else:
                print(f"{computer_c} beats {u_input} - I Win!")

        elif u_input == 'p':
            if computer_c == 'r':
                print(f"{u_input} beats {computer_c} - You Win!")
            else:
                print(f"{computer_c} beats {u_input} - I Win!")

        elif u_input == 'r':
            if computer_c == 's':
                print(f"{u_input} beats {computer_c} - You Win!")
            else:
                print(f"{computer_c} beats {u_input} - I Win!")

        elif u_input == 'q':
            break
        else:
            print("Please enter a Valid Input!!")


    def main() -> None:
        """ Play multiple games until the human asks to stop """
        again: bool = True
        while again:
            again = play_game()

        print("Thanks for playing!")

    if __name__ == "__main__":
        main()

