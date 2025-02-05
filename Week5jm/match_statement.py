'''
num = int(input('Enter a number: '))
num_list = [11,12]
match num:
    case 11 if num %2 ==0:
        print(f'num is {num}')
    case 11:
        print('Num is 11')
    case 20:
        print('Num is 20')
    case 1 | 2| 3:
        print('Num is either 1 2 or 3')
    case[11,12]:
        print(f'List of Numbers: {num_list}')
    case _:
        print('Num is neither 10 nor 20')

'''
grade = int(input('Enter Grade: '))

if grade <60:
    print('F')
else:
    match grade:
        case 60 | 61 | 62 | 63:
            print('D-')
        case 64 | 65| 66:
            print('D')
        case 67| 68 | 69:
            print('D+')
        case 70 | 71 | 72 | 73:
            print('C-')
        case 74 | 75 | 76:
            print('C')
        case 77 | 78 | 79:
            print('C+')
        case 80 | 81 | 82 | 83:
            print('B-')
        case 84 | 85 | 86:
            print('B')
        case 87 | 88 | 89:
            print('B+')
        case 90 | 91 | 92 | 93:
            print('A-')
        case 94 | 95 | 96:
            print('A')
        case 97 | 98 |99:
            print('A+')

if grade < 60:
    print('F')
elif grade < 64:
    print('D-')
elif grade < 67:
    print('D')
elif grade < 70:
    print('D+')
elif grade < 74:
    print('C-')
elif grade < 77:
    print('C')
elif grade < 80:
    print('C+')
elif grade < 84:
    print('B-')
elif grade < 87:
    print('B')
elif grade < 90:
    print('B+')
elif grade < 94:
    print('A-')
elif grade < 97:
    print('A')
else:
    print('A+')
