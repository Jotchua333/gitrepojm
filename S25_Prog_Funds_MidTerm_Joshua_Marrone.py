import random



### Q1

#Defining coin toss function with variables for the random number that determines the computer's move.
def cointoss(user_choice):
    comp_move = random.randint(0,1)
    comp_choice = ''
    if comp_move < 0.5:
        comp_choice = 'heads'
    else:
        comp_choice = 'tails'
    #compares user move versus computer move, prints appropriate response (win/lose/tie)
    if user_choice == 'heads' and comp_choice == 'tails':
        print(f'You picked heads, Computer picked tails. You Win! ')
    elif user_choice == 'tails' and comp_choice == 'heads':
        print(f'You picked tails, Computer picked heads. You Lose! ')
    else:
        print('Tie! ')
#Asks user for input and uses it as a parameter to call the function.
choice = input('Pick heads or tails: ').lower()
cointoss(choice)



### Q2

#Defines function to calculate, categorize, and print users BMI based on input height and weight.
def bmi(h, w):
    #Calculates BMI
    total = (703*w)/(h*h)
    cat = ''
    #Categorizes BMI by checking against the upper limits of each category
    if total < 18.5:
        cat = '"Underweight"'
    elif total < 25:
        cat = '"Normal weight"'
    elif total < 30:
        cat = '"Overweight"'
    elif total < 40:
        cat = '"Obese"'
    else:
        cat = '"Severely Obese"'
    #Prints results
    print(f'Your BMI is {total} and you are in the {cat} category.')
#Asks user for height and weight, passes them as parameters to the function
height = int(input('Enter your height in inches: '))
weight = int(input('Enter your weight in pounds: '))
bmi(height, weight)



### Q3

#Defines function to go through each number from 1 to the target and print FizzBuzz if divisible by 5 and 3, Fizz if divisible by 3, Buzz if divisible by 5, and the number as a string if none of these conditions are met.
def fizzbuzz(target):
    #Loops through each number from 1 - target, checking the divisibility conditions, and printing the appropriate response
    for i in range(1, target+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz ')
        elif i % 3 == 0:
            print('Fizz ')
        elif i % 5 == 0:
            print('Buzz ')
        else:
            print(f'{i} ')
#Asks user for the target number and passes it as a parameter to the fizzbuzz function
number = int(input('Enter the target number: '))
fizzbuzz(number)



### Q4

#Defines function to create a list of even factors of a user-given number and print the result.
def evenfactors(num):
    factor_list = []
    #Loops each number from 1 - user number and checks if i is both a factor AND even, adding to the blank factor list if so.
    for i in range(1, num+1):
        if num%i == 0 and i%2 == 0:
            factor_list.append(i)
    #Prints resulting list of even factors
    print(f'Even factors of {num}: {factor_list}')
#Asks user for the given number and passes it as a parameter to the evenfactors function
number = int(input('Enter a number: '))
evenfactors(number)



### Q5

#Defines function to print a pattern of numbers based on the number of rows input by the user.
def rowprint(rows):
    #Added to each time a row is complete in order to start at the next number up
    startnum = 1
    #Loops first for each row, and loops again in each row to print each number until reaching the given number. Prints in descending pattern
    for i in range (rows, 0, -1):
        for j in range(startnum, rows+1):
            print(j, end=' ')
        startnum += 1
        #Creates new row
        print()
#Asks user for the number of rows and passes it as a parameter to the rowprint function.
rowcount = int(input('Enter number of rows: '))
rowprint(rowcount)

