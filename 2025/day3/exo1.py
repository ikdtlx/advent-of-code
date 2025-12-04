L =[]
with open("input.txt", "r") as f :
    for elt in f :
        L.append(elt.strip())
max=0
i1=-1
i2=-1
res = 0
print(L)
for elt in L:
    for i in range(len(elt)):
        for j in range (i+1, len(elt)):
            if int(elt[i]+elt[j])>max:
                max = int(elt[i]+elt[j])
                i1 = i
                i2 = j
    res += int(elt[i1]+elt[i2])
    max = 0
print(res)
