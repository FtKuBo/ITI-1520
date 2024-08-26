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

