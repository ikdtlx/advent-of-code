#formatage des données 
L = []
with open("input.txt", 'r') as f :
    for line in f :
        L.append(list(line))

tmp=''
L2 = [
    [],
    [],
    [],
    [],
    []
]
for i in range(len(L)):
    for elt in L[i] :
        if elt not in ['', ' ', '\n']:
            tmp+=elt
        elif tmp!='' :
            L2[i].append(tmp)
            tmp=''
    if tmp not in ['', '\n']:
        L2[i].append(tmp.strip())
        tmp= ''

#exo
res_tmp_add=0
res_tmp_mul = 1
res = 0

for i in range(len(L2[0])):
    for j in range(len(L2)-1):
        if L2[-1][i]=='+':
            res_tmp_add +=int(L2[j][i])
        else :
            res_tmp_mul *=int(L2[j][i])
    if res_tmp_add!=0:
        res+=res_tmp_add
    else :
        res+=res_tmp_mul
    res_tmp_add = 0
    res_tmp_mul = 1
print(res)
