""" Traitement des données """

L= []
cpt=-1
with open("input.txt", "r") as f :
    for line in f :
        L.append(list())
        cpt+=1
        for elm in line :
            if elm != '\n':
                L[cpt].append(elm)


"""Dessin des chemins"""
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

"""Affichage des chemins"""
#for ligne in L :
#    for elem in ligne:
#        print(elem, end='')
#    print()

"""Résolution : une solution récursive trop lente, une solution récursive par mémoïsation"""

def get_nb_chemins_rec(L:list, cpt:int, ligne:int, ind_trait:int):
    """
    :param L: liste contenant déjà tous les chemins
    :type L: list
    """
    if ligne==(len(L)-1):
        return 1
    elif L[ligne+1][ind_trait]=='^':
        return get_nb_chemins_rec(L, cpt, ligne+1, ind_trait+1) + get_nb_chemins_rec(L, cpt, ligne+1, ind_trait-1)
    else :
        return get_nb_chemins_rec(L, cpt, ligne+1, ind_trait)

#les chemins se recroisent donc on va le faire par mémoïsation
tab = {}
def get_nb_chemins_memo(L, ligne, col):
    res=0
    if (ligne,col) in tab :
        return tab[ligne,col]
    else :
        if ligne==(len(L)-1):
                res=1
        elif L[ligne+1][col]=='^':
                res= get_nb_chemins_memo(L, ligne+1, col+1) +get_nb_chemins_memo(L, ligne+1, col-1)
        else :
                res=get_nb_chemins_memo(L, ligne+1, col)
        tab[ligne, col]=res
    return res
    
ind_trait = L[1].index('|')
print(get_nb_chemins_memo(L, 1, ind_trait))
