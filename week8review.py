import random


def multi5(numlist):
    for i in numlist:
        if i > 150:
            continue
        elif i > 500:
            break
        elif i % 5 == 0:
            print(f'{i} ')
        else:
            break


### Q2
def printrows(numrows):
    for i in range(1, numrows+1, 2):
        print(f'{i}     ')


### Q3
def factors(num):

    for i in range(1, num+1):
        factor_list = []
        for j in range(1, i+1):
            if i%j == 0:
                factor_list.append(j)
        print(f'Factors of {i}: {factor_list}')

factors(6)

### Q4
def repeatodd(num):
    x=1
    while(x<= num):
        print(x)
        x += 2
repeatodd(15)



### Q5 - temp list so changing indexes won't affect function
def rem_list_elem(given_list):
    temp_list = given_list.copy()
    for elem in given_list:
        print(elem)
        if elem == 'apple':
            temp_list.remove(elem)

    print(temp_list)

list= ['hi', 'apple', 'hello', 'abble', 'apple', 'apple']
rem_list_elem(list)




### Q6 - can be done with while loop as well

def guessinggame():
    number = random.randint(1, 100)
    user_num = 0
    for i in range(7):
        user_num = int(input('Guess the Number between 1 and 100: '))
        if user_num == number:

            break
        elif user_num < number:
            print('Too low, guess again: ')
        else:
            print('Too high, guess again: ')
    if user_num == number:
        print('You guessed the number correctly, you win! ')
    else:
        print('Too many guesses, you lose! ')

guessinggame()


### Q7

def list_dictionary(list):
    dict = {}
    for elem in list:
        dict[elem] = dict.get(elem, 0) + 1
    print(dict)

list_dictionary(['hello', 'hi', 'hello', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat', 'cat'])




























### Q11
def print_to6():
    count= 0
    while True:
        num = random.randint(1, 10)
        count += 1
        if num == 6:
            break
        else:
            continue
    print(f'Number of Iterations: {count}')
print_to6()