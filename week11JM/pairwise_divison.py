'''
Write a function that takes 2 lists of equal length containing numbers.
Creates a new list of the same length containing the results of pairwise division of the parameter lists.
'''
def pairwise(numlist, denlist):
    """

    :param numlist: non-emply number list
    :param denlist: non-empty number list
    :return: new list with results of pairwise division
    """

    newlist = []
    try:
        assert len(numlist) > 0 and len(denlist) > 0, 'One or both of lists are empty'
        assert len(numlist) == len(denlist), 'Lists are of unequal lengths'
        for i in range(len(numlist)):
                newlist.append(numlist[i]/denlist[i])
    except AssertionError as e:
        print('AssertionError: ', e)
    except ZeroDivisionError as e:
        print('Cannot Divide by Zero: ', e)
    except TypeError  as e:
        print('Please Provide Only Numbers: ', e)
    except Exception as e:
        print('Something went wrong: ', e)

    return newlist


list1 = [2, 4, 6]
list2 = [1, 2, 3]
print(pairwise(list1, list2))


list1 = [2, 4, 6]
list2 = [1]
print(pairwise(list1, list2))

list1 = [2, 4, 6]
list2 = []
print(pairwise(list1, list2))

list1 = [2, 4, 6]
list2 = [1, 0, 3]
print(pairwise(list1, list2))

list1 = [2, 4, 'hi']
list2 = [1, 2, 3]
print(pairwise(list1, list2))




