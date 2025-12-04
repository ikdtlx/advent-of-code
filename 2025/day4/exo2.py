L= []
with open ("input.txt", 'r') as f :
    for line in f :
        L.append(list(line.strip()))

coordoonnees= dict()
for i in range(len(L)):
    for j in range (len(L[i])):
        coordoonnees[(i,j)]=L[i][j]

for i in range(-1, len(L)+1):
    coordoonnees[(i, -1)]='.'
    coordoonnees[(i, len(L))]='.'
    coordoonnees[(len(L), i)]='.'
    coordoonnees[(-1, i)]='.'


nb_arobases = 0
nb_accessible = 0
nb_accessible_total = 0
accessibles = []

while True :
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
                nb_accessible+=1
                accessibles.append(pos)
        nb_arobases = 0
    print(nb_accessible)
    nb_accessible_total+=nb_accessible
    if nb_accessible==0:
        break
    while accessibles!=[]:
        coordoonnees[accessibles.pop()]='.'
        nb_accessible-=1
print(nb_accessible_total)
