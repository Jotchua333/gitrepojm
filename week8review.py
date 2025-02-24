def multi5(numlist):
    for i in numlist:
        if i > 150:
            continue
        elif i > 500:
            break
        elif i % 5 == 0:
            print(f'{i} ')
        else:
            break



def printrows(numrows):
    for i in range(1, numrows+1, 2):
        print(f'{i}     ')

def factors(num):

    for i in range(1, num+1):
        factor_list = []
        for j in range(1, i):
            if i%j == 0:
                factor_list.append()
        print(f'Factors of {i}: {factor_list}')

factors(6)