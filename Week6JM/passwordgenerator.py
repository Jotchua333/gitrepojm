#Ask user to enter the number of letters, numbers, and characters in the password.
##Generate a random password by using the above combination.
#letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 #             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
 #             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
 #             'W', 'X', 'Y', 'Z']
#numberlist  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#charlist = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
letterlist = list('abcdefghijklmnopqrstuvwxyz')
numberlist = list('0123456789')
charlist = list('!#$%&()*+')

letters = int(input('How Many Letters?'))
numbers = int(input('How Many Digits?'))
chars = int(input('How Many Characters?'))

password_list = []

for i in range(1, letters+1):
    password_list.append(random.choice(letterlist))
for i in range(1, numbers+1):
    password_list.append(random.choice(numberlist))
for i in range(1, chars+1):
    password_list.append(random.choice(charlist))
print(f'Before Shuffle: {password_list}')
random.shuffle(password_list)
print(f'After Shuffle: {password_list}')

password = ''.join(password_list)
print('Your Password is: ', password)