### Q1: Ask the user to enter number of rows and create pattern as shown
'''
Ex: User enters 5
Output:
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
'''
'''
rows = int(input('Enter Number of Rows: '))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
'''
### Q2: Ask the user to enter number of rows and create pattern like below
'''
User Enters 4:
*
*   *
*   *   *
*   *   *   *
'''
'''
rows = int(input('Enter Number of Rows: '))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()
'''
###EXTRA CREDIT:
'''
rows = int(input('Enter Number of Rows: '))
for i in range(rows, 0,-1):
    for j in range(i, 0,-1):
        print(j, end=' ')
    print()
'''
### Q3: Write a program to print a list of all even numbers till a given target number
'''
target = int(input('Enter target Number'))
evenlist = []
for i in range(0, target+2, 2):
    evenlist.append(i)
print(evenlist)
'''
###Q4: Write a program to print a list of all prime numbers till a given target number
'''
target = int(input('Enter Target Number: '))
primelist = []
for i in range(2, target+1):
    notprime = 0
    for j in range(2,i+1):
        if (i%j == 0) and (i != j):
            notprime = 1
    if notprime == 0:
        primelist.append(i)
print(primelist)
'''
### Q5: Find the highest number from a given list of numbers using for loop. Do not use any in-built functions
'''
numlist = []
highest = 0
length = int(input("How long is your number list?"))
for i in range(length):
    new = int(input('Add a number to your list: '))
    numlist.append(new)
for j in range(0, length):
    if numlist[j] > highest:
        highest = numlist[j]
print(f'The Highest number On Your List Was: {highest}')
'''
























