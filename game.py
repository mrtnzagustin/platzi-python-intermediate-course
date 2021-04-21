import random
from functools import reduce
import os

# Clear the screen
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

# Obtains a random word from the file words.txt
def get_random_word():
    # Open file of words an create a list 
    with open("files/words.txt", "r", encoding="utf-8") as file:
        words = [word.replace("\n", "") for word in file]
    return words[random.randint(0, len(words))]

# Indetifies if the letter dictionary param is already matched by user
# and returns the letter or a '_'
def show_matches(letter_dict):
    if letter_dict['matched']:
        return letter_dict['letter']
    else:
        return '_'

# Reveals partially the generated word
def show_word_dict(word_list_dict):
    screen_clear()
    print("Guess the word!")
    word_with_matches = list(map(show_matches, word_list_dict))
    print("".join(word_with_matches))

# Shows the win message
def win(word):
    screen_clear()
    print("You win, the word was", word.upper())

# Runs the game
def run():
    # Obtains a random word
    word = get_random_word()
    # Creates a list with "letter dictionaries"
    word_list_dict= [ { "letter": word[i], "matched": False } for i in range(0, len(word)) ]
    # Number of characters that remains to match
    characters_remain_to_match = len(word)

    # While the user dont enter all the letters for the word, keep asking
    while characters_remain_to_match > 0:
        # Shows the word (partially)
        show_word_dict(word_list_dict)
        try:
            # Ask for a new letter
            character = input("Ingress a character: ")
            # Check if the letter is an alpha or throw an asertion error
            assert character.isalpha(), "You must digit a alpha character"
            
            # Loop in all letters and check if the character matches some of the remain letters
            for i in range(0, len(word_list_dict)):
                if not word_list_dict[i]['matched'] and word_list_dict[i]['letter'] == character:
                    word_list_dict[i]['matched'] = True # marks the letter as matched
                    characters_remain_to_match -= 1 # decrease the number of characters remained to match the full word
        except AssertionError as assertion_error:
            print("Error:", assertion_error.__str__()) # prints the error
    win(word) # Finally, shows the win message


if __name__ == '__main__':
    run()