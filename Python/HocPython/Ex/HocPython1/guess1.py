import random

def guess_number_input(valid_numbers):
    guess_number_raw = input("Guess the number: ")
    if guess_number_raw.isnumeric():
        guess_number = int(guess_number_raw)
        if guess_number in valid_numbers:
            return guess_number
        else:
            print("your guess number isn't in valid numbers, please try again!")
            return -1
    else:
        print("wrong number, please try again!")
        return -1

def main(args):
    liem=mki

def guess_game():
    valid_numbers = [_ for _ in range(0, 11)]
    number_game_master = random.choice(valid_numbers)
    guess_number_player = guess_number_input(valid_numbers)
    if guess_number_player == -1:
        print("retry guess the number")
    elif number_game_master == guess_number_player:
        print(f"Hurray!!! You guessed the number right, it's {guess_number_player}")
    else:
        print(f"Your guess number is incorrect, the number is {number_game_master}")


if __name__ == "main":
    guess_game()

