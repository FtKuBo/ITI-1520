from math import *

def triangle(n,i=1): 
    """
    int -> None
    Notre cas de base est lorque i est supérieur à n la fonction s'arrête
    sinon elle continue à s'appeller elle même
    """
    if i>n:                                           #cas de base
        return ""
    else:
        print('*'*i)
        return triangle(n,i+1)                        #appel récursif de la fonction


def etoiles(n,i=None):
    """
    int -> None
    Notre cas de base est i>n ainsi la fonction s'arrête
    sinon elle continue à s'appeller elle même
    """
    if i==None: return etoiles(n,-n)                   #initialisation de i à -n car on ne peut pas le faire directement dans les parenthése
    if i>n: return  ""                                 #cas de base là ou la fonction s'arrête
    else:                                             
        if i!= 0:print('*'*abs(i))                     #valeur absolue de -4 -3 -2 -1  1  2  3  4  -> 4 3 2 1 1 2 3 4
        return etoiles(n,i+1)                          #appel recusif de la fonction

def  prodListePos_rec(l,length):
    """
    l->int
    fais le produit des élement positif de la liste avec la récursivité
    """
    if length==0:
        return 1
    else:
        return l[length-1]*prodListePos_rec(l,length-1) if l[length-1]>0 else prodListePos_rec(l,length-1)

def prodLRec1(l):
    """
    l->int
    fais le produit des élement positif de la liste avec la récursivité
    """
    if l==[]:
        return 1
    else:
        return l[0]*prodLRec1(l[1:]) if l[0]>0 else prodLRec1(l[1:])
