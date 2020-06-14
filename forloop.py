


for i in range(1,21):
	if (i == 4) or (i == 13):
		print('unlucky')
	elif i % 2 != 0 :
		print('odd')
	else:
		print('even')  
	
# its the same code  but refactory
# its better because give more data with less code and better present


for num in range(1,21):
	if (num == 4) or (num == 13):
		state = 'Unlucky'
	elif i % 2 != 0 :
		state ='odd'
	else:
		state = 'even'  
	print('The {}  is {} '.format(num,state))