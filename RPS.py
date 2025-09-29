import random
#Rock paper scissors game - George Pollard + many resources from the internet
# Mapping of user input to game choices
CHOICE_MAPPING = {"r": "Rock", "p": "Paper", "s": "Scissors"}
# Mapping of winning relationships: key beats value
WINNING_RELATIONSHIP = {"r": "s", "p": "r", "s": "p"}

def get_user_choice():
    """
    Prompt the user to select Rock, Paper, Scissors, or Quit.
    Returns the user's choice as a single character or None if quitting.
    """
    while True:
        user_input = input("Choose [R]ock, [P]aper, [S]cissors (or Q to quit): ").strip().lower()
        if user_input == "q":
            return None
        if user_input and user_input[0] in CHOICE_MAPPING:
            return user_input[0]
        print("Invalid input. Enter R, P, S, or Q.")

def play_round():
    """
    Conduct a single round of Rock, Paper, Scissors.
    Returns the result of the round ("tie", "user", or "computer") and the choices made.
    """
    user_choice = get_user_choice()
    if user_choice is None:
        return None, None

    computer_choice = random.choice(list(CHOICE_MAPPING.keys()))
    print(f"You: {CHOICE_MAPPING[user_choice]}  |  Computer: {CHOICE_MAPPING[computer_choice]}")

    if user_choice == computer_choice:
        return "tie", (user_choice, computer_choice)
    if WINNING_RELATIONSHIP[user_choice] == computer_choice:
        return "user", (user_choice, computer_choice)
    return "computer", (user_choice, computer_choice)

def play_best_of(rounds):
    """
    Play a best-of series of Rock, Paper, Scissors.
    The first to win the majority of rounds wins the match.
    """
    rounds_needed_to_win = rounds // 2 + 1
    user_score = computer_score = 0
    round_number = 1

    while user_score < rounds_needed_to_win and computer_score < rounds_needed_to_win:
        print(f"\nRound {round_number} — Score You {user_score} : Computer {computer_score}")
        result, _ = play_round()
        if result is None:
            print("Game aborted by user.")
            return
        if result == "user":
            user_score += 1
            print("You win the round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins the round!")
        else:
            print("Round is a tie.")
        round_number += 1

    print(f"\nFinal Score You {user_score} : Computer {computer_score}")
    if user_score > computer_score:
        print("You won the match! 🎉")
    else:
        print("Computer won the match. Try again!")

def main():
    """
    Main function to start and manage the Rock, Paper, Scissors game.
    Allows the user to play multiple matches.
    """
    print("Rock Paper Scissors")
    while True:
        user_input = input("\nEnter number of rounds (odd number, e.g., 1,3,5) or Q to quit: ").strip().lower()
        if user_input == "q":
            print("Goodbye.")
            break
        if not user_input.isdigit():
            print("Please enter an odd positive integer or Q.")
            continue

        total_rounds = int(user_input)
        if total_rounds <= 0 or total_rounds % 2 == 0:
            print("Please enter a positive odd number (best-of).")
            continue

        play_best_of(total_rounds)

        play_again = input("\nPlay another match? (Y/N): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing. Goodbye.")
            break

if __name__ == "__main__":
    main()