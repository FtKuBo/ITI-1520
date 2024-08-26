import random

l=[]
for i in range(100):
    k=random.randrange(1,100+1)
    l.append(k)
print(l)
def recherche(v):
    global l
    Npas=0
    for i in l:
        Npas += 1
        if i==v:
            print(Npas)
            return True

    print(Npas)
    return False



#################################
matr=[[1,2,3],[4,5,6]]
v=4
def matrice(M,v):
    Npas=0
    for i in M:
        for j in i:
            Npas+=1
            if j==v:
                print(Npas)
                return True
    print(Npas)
    return False

matrice(matr,v)


