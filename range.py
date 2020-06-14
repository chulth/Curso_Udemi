#en este archivo se encontraran formas de hacer mejor los rangos y for loops

#lista = [a for a in range(8,0,-2)] # esta es una lista de comprension que
#te ayuda a genera una lista de numeros pares del 8,6,4

'''
# this list print numbers from 10 sice 21
# anly numbers odds (11,13,15,17,19)
lista = [a for a in range(10,21) if a % 2 !=0]
print(lista)
'''

'''
this print many times you enter input, buy it is continues

reclaimp = ('How many times i have tell you \n ' )
print(reclaimp)
veces = int(input())
grito = ('clean up your room, now')
print(grito * veces)
'''
reclaimp = ('how many times i tell you')
print(reclaimp)
try:
	times = int(input())
	claimp = ('clean up your room')
	for times in range(times):
		print(claimp)
except:
	print('enter a number')

