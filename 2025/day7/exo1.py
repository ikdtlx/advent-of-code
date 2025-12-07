with open("input.txt", "r") as f :
    L = [list(l.strip()) for l in f]

ind_s = L[0].index('S')
L[1][ind_s]='|'
cpt=0
for i in range(1, len(L)-1):
    for j in range(len(L[1])):
        if L[i][j]=='|':
            if L[i+1][j]=='^':
                cpt+=1
                L[i+1][j+1]='|'
                L[i+1][j-1]='|'
            else :
                L[i+1][j]='|'
print(cpt)
