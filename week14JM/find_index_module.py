'''
Write a function that returns the index of a given element from the given list.
'''
print("Importing find index module")
test_str = "test string"
print('Running find index module directly: ', __name__)
def find_index(search_list, target_elem):
    for idx, val in enumerate(search_list):
        #print(idx, val)
        if val == target_elem:
            return idx
    return -1


#sample = ['apple', 'banana', 'orange', 'kiwi']
#print(find_index(sample, 'orange'))











