import random
from words import alpha_words
import hangmanart as hm
stages = hm.hangman_stages()
play_again = 'yes'

while play_again in ['yes', 'y']:
    chosen_word = random.choice(alpha_words).lower()
    print(hm.logo)
    #print(chosen_word)
    word_display = []

    for _ in range(len(chosen_word)):
        word_display += '_'
    print(word_display)

    game_over = False
    lives = 7
    wrong = []

    while not game_over:
        guess = input('Guess a letter: ').lower()

        if guess in word_display or guess in wrong:
            print('You Already Guessed That! Try Again!')
            print(f'Lives Left: {lives}')
        elif guess not in chosen_word:
            lives = lives - 1
            wrong.append(guess)
            print(f'{guess.upper()} is Not in the Word! ')
            if lives == 0:
                print('Out of Lives! Game Over!')
                game_over = True
            else:
                print(f'{lives} Lives Left')
        else:
            for idx, val in enumerate(chosen_word):
                if val == guess:
                    word_display[idx] = guess.upper()
                    print(f'{guess.upper()} is in the Word! ')
        print(f'{' '.join(word_display)}')

        if '_' not in word_display:
            print('Game Over! You Win! ')
            game_over = True

        print(stages[lives])

    print(f'The Chosen Word Was: {chosen_word.upper()}')
    play_again = input('Want to Play Again? (y or n): ')
print('Thank You for Playing! ')








