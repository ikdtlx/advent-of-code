with open("input.txt", "r") as f :
    L = [s.strip().split('\n') for s in f]
L2 = [tuple(elem.pop().split(',')) for elem in L]
L3 = [(int(x), int(y)) for (x,y) in L2]
d = {}
for i in range(len(L3)):
    for j in range(1, len(L3)):
        if L3[i]!=L3[j]:
            d[(L3[i], L3[j])]=(abs(L3[i][0]-L3[j][0])+1)*(abs(L3[i][1]-L3[j][1])+1)
max = 0
k_max = 0
for key, value in d.items():
    if d[key]>max :
        max = d[key]
        k_max = key
print(max)
