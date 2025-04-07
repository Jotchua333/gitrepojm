'''
modules - pre-written code files that can be reused in any other program

standard
external
    need to be installed first before importing
custom-built
    developed by the programmers for specific use cases; not shared by public
'''
import random
#standard module already part of the language

#import pandas
#pandas is an external library used for data analysis
#pip install pandas

#Importing entire module with an alias:

#import find_index_module as fim
#sample = ['apple', 'banana', 'orange', 'kiwi']
#req_idx = fim.find_index(sample, 'kiwi')
#print(req_idx)

#Import pandas as pd (USE ALIASES)

#Importing specific functions/var from module:

from find_index_module import find_index

sample = ['apple', 'banana', 'orange', 'kiwi']
req_idx = find_index(sample, 'kiwi')
print(req_idx)

print('Running modules intro: ', __name__)