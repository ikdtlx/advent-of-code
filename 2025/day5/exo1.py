L=list()
with open("input.txt", 'r') as f :
    for line in f:
        L.append(line.strip())
i=0
while L[i]!='':
    i+=1
available = L[i+1:]
fresh = L[:i]
nb_fresh = 0
verified = []
for elem in available:
    for i in range(len(fresh)):
        tiret = int((len(fresh[i])-1)/2)
        if int(elem) in range(int(fresh[i][:tiret]),int(fresh[i][tiret+1:])+1) and elem not in verified:
            #print(range(int(fresh[i][:tiret]),int(fresh[i][tiret+1:])+1))
            nb_fresh+=1
            verified.append(elem)
print(nb_fresh)
