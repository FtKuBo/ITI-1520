from math import *


def tempsVoyage(dist,vts):
    """
    Calcule le temps du parcours d'une distance en fonction de la vitesse du voyage
    """
    return (dist / vts ) * 60



def noteFinale(labnote,devrmoy,qznote,partnote,examfinal):
    """
    Calcule de la note finale d'un éleve à partir des 5 notes obtenus et de leur coefficient
    """
    return labnote*0.1+devrmoy*0.25+qznote*0.05+partnote*0.2+examfinal*0.4




def bibformat(autr, ttre, vill, msnEdtn, ans):
    """
    affiche une phrase
    """
    return autr+" ("+str(ans)+"). "+ttre+". "+vill+": "+msnEdtn




def bibformatPrint():
    """
    affiche phrase en fonction de l'entrée
    """
    v1=input("SVP entrez l'auteur: ")
    v2=input("SVP entrez le titre: ")
    v3=input("SVP entrez la ville: ")
    v4=input("SVP entrez la maison d'edition: ")
    v5=input("SVP entrez l'an de publication: ")
    print(bibformat(v1,v2,v3,v4,v5))





def logFun(vls):
    """
    résouds l'équation du type : 10^4y=x+3 
    """
    
    return (log(vls+3,10))/4




def anneeBis(yr):
    """
    If yr n'est pas divisible par 4, l'année n'est pas bissextile. If yr est divisible 
    par 4, l'année est bissextile sauf si an est divisible par 100 et pas par 400.
    """
    return yr%4 == 0 or yr%100 == 0 and yr%400 != 0
