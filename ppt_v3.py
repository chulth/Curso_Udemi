
from random import choice
#definir las variables
player = 0
comp = 0
win=0
ngame = 3

while win != ngame:
    r = ('Rock')
    p = ('Paper')
    s = ('Scirssors')
    gamer =[r,p,s]

    print('Escoje una opcion {} {} {} y juega contra la computadora'.format(r,p,s))
    p1= input()
    c1 = choice(gamer)

    if p1==c1:
        print('Drawn')
        

    elif (p1 == r) and (c1 == s):
        print('player wins')
        win+=1
        player +=1

    elif (p1 == p) and (c1 == r):
        print('player wins')
        win+=1
        player +=1

    elif (p1 == s) and (c1 == p):
        print('player wins')
        win+=1
        player +=1
    else:
        print('computer win')
        win+=1
        comp +=1

if comp > player:
    print('your is pussy the pc won.jojojo')
else:
    print('you have lucky, you wins')