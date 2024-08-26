def transl(d, s):
    #prends comme entrée un dictionnaire Python d et une chaine des caractères s, et retourne la traduction de s en d.
    #dict, string --> string
    #si c'est un clé on retoure sa valeur 
    #si non si c'est une valeur on retourne sa clé on utilisant sa position dans la liste des valeurs pour trouver sa clé dans la liste des clé
    #si non on return Uknown
    return d[s] if s in d else list(d.keys())[list(d.values()).index(s)] if s in d.values() else "Unknown"

def setOp(l1,l2):
    #list,list --> set
    #on fait la somme des deux liste ce qui va nous donner une seule liste
    #cette liste on la transforme en set en utiliseant set()
    #rappel : dans un set tout est déjà classé et trier donc pas de répetition
    return set(l1+l2)

def matrixMinMax(m):
    #list --> tuple
    #on fait l'hypothése que la liste n'est pas vide 
    #et en utiliseant les fonctions min max on retourne un tuple avec le minimum et le maximum de la liste
    mnew=[]
    for elt in m : mnew+=elt
    return min(mnew),max(mnew)