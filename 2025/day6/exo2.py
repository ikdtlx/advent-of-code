#formatage des données 
L = []
with open("input.txt", 'r') as f :
    for line in f :
        L.append(list(line))

#pas de tmp, on veut chiffre par chiffre

for elem in L:
    if '\n' in elem :
        elem.remove('\n')

#exo

#Création d'une liste de couples représentant les coordonnées des colonnes où on a des opérations
tmp = [0]
for j in range(len(L[0])):
        if L[0][j]==L[1][j]==L[2][j]==L[3][j]==L[4][j]==' ': #ajouter L[4] pr input
             tmp.append(j-1)
             tmp.append(j+1)
tmp.append(len(L[0])-1)


range_operations = []
for i in range (0, len(tmp), 2):
    range_operations.append((tmp[i], tmp[i+1]))
#Fin

#Opérations
res = 0
res_add = 0
res_mul = 1
tmp =''
for elem in range_operations:
    if L[-1][elem[0]]=='+':
        for i in range(elem[0], elem[1]+1):
            for j in range(len(L)-1):
                tmp+=L[j][i]
            res_add+=int(tmp.strip())
            tmp=''
    else :
        for i in range(elem[0], elem[1]+1):
            for j in range(len(L)-1):
                tmp+=L[j][i]
            res_mul*=int(tmp.strip())
            tmp=''
    if res_add :
        res+=res_add
        res_add=0
    else :
        res+=res_mul
        res_mul=1
    
print(res)
        

