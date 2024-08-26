from math import *

def patinage(epssglc,tmpmoy):
    """
    indique si il est possible de patiner sur le canal Rideau
    """
    return epssglc >= 30 and tmpmoy <= -10

def alphaNote(note):
    """
    attribue une note alphabetique celon l'échelle de ottawa univ
    """
    échllnote = {10:"A+",15:"A",20:"A-",25:"B+",30:"B",35:"C+",40:"C",45:"D+",50:"D",60:"E",100:"F"}

    key = None

    for elt in échllnote :
        if elt + note >= 100 :

            key = elt

            break
    
    if key is None or note > 100 : return "it is not a value that is in the range 0-100"
    
    return échllnote[key]

def alphaNoteVerif():

    note = float(input("Insérez une note entre 0-100: "))

    while not 0<=note<=100 :
        note = float(input("Cette valeur n'est pas valable ! Reinsérez une note entre 0-100: "))

    mark = alphaNote(note)
    print("Votre note est de:",str(mark))
    print("Echoue" if mark == "E" or mark =="F" else "Réussi")


def boucles(n): #à faire Q4
    if n % 2 == 0:   #nombre paire
        print(" ".join([str(i) for i in range(1, n) if i%2 != 0]))
        print(" ".join([str(elt) for elt in reversed([i for i in range(2, n+1) if i%2 == 0])]))
    else:
        print(" ".join([str(i) for i in range(1, n+1) if i%2 != 0]))
        print(" ".join([str(elt) for elt in reversed([i for i in range(1, n+1) if i%2 != 0])]))  #int -> String

def facteursDeN(entier): #à faire Q5
    fact=[]
    for i in range(2,entier):
        if entier%i == 0 : fact.append(i)
    print("les facteurs de",str(entier),"sont:"," ".join([str(elt) for elt in fact]))
    print(sum(fact))
    return sum(fact) < entier #int -> Bool


def carreParfait(entier):
    """
     fonction Python appelée carreParfait qui prend un entier x comme
    paramètre et vérifie si l’entier est un carré parfait. La fonction retourne une valeur booleene,
    Si le nombre x est un carré parfait, la fonction doit afficher un message le confirmant, afficher aussi sa racine
    carrée, et retourner True. Sinon, elle doit afficher que le nombre x n’est pas un carré parfait et retouner False
    """

    print("l'entier "+str(entier)+" est un carré parfait, sa racine carré est: "+str(sqrt(entier)) if str(sqrt(entier))[-2:]==".0" else "l'entier "+str(entier)+" n'est pas un carré parfait")

    return str(sqrt(entier))[-2:]==".0"

def maFun(entiernatpos):
    """
    calcule mathématique fun !
    """
    return ((-1)**entiernatpos)/(2*entiernatpos+1)

def maFun_bis(entiernatposbis):
    """
    calcule mathématique fun bis !
    """
    return sum([maFun(i) for i in range(0,entiernatposbis+1)])
















def maFun1(entiernatpos):
    """
    calcule mathématique fun !
    """
    return ((-1)**entiernatpos)/(2*entiernatpos+1)

def maFun1_bis(entiernatposbis):
    """
    calcule mathématique fun bis !
    """
    return sum([maFun1(i) for i in range(0,entiernatposbis+1)])