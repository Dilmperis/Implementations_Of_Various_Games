# Dependencies
import random

# Print statements
print('Welcome to the Number Guessing Game')
print("I'm thinking of a number between 1 and 100. Guess it.\n")

# Spelling check of input
def check_spelling(word, correct_word_list):
    while word not in correct_word_list:
        word = input(f'Wrong spelling. Type one of {correct_word_list}: ').lower()
    return word

# Difficulty
difficulty = input('Choose a level of difficulty.\n"Easy" or "Hard"?: ').lower()
correct_difficulty_list = ['easy', 'hard']
difficulty = check_spelling(difficulty, correct_difficulty_list)

# Attempts according to difficulty
def attempt_number(difficulty):
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10

    return attempts

attempts = attempt_number(difficulty)

# Playing Loop
number_to_guess = random.randint(1,100)
win_flag = False

# Get valid guess (a number and not a word, and the number in [1,100])
def valid_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))

            while guess<1 or guess>100:
                guess = int(input("Make a guess between 1 and 100: "))
            return guess
        except ValueError:
            print('Invalid guess. Please type a number!')

def game_play(attempts, number_to_guess, win_flag):
    print(f"\nYou have {attempts} attempts to guess the number")
    guess = valid_guess()

    if guess == number_to_guess:
        print(f'Congrats! You guessed correctly the number {number_to_guess}')
        win_flag = True
    else:
        if guess > number_to_guess:
            print("Too high")
        elif guess < number_to_guess:
            print("Too low")
        attempts -=1
        print("Guess again")
        win_flag = False

    return attempts, win_flag

while (attempts > 0) and (win_flag == False):
    attempts, win_flag = game_play(attempts, number_to_guess, win_flag)

def result_of_game(attempts, win_flag):
    if (attempts>0) and (win_flag == True):
        print('\nEnd of the game. You are a winner')
        print("-----------------------------------\n")
    else:
        print(f'\nEnd of the game. Unfortunately you lost... The number to guess was {number_to_guess}')
        print("-----------------------------------\n")

result_of_game(attempts, win_flag)

# Keep playing?
def want_to_play_again():
    keep_playing = input("Do you want to play again? Yes or No? ").lower()
    correct_keep_playing_list = ['yes', 'no']
    keep_playing = check_spelling(keep_playing, correct_keep_playing_list)
    return keep_playing

keep_playing = want_to_play_again()

while keep_playing == "yes":
    difficulty = input('\nOk, we will start again. Choose a level of difficulty.\n"Easy" or "Hard"?: ').lower()
    difficulty = check_spelling(difficulty, correct_difficulty_list)
    attempts = attempt_number(difficulty)
    number_to_guess = random.randint(1,100)
    win_flag = False

    while (attempts > 0) and (win_flag == False):
        attempts, win_flag = game_play(attempts, number_to_guess, win_flag)

    result_of_game(attempts, win_flag)
    keep_playing = want_to_play_again()

if keep_playing == "no":
    print('\nIt was nice to play with you! Goodbye')


