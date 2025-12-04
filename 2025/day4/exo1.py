L= []
with open ("input.txt", 'r') as f :
    for line in f :
        L.append(list(line.strip()))

coordoonnees= dict()
for i in range(len(L)):
    for j in range (len(L[i])):
        coordoonnees[(i,j)]=L[i][j]

#on ajoute des . autour des éléments qui sont en bout de ligne/colonne
for i in range(-1, len(L)+1):
    coordoonnees[(i, -1)]='.'
    coordoonnees[(i, len(L))]='.'
    coordoonnees[(len(L), i)]='.'
    coordoonnees[(-1, i)]='.'


nb_arobases = 0
accessible = 0

for pos, value in coordoonnees.items():
    if value == '@':
        if coordoonnees[pos[0]+1,pos[1]]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0],pos[1]+1]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0]+1,pos[1]+1]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0]-1,pos[1]]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0],pos[1]-1]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0]-1,pos[1]-1]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0]-1,pos[1]+1]=='@':
            nb_arobases+=1
        if coordoonnees[pos[0]+1,pos[1]-1]=='@':
            nb_arobases+=1
        #print(f"pos = {pos} et il y a {nb_arobases} @ autour")
        if nb_arobases<4:
            accessible+=1
    nb_arobases = 0

print(accessible)
