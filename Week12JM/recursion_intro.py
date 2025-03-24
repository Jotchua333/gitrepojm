'''
Another way of solving problems wherein a function calls itself
with a slight modification to parameters every time until a base case is
reached.

Iterative --> while(as long as a given condition is satisfied)
              for(as long as we go through all the elements in the sequence)

5 * 4 = 5 + (5 * 3)
      = 5 + 5 + (5 * 2)
      = 5 + 5 + 5 (5 * 1)
'''

def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b-1)

#print(mult_recur(5, 4))

'''
WRITE A RECURSIVE FUNCTION THAT CALCULATES A TO THE POWER OF B
'''

def power_recur(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power_recur(a, b-1)

#print(power_recur(2, 5))

'''
WRITE A RECURSIVE FUNCTION TO CALCULATE THE FACTORIAL OF A NUMBER
'''

def fact_recur(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact_recur(a-1)

#print(fact_recur(5))

'''
WRITE A RECURSIVE FUNCTION TO FIND THE SUM OF ALL NUMBERS IN A GIVEN LIST
'''

def list_recur(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_recur(num_list[1:])

nums = [1, 1, 1]
print(list_recur(nums))

'''
WRITE A RECURSIVE FUNCTION TO REVERSE THE ELEMENTS OF A LIST
'''
def reverse_recur(a):
    if len(a) == 1:
        return





















