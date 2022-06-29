from Hangman_ART import stages, logo
import random

# load_word(FILE_NAME) accepts a file name as a parameter and loads all the words from the .txt file
def load_word(FILE_NAME):
    print("Loading word list from file...")
    word_list = []
    with open(FILE_NAME) as file:
        for line in file:
            word_list.append(line.rstrip('\n'))
        num_words = len(word_list)
        print(f"{num_words} words loaded.")
        return word_list

# choose_word(word_list, already_used) accepts a list of all the words and a list of words that has already been used in a game
# and it will return a random word from the list of words that is not found in the "already_used" list.
def choose_word(word_list, already_used):
    chosen_word = random.choice(word_list)
    while chosen_word in already_used:
        chosen_word = random.choice(word_list)
    return chosen_word

# is_valid_level(user_input)
def is_valid_level(user_input):
    if user_input.lower() == "easy":
        return True
    elif user_input.lower() == "hard":
        return True
    else:
        return 

# game_finish(remaining_lives, user_guess, chosen_word) checks whether or not the game is already over by returning a boolean.
def game_finish(remaining_lives, user_guess, chosen_word):
    if remaining_lives == 0 or user_guess == chosen_word:
        return True
    else:
        return False

# play_game(chosen_word) starts the hangman game.
def play_game(chosen_word):
    lower_case_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guessed_letters = []
    guessed_words = []
    chosen_word_list = list(chosen_word)
    lives = len(stages) - 1
    display = '_' * len(chosen_word)
    display_list = list(display)
    while not game_finish(lives, display, chosen_word):
        print(stages[lives])
        for letter in display:
            print(letter, end = ' ')
        print()
        print()
        print("Available letters: ", end=' ')
        for letter in lower_case_alphabet:
            if not letter in guessed_letters:
                print(letter, end=' ')
        print()
        guess = input("Guess a letter/word: ")
        while not guess.isalpha() or guess.lower() in guessed_letters or guess.lower() in guessed_words:
            guess = input("Guess a letter/word: ")
            if not guess.isalpha():
                print("Invalid input. Please only input character in the alphabet or words that only contain the alphabet")
            elif guess.lower() in guessed_letters:
                print(f"You have tried '{guess}' before. Please input another letter or word.")
            elif guess.lower() in guessed_words:
                print(f"You have tried '{guess}' before. Please input another letter or word.")
        if len(guess) == 1:
            guessed_letters.append(guess)
            if not guess.lower() in chosen_word:
                print(f"\'{guess.lower()}\' is not in the word.")
                lives -= 1
            else:
                for i,element in enumerate(chosen_word_list):
                    if element == guess.lower():
                        display_list[i] = guess.lower()
                display = ''.join(display_list)
        else:
            guessed_words.append(guess.lower())
            if guess.lower() != chosen_word:
                lives -= 1
            else:
                display = chosen_word
        print()
        print()
    print(stages[lives])
    for letter in display:
        print(letter, end = ' ')
    print()
    print()
    if lives > 0:
        print("Congratulations! You won!")
    else:
        print(f"Game Over. The word was {chosen_word}")


# This is the main function
def main():    
    print(logo)   
    play_again = 'Y'
    used_words = []
    while play_again.upper() == 'Y':
        word_list = []
        level = ""
        while not is_valid_level(level.lower()):
            level = input("Which level do you want to play in? Input \"easy\" or \"hard\"\n")
            if not is_valid_level(level.lower()):
                print("Invalid input. Please input \"easy\" or \"hard\"")

        # This body of code loads the words into a list        
        if level.lower() == "easy":
            word_list = load_word(r"C:\Users\William\Documents\Clement\Python\Udemy\Projects\Hangman\easy_word_list.txt")
        else:
            word_list = load_word(r"C:\Users\William\Documents\Clement\Python\Udemy\Projects\Hangman\hard_word_list.txt")
    
        print()

        random_word = choose_word(word_list, used_words)
        used_words.append(random_word)
        play_game(random_word)
        play_again = ' '
        while play_again.upper() != "Y" and play_again.upper() != "N":
            play_again = input("Do you want to play again? Y/N: ")
            if play_again.upper() != "Y" and play_again.upper() != "N":
                print("Invalid input. Please input Y or N")
    print()
    print()
    print("Thank you for playing hangman!", end='\n\n')


if __name__ == '__main__':
    main()      
