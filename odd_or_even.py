number= input('please enter a number: ')

try:
    number = int(number)
    
    if number % 4 == 0 :
        print('es mútliplo de 4')

    elif number % 2 == 0 :
     print('is even')

    else:
        print('impar')
    
except:
    print('seriedad por favor')
