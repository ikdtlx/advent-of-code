L = []
with open ("jour1\input.txt", 'r') as f:
    for elt in f:
        elt = elt[:-1]
        L.append(elt)
dial = 50
cpt= 0

for elt in L :
    b = dial
    if elt[0]=='R':
            dial = (dial + int(elt[1:]))%100
            cpt += (b + int(elt[1:]))//100
    else :
        for _ in range (int(elt[1:])):
            dial = (dial -1)%100
            if dial ==0:
                 cpt+=1


print(cpt)
