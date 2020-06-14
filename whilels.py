#test code

'''
# this code using for make while loop unil write please, sr, two magic words
user__responce = None
while user__responce != 'please, sr':
	print('say the magic word: ')
	print('U0001f600')
	user__responce = input()

#una formas mas elevada de hacer esto es sin los strings de multiplicacion
#this is better do without strings multiplication, because is ugly solution
num = 0
emo = 'U0001f600'
while num < 20:
	print(num * emo ) #this es the part ugly of solution
	num+=1

print('finish joke')
'''
for num in range(1,11):
	count = 1
	smileys = ""
	while count <= num:
		smileys += "\U0001f600"
		count += 1
	print(smileys)
