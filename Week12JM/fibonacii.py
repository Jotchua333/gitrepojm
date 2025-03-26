'''
WRITE A RECURSIVE FUNCTION TO GET A PARTICULAR FIBONACCI NUMBER
'''

def fib(fib_num):
    print('Calling Fib. . . ')
    if fib_num == 1:
        return 0
    elif fib_num == 2:
        return 1
    else:
        return fib(fib_num-1) + fib(fib_num-2)

print(fib(15))


















