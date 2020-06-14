#this is a game wich  ask a number for guees a player
# question whats modules needs
#need random number
from random import randint
#variable for player number
num_player = 0
#generar el numero que sera compárador
num_com = 1
#variable exit for loop
exit= 'y'
while exit == 'y':
#while the number is not same, not exit of loop
    while num_com != num_player:
        #variable for player number
        num_player = 0
        #generar el numero que sera compárador
        num_com = randint(1,3)
        #ask a number
        print('into a number for play')
        num_player = int(input())
        #if no is same, ask for other number
        #comparate if is same number
        # comparate the number of player with number of random
    print('Fine, well done')
    print('Do you want continues? (Y/N)')
    exit =str(input().lower())

    # print good luck
    
    
    
    
print('end game')

# ask question for play other time
#the player responses (y/n)
#if y continues other game
#if n finish the game


 