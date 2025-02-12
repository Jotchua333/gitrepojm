### While Loops ###
'''
x = 1

while x <= 5:
    print(x)
    x+=1


while x <= 10:
    print(x)
    x+=1
'''
### RPS - Update with while (done) ###

### Break statement ###
'''
x=1

while x <= 10:
    if x ==5:
        break
    print(x)
    x+=1
'''
### Continue Statement ###
'''
x=0

while x <= 10:
    x+=1
    if x ==5:
        continue
        # skips remaining excecution :)
    print(x)
'''
### For Loop ###
'''
nums = [1,2,3,4,5]

for num in nums:
    print(f'{num} Mississippi')
'''
### Range(Uses Indexes) ###
'''
print('First 10 Index Numbers: ')
for i in range(10):
    print(i)
print('First 10 Natural Numbers: ')
for i in range(1,11):
    print(i)
print('Odds Only: ')
for i in range(1,11, 2):
    print(i)
'''

### Sum of the First 100 Natural Numbers ###
'''
sum = 0
for i in range(1,101):
    sum+=i

print(f'The Sum of the First 100 Natural Numbers: {sum}')
'''
### Return Multiplication Table for Given Number, up to 10. ###
'''
num = int(input('Enter a Number for a Multiplication Table: '))
for i in range(1,11):
    print(f'{num} * {i} = {num*i}')
'''
### Print Numbers Reversed ###
'''
print('20-10 in Descending Order: ')
for i in range (20, 9, -1):
    print(i)
'''
### NESTED LOOPS ###
'''
nums = [1, 2, 3, 4]

for n in nums:
    for letter in 'abc':
        print(n, letter)
'''
