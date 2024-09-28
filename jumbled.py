import random
from initialize import *
from shuffle import *

def play(original_word):

    print("")
    
    length =  len(original_word)

    print(f"\nThe jumbled word for you is \t{shuffle(original_word).upper()}")

    attempt = 0

    word_length = len(original_word)

    max_attempt = word_length-3 if word_length> 4 else word_length-1

    print(f"You have {max_attempt} attempts to solve this.")

    while attempt < max_attempt:

        error = 0
        remaining_attempt = max_attempt - attempt

        print(f"-" * word_length)
        guess = input(f"\nEnter your guess? 🤞 \n").strip().lower()

        if len(guess) == word_length:

            for i in range(length):
                print(f"{guess[i].upper()}\t", end="")
            print()

            for i in range(length):
                if guess[i] == original_word[i]:
                    print("🔼\t", end="")
                else:
                    print("🔺\t",end="")
                    error+= 1
            if error == 0:
                print(f"\n You won. 🏆🏆🏆  The orginal word was {original_word}")
                if remaining_attempt >= max_attempt/2:
                    print("You got  {}".format("🌟"*3))
                else:
                    print("You got {}".format("🌟"*1))
                restart()
                break      
            print()

        elif len(guess) < word_length:
            missing = word_length - len(guess)
            print(f"you entered {missing} letters less.")
        
        else:
            more = len(guess) - word_length
            print(f"you entered {more} letters more.")

        attempt+= 1
        remaining_attempt = max_attempt - attempt
        if remaining_attempt == 0:
            print("\nNo attempts remaining now...")
        else:
            print(f"\nonly {remaining_attempt} attempts remaining now....")
        
    print(f"\nYou lost. The orginal word was {original_word}")
    restart()
      
def restart():
    response = input("\nDo you wanna play again?\n"
                     "\nwrite No to quit. To play Just press ENTER  ").lower().strip()
    if response:
        if response == "no":
            print("You played well. You can play any time again...Bye")
            quit()
        else:
            initialize()


initialize()

