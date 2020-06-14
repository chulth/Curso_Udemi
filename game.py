
from random import randint

cont =('y')
exit = ('n')

while cont != exit:
    num = randint(1,3)
    guees = 0
    while num != guees  :
        print('enter a number between 1 to 3 ')
        guees = int(input())
        print('good luck')
    exit=input('do you want exit')
print('end of game')
















'''



num = 0

    guess= 0
    while num !=guess:
        print('guees a number between 1 to 3')
        guess= int(input())
    print('good you are lucky')


    exit = input('Do you want playing? : (y/n)')
print('finish the game')


 num = randint(1,3)
    guess= 0
    while num !=guess:
        print('guees a number between 1 to 3')
        guess= int(input())
    print('good you are lucky')
    print(response)
'''