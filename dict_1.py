game=['score','high_score','number_of_lives','items', 'power_ups','armo','enemies_on _screen']

games =dict.fromkeys(game,0 )

#print(games)

playlist= {
    'title':'Patagonia Bus',
    'author' :'Diana Rodriguez',
    'songs' : [
        {'title song':'song1','artist' :['Calamaro'], 'duration': 2.5},
        {'title song':'song2','artist' :['Queen'], 'duration': 3.5},
        {'title song':'song3','artist' :['Jackson'], 'duration': 1.5},
        {'title song':'song4','artist' :['Soda Stereo'], 'duration': 2.8},
        
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

#print(total_length) 

#for song in playlist['songs']:
    #print('estos son los {} y sus canciones {} para nuestra lista patagonia'.format(song['artist'], song['title song']))



list1 =[['jhon', 'diana'],[' alejandra', 'jorge',], ['pablo','Alfredo']]
list2 =['Bulla', ' Andrade', 'Andrade', 'Bulla', 'Bulla']

#juntos = {list1[i]:list2[i] for i in range(len(list1))}
#print(juntos)

#masjuntos = {i[0].upper()+i[1:]: j.upper() for i,j in juntos.items()}
#print(masjuntos)
#todos = { (i.upper() if i is 'diana' else i ): (j.upper()) for i, j in juntos.items()}
#print(todos)

#lleno={(k): ( v ) for k,v in list1}
#print(lleno)
#print(dict(list1))
key={k: chr(k) for k in range(65,91)}
print(key)