### Q1
'''
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second numberL '))

mult_nums = lambda x, y: x*y
print(mult_nums(num1, num2))
'''
### Q2
'''
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print((lambda a,b: a-b)(num1, num2))
'''

### Q3
'''
list1 = [1, 3, 6, 4, 8]

newlist = filter(lambda x: x>5, list1)
print(list(newlist))
'''

### Q4
'''
num = int(input('Enter NUmber: '))
newnum = lambda x: x/5 if x>10 else x+5
print(newnum(num))
'''

### Q5
'''
nums = [3, 2, 6, 8, 4, 6, 2, 9]
names = ["Jane", "Lee", "Will", "Brie"]
#A
newnumlist = list(map(lambda x: x*2, nums))
print(newnumlist)
#B
newstrlist = list(map(lambda x: 'Hello' + x, names))
print(newstrlist)
'''

### Q6
'''
nums = [3, 2, 6, 8, 4, 6, 2, 9]
from functools import reduce
part1 = list(filter(lambda x: x%2 != 0, nums))
part2 = list(map(lambda x: x*x, part1))
part3 = reduce(lambda a, b: a+b, part2)
print(part3)
'''

### Q7
'''
nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(lambda x: x%2 == 0, nums))
odds = list(filter(lambda a: a%2 != 0, nums))
print(f'Count of evens: {len(evens)}')
print(f'Count of odds: {len(odds)}')
'''