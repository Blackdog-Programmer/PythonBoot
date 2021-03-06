# Hangman Game Site: https://t.ly/Flv3
import hangman_art
import hangman_word

import os
import sys
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    print(hangman_art.logo)

    chosen_word = random.choice(hangman_word.word_list)
    # print(chosen_word)

    finish = 0
    status = len(hangman_art.stages)-1

    mask = '_'
    masked_word = [mask] * len(chosen_word)
    user_letters = []
    while mask in masked_word:
        print(hangman_art.stages[status])

        if status == finish:
            sys.exit(f"Oops! the word was {chosen_word}. Try Again :)")

        letter = input('Guess a letter: ').lower()
        if len(letter) != 1 or not letter.isalpha():
            print(f'Please type a alphabet letter')
            continue
        elif letter in user_letters:
            print(f'Already chosen, please type other letter')
            continue
        elif letter in chosen_word:
            masked_word = []
            user_letters.append(letter)
            for chosen_letter in chosen_word:
                if chosen_letter in user_letters:
                    masked_word.append(chosen_letter)
                else:
                    masked_word.append(mask)
        else:
            user_letters.append(letter)
            status -= 1

        clear()
        print(''.join(masked_word))

    print('Congratulation You Win! :)')
