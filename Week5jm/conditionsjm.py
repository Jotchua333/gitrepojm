'''
height = int(input('Enter your height in cms: '))

if height > 120:
    print('Eligible to Ride')
else:
    print('Not eligible to ride')
'''
#2
'''
height = int(input('Enter your height in cms: '))

if height > 120:
    print('Eligible to Ride')
    age = int(input('Enter Your Age: '))
    if age <=18:
        print('Please pay $7')
    else: print('Please pay $12')

else:
    print('Not eligible to ride')
'''
#3 rollercoaster ride with nested if-else with elif.
'''
height = int(input('Enter your height in cms: '))
total_bill = 0
if height > 120:
    age = int(input('Enter your age: '))
    if age < 12:
        total_bill += 5
    elif age <= 18:
        total_bill += 7
    else:
        total_bill += 12

    photo = input('Would you like a photo? (Yes/No)')
    if photo == 'Yes':
        total_bill += 3

    print(f'Your total bill is ${total_bill}')
else:
    print("You are not eligible to ride.")
'''

height = int(input('Enter your height in cms: '))
total_bill = 0
if height > 120:
    age = int(input('Enter your age: '))
    if age < 12:
        total_bill += 5
    elif age <= 18:
        total_bill += 7
    elif age >= 45 and age<=55:
        total_bill +=0
    else:
        total_bill += 12

    photo = input('Would you like a photo? (Yes/No)')
    if photo == 'Yes':
        total_bill += 3

    print(f'Your total bill is ${total_bill}')
else:
    print("You are not eligible to ride.")
