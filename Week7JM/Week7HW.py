### Q1: Check if a string is a palindrome or not

#Returns true if the string is equal to the reverse of itself.
def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
'''
string = input('Enter the String You Would Like to Check: ').lower()
print(f'Is Palindrome: {palindrome(string)}')
'''

###Q2: Check if a string is an anagram of another.
def anagram(str1, str2):
    is_anagram = True
    #Checks that strings are the same length
    if len(str1) != len(str2):
        return False
    #Skips if the current index letter is present in the second string, and sets is_anagram to false before breaking if not.
    for i in str1:
        if i in str2:
            continue
        else:
            is_anagram = False
            break
    return is_anagram
'''
string1 = input('Input the first string: ').lower()
string2 = input('Input the second string: ').lower()
print(f'Anagrams: {anagram(string1, string2)}')
'''

### Q3: Write a function to that takes username, birth year, budget, price of the product as
#inputs and performs the following operations.
#a. Calculates the current age based on the birth year
#b. Calculates the number of products that can be bought based on budget and price
#per product. Round down the number of products.
#. Displays the message as shown in sample output
def operations(username, birthyear, budget, price):
    age = 2025-birthyear
    numprod = (budget/price)
    finalprod = (f'Hello {username}, you are {age} years old and can buy {numprod} products!')
    return finalprod
'''
user = input('Enter Username: ')
birth = int(input('Enter Birth Year: '))
budg = int(input('Enter Budget: '))
prod_price = int(input('Enter Price of Product: '))

print(operations(user, birth, budg, prod_price))
'''

### Q4: Write a program to check whether we can create a triangle or not
'''
f any of the three lengths is greater than the sum of the other two, then you cannot form a
triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is
called a "degenerate" triangle.)
Write a function named is_triangle that takes three integers as arguments, and that prints
either "Yes" or "No," depending on whether you can or cannot form a triangle with the
given lengths
'''

def is_triangle(num1, num2, num3):
    if num1 > num2+num3:
        print('No')
        return
    elif num2 > num1+num3:
        print('No')
        return
    elif num3 > num1 + num2:
        print('No')
        return
    elif num1 == num2+num3:
        print('Degenerate Triangle')
        return
    elif num2 == num1+num3:
        print('Degenerate Triangle')
        return
    elif num3 == num1+num2:
        print('Degenerate Triangle')
        return
    else:
        print('Yes')
        return
'''
number1 = int(input('Enter the first side length: '))
number2 = int(input('Enter the second side length: '))
number3 = int(input('Enter the third side length: '))
is_triangle(number1, number2, number3)
'''

### Q5:
def triangle(num):
    trisum = 0
    for i in range(1, num+1):
        trisum +=i
        if trisum == num:
            return True
    return False

number = int(input('Enter the Number: '))
print(f'Is Triangular: {triangle(number)}')





















