from math import *

def calcmoy():
    L=list(eval(input("donnez une liste des valeurs séparées par des virgules : ")))
    return "la valeur moyenne est: "+str(sum(L)/len(L))
print(calcmoy())

######################################################################


def notesstat():
    Nt=list(eval(input("Insérez la liste de notes des étudiants séparées par des virgules : ")))
    return "-la meilleur note de la classe est: "+str(max(Nt))+"\n-la moins bonne note de la classe est: "+str(min(Nt))+"\n-la moyenne de la classe est: "+str(sum(Nt)/len(Nt))
print(notesstat())

#####################################################################


def calcule_distance(n):
    return [(2*(n**2)*cos(radians(i))*sin(radians(i)))/9.8 for i in range(0,100,10)]

print(calcule_distance(9))


#####################################################################


def écart_type(L):
    moy = sum(L)/len(L)
    return "l'écart type est "+str(sqrt(sum([(elt-moy)**2 for elt in L])/len(L)-1))


L=list(eval(input("donnez une liste des valeurs séparées par des virgules : ")))
print(écart_type(L))
