import logging

def add(x, y):
    return x+y
def sub(x, y):
    return x-y


'''
5 levels:

INFO - used to confirm things are working as expected

DEBUG - used to get detailed info, typically when diagnosing a problem

WARNING - used to indicate why something unexpected happens or indication of future problems

ERROR - used to log a serious problem due to which the program may be unable to perform a function

CRITICAL - indicates a serious error which might crash the application

Default level - WARNING
'''
num1 = 10
num2 = 5
addres = add(num1, num2)
subres = sub(num1, num2)
logging.warning(f'Sum of {num1} and {num2} is {addres}')
logging.warning(f'Difference of {num1} and {num2} is {subres}')

#CHange logging level to debug
#WRite log to file
#Change format to include timestamp
logging.basicConfig(filename = 'logging_sample.log', level=logging.DEBUG, format = '%(asctime)s:%(levelname)s: %(message)s')

