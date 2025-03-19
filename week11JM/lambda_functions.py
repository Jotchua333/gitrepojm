"""
def calc(op, x, y):
    return op(x, y)

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b












#add being used like a variable
res = calc(add, 3, 4)
print(res)

res = calc(subtract, 3, 4)
print(res)

res = calc(multiply, 3, 4)
print(res)

res = calc(divide, 3, 4)
print(res)

"""

### LAMBDA FUNCTIONS ###
def square(a):
    return a*a
#print(square(5))

square_ope = lambda a: a*a #Lambdas ae also called anonymous functions
#print(square_ope(5))

'''
Write a Lambda function to check if a number even or not
Returns "Even Number" if even; "Odd Number" if odd
'''
even_check = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"

hello = lambda x: f"Hello {x}"
#print(hello('London'))

### IIFEs --> Immediately Invoked Function Expressions
#Used when we dont want to re use the lambda function
#So the lambda expression is not assigned to a variable

#print((lambda x: f"Hello {x}")('London'))
#print((lambda x: x*2)(2))

### HIGHER ORDER FUNCTIONS ###
#EX: filter(), map(), reduce()

'''
Write a function that prints even numbers from a given list
'''
#FILTER FUNCTION

def is_even(n):
    return n%2 == 0
num_list = [3, 2, 6, 8, 4, 6, 2, 9]
even_nums = filter(is_even, num_list)
#print(even_nums) #Returns filter object
#print(list(even_nums))

evennums = filter(lambda n: n%2 == 0, num_list)
#print(list(evennums))

#MAP FUNCTION
#apply a function to every element in the iterable(list, etc.)

doubles = list(map(lambda n: n*2, num_list))
#print(doubles)

strings = ['Canada', 'Spain', 'Mexico']
string_lengths = list(map(lambda x: len(x), strings))
#print(string_lengths)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

add_nums = list(map(lambda x,y: x+y, nums1, nums2))
#print(add_nums)

#REDUCE FUNCTION
#Reduce all numbers to a single value based on the same logic

nums = [3, 8, 10, 4, 11, 9]
sum = 0
for n in nums:
    sum = sum + n
#print('Sum: ', sum)

from functools import reduce
total_sum = reduce(lambda a, b: a+b, nums)
print(total_sum)

###





















