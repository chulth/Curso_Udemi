'''
Esta funcion aparea dos listas y genera una nueva lista con pares 
#[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]
deben ser dos lista con el mismo numero de valores
es justo la funcion para trabajar con diccionarios
#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

lista1=[1,2,3,4,5,6]
lista2=[10,20,30,40,50,60]
#z=list(zip(lista1,lista2))
z = dict(zip(lista1,lista2))
print(z)