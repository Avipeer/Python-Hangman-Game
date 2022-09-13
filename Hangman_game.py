from logging import exception


MAX_TRIES = 6


def print_hangman(num_of_tries):

    HANGMAN_PHOTOS = {}

    HANGMAN_PHOTOS[0] = """
    x-------x





    """
    HANGMAN_PHOTOS[1] = """
    x-------x
    |
    |
    |
    |
    |________
    """
    HANGMAN_PHOTOS[2] = """
    x-------x
    |       |
    |       0
    |
    |
    |________
    """
    HANGMAN_PHOTOS[3] = """
    x-------x
    |       |
    |       0
    |       |
    |
    |________
    """
    HANGMAN_PHOTOS[4] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |________
    """
    HANGMAN_PHOTOS[5] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |________
    """
    HANGMAN_PHOTOS[6] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |________
    """
    return  print(HANGMAN_PHOTOS[num_of_tries])
    

def game_title():#this function prints the game title
    print("""Welcome to the game Hangman! 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
   |_|  |_|\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/
""")
    return


def check_win(secret_word, old_letters_guessed):#Veturns true if the player guess all the letters
    final_word = show_hidden_word(secret_word, old_letters_guessed)
    return not "_" in final_word


def show_hidden_word(secret_word, old_letters_guessed):#Vreturn string with correct letters and underlines
    """
    checks if all the letters that the players guessed(stored in old_letters_guessed) are in the secret word
    """
    correct_guess_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            #correct_guess_word.append(letter)
            correct_guess_word = correct_guess_word + letter
        else:
            #correct_guess_word.append("_")
            correct_guess_word = correct_guess_word + " _ "
    return correct_guess_word


def check_valid_input(letter_guessed):#returns true if the input is correct
    
    only_eng_letters = letter_guessed.isalpha()
    #checks if the input has more than 1 letter and has charchters other than alphabet letters
    if len(letter_guessed) > 1 or not only_eng_letters:
        print("Illegal input! only single english letters are accepted!")
        return False

    else:
        return True


def try_update_letter_guessed(old_letters_guessed, secret_word ):#returns "true" if input is valid, otherwise it prints X and 
    while True: #ask from the user input until a correct input is entered
        user_letter_input = input("Please enter a single english letter:")
        if check_valid_input(user_letter_input):#makes sure the user typed a single english letter
            letter_guessed_lower_case = user_letter_input.lower()
            if letter_guessed_lower_case in old_letters_guessed:#ensures the user types a letter he hasnt entered yet
                print("you already guessed that letter, please choose another") 
                continue

            break

    #the following statement: if the letter
    if  letter_guessed_lower_case in secret_word: 
        old_letters_guessed.append(letter_guessed_lower_case)
        print("Correct!")
        return True

    else:
        old_letters_guessed.append(letter_guessed_lower_case)
        print("Incorrect guess!try again!\nX\n"," -> ".join(old_letters_guessed))
        return False
   

def choose_word(file_path, index):#picks a word placed in index - 1 from the file in the file path 

    with open(file_path, "r") as hangman_words_file:
        hangman_words_list = hangman_words_file.readline().split(" ")#converts the string to a list of words
    amount_of_words_in_file = len(hangman_words_list)
    corrected_chosen_index = (index - 1) % amount_of_words_in_file
    amount_of_unique_words = len(set(hangman_words_list))
    return (hangman_words_list[corrected_chosen_index] )


def main():
    
    """
    1)print the game title 
    2)ask the player for the text file path and index 
    3)print the first hangman pic with the empty lines underneath 
    4)ask for letter input, if the input is wrong print X and the letters guessed so far, sorted, and ask for another input
    5)print the correct letters to the lines or a new hangman state with "incorrect guess"
    6)if the player guess correctly print WIN, if the player reaches 6 wrong attempts print "lose"
    """
     
    old_letters_guessed =[]
    num_of_tries = 0
    game_title()
    game_words_file_path = (input("Please enter a file path that contains a text file with words:[press enter to confirm]:"))
    word_index = int(input("Please enter any number bigger than 0 [press enter to confirm]:"))
    secret_word = choose_word(game_words_file_path, word_index)
    
    while num_of_tries <= MAX_TRIES:  
        if check_win(secret_word, old_letters_guessed):
            print("You win! the secret word is:", secret_word)
            break

        print_hangman(num_of_tries)
        print(" " * 3 + show_hidden_word(secret_word, old_letters_guessed) + "\n")
        if try_update_letter_guessed(old_letters_guessed, secret_word):
            continue

        num_of_tries += 1 
    if num_of_tries > MAX_TRIES:
        print("you lost! the secret word was:", secret_word)

if __name__ == "__main__":
    main()
