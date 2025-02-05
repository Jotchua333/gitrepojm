import random
rand_num = round(random.random(), 2)



rock = '''   
            _______
        ---/   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
'''
paper = '''
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
move = input('Pick your Move: (Rock/Paper/Scissors)').lower()

if rand_num < 1/3:
    comp_move = 'rock'
    print(rock)
elif rand_num < 2/3:
    comp_move = 'paper'
    print(paper)
else:
    comp_move = 'scissors'
    print(scissors)



if move == comp_move:
    result = 'Tie!'
elif move == 'rock':
    if comp_move == 'paper':
        result = 'You Lose!'
    elif comp_move == 'scissors':
        result = 'You Win!'
elif move == 'paper':
    if comp_move == 'rock':
        result = 'You Win!'
    elif comp_move == 'scissors':
        result = 'You Lose!'
elif move == 'scissors':
    if comp_move == 'rock':
        result = 'You Lose!'
    elif comp_move == 'paper':
        result = 'You Win!'
else:
    print('Invalid Move. Try Again!')

print(f'You picked {move.capitalize()}. Computer picked {comp_move.capitalize()}. {result.capitalize()}')


