import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """


    if len(word) == 0:
        return 0
# get word score function used for finding the total score by the end of the scrabble game

    assert type(word) == str, "does not match str"
    assert type(n) == int, "does not match int"
    assert n > 0, "must be greater or equal to 0"
    assert len(word) >= 0, "must be greater than 0"
    assert word.islower() == True, "word is lower case"

    score = 0

    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    if n == len(word):
        score = (score * len(word)) + 50 
    else:
        score = score * len(word)
    return score 






# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

def update_hand(hand, word):
    assert type(word) == str, "type does not match"
    assert type(hand) == dict, "type does not match"
    assert len(word) > 0, "length can not be zero"
    assert len(hand) > 0, "length can not be zero"

    updated_hand = hand.copy()

    for letter in word:
        updated_hand[letter] -= 1
        if updated_hand[letter] == 0:
            del updated_hand[letter] 
    assert type(hand) == dict, "type error"
    return updated_hand


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    """
    PsuedoCode: 
    for each letter in hand
    if letter in word is the same as letter in the word list
    returns true 
    or else returns false when letter does not match letter in word list
    """
    
    assert type(word) == str, "type does not match"
    assert type(hand) == dict, "type does not match"
    assert word.islower() == True, "word must be lowercase"

    hand_copy = hand.copy()

    for letter in word:
        if letter in hand_copy:
            # enough letters in the hand ?

            if hand_copy[letter] > 0:
                hand_copy[letter] -= 1
            else: # not enough letters
                del hand_copy[letter]
                return False
        else:
            return False


    if word in word_list:        
        return True
    else:
        return False



    # for letter in hand:
    #     if letter in word == letter in word_list:
    #         return True
    #     else: 
    #         return False 



def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    assert type(hand) == dict, "type does not match"
    return sum(hand.values())


def play_hand(hand, word_list, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while True:
    # Display the hand
      print("Current line: ", end='')
      display_hand(hand)
    # Ask user for input
      word_input = input("Enter word or enter full stop '.' to finish game: ")
    # If the input is a single period:
      if word_input == '.':
    # End the game (break out of the loop)
        print("Game finished, total score is : " + str(total_score) + ' points.')
        break
    # Otherwise (the input is not a single period):
      else:
    # If the word is not valid:
        if not is_valid_word(word_input, hand, word_list):
    # Reject invalid word (print a message followed by a blank line)
          print("Wrong input, enter again.")
          print()
          continue
    # Otherwise (the word is valid):
        else:

    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
          score = get_word_score(word_input, n)
          total_score += score
          print('"' + word_input + '"' + " earned " + str(score ) + " points. Total: " + str(total_score) + " points.")
    # Update the hand
        hand = update_hand(hand, word_input)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        if calculate_hand_len(hand) == 0:
            print("No letters left. Total score : " + str(total_score) + " points.")
            break


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
    
    2) When done playing the hand, repeat from step 1    
    """

    hand = {}
    while True:
        input_choice = input("Enter n to play a new game, r to play the last game again, or e to exit game: ")
        if input_choice == 'n':
            hand = deal_hand(HAND_SIZE)
            old_hand = hand.copy()
            play_hand(hand, word_list,HAND_SIZE)
        else: 
          if input_choice == 'r':
            if len(hand) == 0:
                print("Sorry. You have not played a hand before.")
                continue
            else:
                play_hand(old_hand, word_list, HAND_SIZE)
          else: 
            if input_choice == 'e': 
              print("End game.")
              break
            else:
               print("Input invalid.")


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
