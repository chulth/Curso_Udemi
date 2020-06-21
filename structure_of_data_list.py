from string import capwords

'''
a= range(1,100)
list = [a]
nums=list
print(nums)

#response of course
num = list(range(1,100))

#my response
nums=[i for i in range(1,100)]
print(nums)
print(num)
'''
people=['jorge','jhon','diana', 'pedro']
people.remove('jorge')
people[0]= 'John'
people[1]= 'Diana'
people[2]= 'Pedro'
people.append('gustavo') 
people.append('veronica')
people.append('alan')
people.append('juan')
people.append('nahuel')
people.sort()
nu=[i[0].upper() +i[1:] for i in people] #this code capitalize words, its functional!!!
print(nus)
num=[num*10 for num in range(1,6)] #this list storage numbers 10 to 10
#print(num)
for i in range(0,60,10):
    print(i)
phrase ='this is a phrase with vowels'
without = [''.join(i for i in phrase if i not in 'aeiou')]#this function select only letters
#print(without) 

numbers = [0,1,2,3,4,5,6,7,8,9]
evens = [ num for num in numbers if num % 2 == 0]
odds = [ num for num in numbers if num % 2 != 0]
whats = [num *2 if num % 2 == 0 else num/2 for num in numbers]

#print(evens)
#print(odds)
#print(whats)

answer = [num for num in range(1,101) if num % 12 == 0]
#print(answer)