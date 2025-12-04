with open("input.txt", 'r') as f :
    ch = f.readline()
L = []
tmp = ''
#conversion str -> liste
for i in range (len(ch)):
    if ch[i]==',':
        L.append(tmp)
        tmp=''
    else :
        tmp+=ch[i]
L.append(tmp) #car il n'y a pas de virgule à la fin de la chaîne de caractères
#print(L)
res=0
for elt in L :
    pos_tiret = elt.find('-')
    depart = int(elt[:pos_tiret])
    fin = int(elt[pos_tiret+1:])
    for i in range (depart,fin+1):
        if len(str(i))%2==0 and str(i)[:int(len(str(i))/2)]==str(i)[int(len(str(i))/2):]:
            res+=i
print(f"res final = {res}")



