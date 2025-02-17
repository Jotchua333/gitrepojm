### Write a function that checks if a number is even or not.
def is_even(num):
    #Checks if the number is even and returns true or false
    '''if num%2==0:
        """
        :param num: a positive integer
        :return: Print statement saying even or not
        """
        return True
    else:
        return False
    '''
    return num%2==0
#Prints the output of is_even
'''
number = int(input('Enter a number to check if it is even: '))
print(is_even(number))
'''

###Using functions in the middle of other code

###For a given range, print whether each number is even or odd

def print_even(start, end):
    """

    :param start: starting number in range
    :param end: ending number in range
    :return: list of numbers in range defined even or odd.
    """
    #Tracks each element of range and prints whether it is even or odd
    for i in range(start, end+1):
        if is_even(i):
            print( i, 'even')
        else:
            print( i, 'odd')

#Asks user for ranges and prints results from print_even
'''
starting = int(input('enter the lowest value in the range: '))
ending = int(input('enter the highest number in the range: '))
print_even(starting, ending)
'''

###Sum of all odd numbers in a given range

def sum_odd(start, end):
    """

    :param start: starting number in range
    :param end: ending number in range
    :return: total off odd numbers in range
    """
    #Adds any odds in range to a total and returns it
    total= 0
    for i in range(start, end + 1):
        if i%2 != 0:
            total = total+i
    return total
# Asks user for ranges and prints the return from sum_odd
'''
starting = int(input('enter the lowest value in the range: '))
ending = int(input('enter the highest number in the range: '))
total = sum_odd(starting, ending)
print(f'Total of all odd numbers is: {total}')
'''

def add(num1, num2):
    return num1+num2
def multiply(x, y):
    print(x*y)

add(1, 2)
print(add(1,2))
multiply(3,4)
print(multiply(3, 4))