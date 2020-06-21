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
#print(z)
midterms=[80, 91,78]
finals=[98,89,53]
students=['dan', 'ang', 'kate']

#[pair for pair in zip(midterms,finals)] #have errors
#final_grades = [pair for pair in zip(midterms,finals)]# this list iterate in other two list
final_grades = [max(pair) for pair in zip(midterms,finals)] # print only max values
final_grades2 = {pair[0]: max(pair[1],pair[2]) for pair in zip(students, midterms,finals)}
#print(final_grades) # this do same of scores
#print(dict(final_grades2))

scores = list(map(
    lambda pair: max(pair),
    zip(midterms,finals)



))

#print(scores) # this do same of final_grades

final_scores = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

#print(final_scores) # this is similar they are in others lenguagues

final_averages = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)

print(final_averages) # this function show the average scores.