num = int(input('Enter a Number from 1-9: '))
word_dict={0: 'Zero', 1: 'One', 2: 'Two',
           3: 'Three', 4: 'Four', 5: 'Five',
           6: 'Six', 7: 'Seven', 8: 'Eight',
           9: 'Nine'}
word_list=['zero','one','two','three','four','five','six','seven','eight','nine']

#Using if-else:
if num == 0:
    print('Zero')
elif num == 1:
    print('One')
elif num ==2:
    print('Two')
elif num == 3:
    print('Three')
elif num == 4:
    print('Four')
elif num == 5:
    print('Five')
elif num == 6:
    print('Six')
elif num == 7:
    print('Seven')
elif num == 8:
    print("Eight")
elif num == 9:
    print('Nine')
else:
    print('Invalid Number. Try Again.')

#Using match-case:

match num:
    case 0:
        print('Zero')
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case 4:
        print('Four')
    case 5:
        print('Five')
    case 6:
        print('Six')
    case 7:
        print('Seven')
    case 8:
        print('Eight')
    case 9:
        print('Nine')


