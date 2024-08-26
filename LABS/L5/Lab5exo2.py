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
    
