from random import randint 

def coin_fliip():
    '''this function return Heads or tails'''
    value= randint(0,1)
    if value is 1:
        return 'Heads'
    else:
        return 'Tails'

#print(coin_fliip())

def days_of_week(day):
    '''this function retunr one day of weekend'''
    days={
        1:'Sunday',
        2:'monday',
        3:'Tuesday',
        4:'Wednesday', 
        5:'Thursday',
        6:'Friday', 
        7:'Saturday',
        }

    return days.get(day,None)

    
#print(days_of_week(-1))

def multiple_count(string):
    for i in string:
        print(string.lower().count(i))
        for j in string:
            print(j)
    count_other_letters = {[j for j in string] : [(string.lower().count(i)) for i in string] for j,i in string}
    
    count_letters = { j: (string.lower().count(i)) for j , i in string }

#multiple_count('buenos dias niños')

def frecuency(something, char):
    num =[something.count(char) for char in something]
    print() num 

frecuency([4,2,2,2,2,2,1,1,1], 2)