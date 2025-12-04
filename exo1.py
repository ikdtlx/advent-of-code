L = []
with open ("jour1\input-test.txt", 'r') as f:
    for elt in f:
        elt = elt[:-1]
        L.append(elt)
dial = 50
cpt= 0

for elt in L :
    if elt[0]=='R':
        dial = (dial + int(elt[1:]))%100
    else :
        dial = (dial - int(elt[1:]))%100

    if dial == 0:
        cpt +=1
    print(dial)

print(cpt)
