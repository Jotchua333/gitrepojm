'''
QUICK SORT
-3 way partition by using median as pivot (Dutch Flag Approach)
'''

import statistics
nums= [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 44, 28]

def quicksort(nums_list):
    #Base Case
    if len(nums_list) <= 1:
        return nums_list
    else:
        #Finds Median
        median_value = statistics.median(
            [
                nums_list[0],
                nums_list[len(nums_list) // 2],
                nums_list[-1]
            ]
        )
        #Creates lists
        left_list = []
        mid_list = []
        right_list = []
        #Assigns values to lists
        for i in nums_list:
            if i < median_value:
                left_list.append(i)
            elif i == median_value:
                mid_list.append(i)
            else:
                right_list.append(i)
        #Breaks down to next layer, until returning all single values in order.
        return quicksort(left_list) + mid_list + quicksort(right_list)

print(quicksort(nums))

