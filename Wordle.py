import random
import sys

def main():
    # Get a random word.
    class bcolors:
        WARNING = '\033[93m'
        ENDC = '\033[0m'
        cyan = "\u001b[36m"
    global tries
    tries = 0
    used_tries = 1
    start()
    yellow_letters = ''
    green_letters = '     '
    while tries > 0:
        attempt = input("Please input a 5 letter attempt: ")
        
# Ensures valid attempt length. Prepares alphabet key.
        if len(attempt) != 5:
            print("Invalid input length. Use 5 letters")
        else:
            letter_num = 0
            color = ' '
            alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            
# Tests attempt word with the answer. Lists correct "green" letters and semi correct "yellow" letters
            for letter in attempt:
                if letter.upper() == answer[letter_num]:
                    color = 'green'
                    if letter.upper() not in green_letters:
                        green_letters = green_letters[:letter_num] + letter.upper() + green_letters[letter_num + 1:]
                elif letter.upper() in answer:
                    color = 'yellow'
                    if letter.upper() not in yellow_letters:
                        yellow_letters = yellow_letters + letter.upper()
                elif letter.upper() not in answer:
                    color = 'red'
                    if letter.upper not in alphabet:
                        alphabet.remove(letter.upper())
                else:
                    print('Error')
                print(letter + ' - ' + color)
                letter_num += 1

# Dectecs if you have won. Prints how many tries are available. Shows correct "green" letters and semicorrect "yellow" letters
            if attempt.upper() == answer:
                if used_tries == 1:
                    print(' You Won! That took ' + str(used_tries) + ' guess.')
                else:
                    print(' You Won! That took ' + str(used_tries) + ' guesses.')
                replay()
                break
            else:
                tries -= 1
                used_tries += 1
                if tries == 1:
                    print(attempt.upper() + ' is not the correct answer! ' + str(tries) + ' try left')
                else:
                    print(attempt.upper() + ' is not the correct answer! ' + str(tries) + ' tries left')
                print(bcolors.WARNING + '[' + ', '.join(yellow_letters) + ']' + bcolors.ENDC + bcolors.cyan + '[' + ', '.join(green_letters) + ']' + bcolors.ENDC)
                print(alphabet)
#hah loser
    if tries == 0:
        print('You lose! The correct answer is ' + answer)
        replay()


# Resets the game. Called at 51 and 65.
def replay():
    p_again = input('Play again?\nYes or No: ')
    if p_again.lower() == 'yes':
        main()
    else:
        print('Good Bye!')

# Starts up the game with the difficulty rating. Gets random word. Called at 13.
def start():
    global answer
    answer = getRandomWord().upper()
    global tries
    user_input = input("Choose easy or hard mode: ")
    if user_input.lower() == 'easy':
        tries = 6
    elif user_input.lower() == 'hard':
        tries = 5
    elif user_input.lower() == 'dev':
        print(answer)
        tries = int(input('number of tries: '))
        



# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
