'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list1, command, location, value = 0):
    if (command == "remove") and (location == "end"):
        list1.pop(-1)
        return print(list1)
    elif (command == "remove") and (location == "beginning" ):
        list1.pop(0)
        return print(list1)
    elif (command == "add") and (location == "beginning"):
        list1.insert(0,value)
        return print(list1)
    elif (command == "add") and (location == "end"):
        list1.append(value)
        return print(list1)
        



#list_manipulation([1,2,3], "remove", "end")
#list_manipulation([1,2,3], "remove", "beginning") #  1
#list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
#list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]

def palindrome(string):
    lis1=list(string)
    lis2 = (lis1[::-1])
    if lis1 == lis2:
        return True
    return False 
   

#palindrome('hannah')
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    return num % 2 == 0
    
def partition(l,fn):
    l1=[]
    l2=[]
    for x in l:
        if fn (x):
            l1.append(x)
        else:
            l2.append(x)
    return [l1,l2]
    
    
#partition([1,2,3,4], isEven) # [[2,4],[1,3]]

def sum_all_values(*args):
    total = 0 
    for num in args:
        total += num
    print(total)

#nums = (1,2,3,4,5,6,74,4,6,8)
#sum_all_values(2,2,2,2,2,2,2,2,*nums,2,4,4,4,4,4,4,4)

def calculate(**kwargs):
    dict_loopup={
        'add':kwargs.get('first',0)+kwargs.get('second',0),
        'substract': kwargs.get('first',0) - kwargs.get('second', 0),
        'multiply': kwargs.get('first',0)*kwargs.get('second',0),
        'divide' : kwargs.get('first',0)/kwargs.get('second',0),
        }
    is_float = kwargs.get('make_float',False)
    operation_value = dict_loopup[kwargs.get('operation', '')]
    if is_float:
        final = '{} {}'.format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = '{} {}'.format(kwargs.get('message', 'the result is '), int(operation_value))
    
    return final



calculate(make_float = False, operation = 'add', message = 'You just added', first=2, second=4)#'You just added 6'
calculate(make_float= True, operation =  'divide', first = 3.5, second = 5) # ther result is 0.7
