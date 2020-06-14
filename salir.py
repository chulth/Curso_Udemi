
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