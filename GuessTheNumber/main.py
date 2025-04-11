from random import randint
from art import logo
print(logo)

EASY_TURN = 10
HARD_TURN = 5

def check_answer(user_guess, actual_num, turns):
    """Checks guess and returns updated turns."""
    if user_guess > actual_num:
        print("Too high")
        return turns - 1 
    elif user_guess < actual_num:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The number was {actual_num}")
        return turns

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_TURN
    else:
        return HARD_TURN

def game():
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("I'm thinking of a number between 1 to 100")
    chosen_num = randint(1, 100)   
    turns = set_difficulty()
    guess = None

    while guess != chosen_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, chosen_num, turns)

        if guess == chosen_num:
            break
        elif turns == 0:
            print("You've run out of guesses. You lose.")
            print(f"The correct number was {chosen_num}.")
            return
        else:
            print("Guess again.\n")

game()
