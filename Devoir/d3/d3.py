def compte100(L):
    #retourne le nb d'element dans la liste supérieur à 100
    # contrat type : list(float) -> int   (en effet on parle de liste de nombre et pas de liste d'entier)
    try:
        return sum([1 if elt > 100 else 0 for elt in L])
    
    except:
        raise Exception("La composition ou la structure de la liste n'est pas conforme")


def sommeListeDiv2(L):
    #retourne la somme des elements de la liste qui sont paires
    #list(int) -> int (car somme d'entier)
    try:
        return sum([elt for elt in L if elt%2==0])
    
    except:
        raise Exception("La composition ou la structure de la liste n'est pas conforme")


def triples(string):
    #vérifie il y a au moins une séquence de 3 caractères consécutifs égaux
    #string -> bool
    try:
        for char in string:
            if char*3 in string:
                return True
        return False
    
    except:
        raise Exception("L'entrée n'est pas une chaine de charactére/string")
    
def momo(string):
    #retourne une nouvelle chaine de caractères qui contient les caractères de la chaine donnée une fois chacun, en même ordre, et avec leur nombre de répétitions.
    #string -> string
    try:
        res = ""
        x=0
        for char in string:
            if len(res)<=0:
                res+=char

            if char !=res[-1]:
                res+=str(x)+char
                x=1

            elif char == res[-1]: x+=1

        return res+str(x)
    except:
        raise Exception("L'entrée n'est pas une chaine de charactére/string")

def noDup(string):
    #retourne une nouvelle chaine de caractères qui contient les caractères de la chaine donnée une fois chacun, en même ordre, sans répétitions.
    #string -> string
    try:
        res = ""
        for char in string:
            if len(res)<=0:
                res+=char

            if char != res[-1]:
                res+=char

        return res
    
    except:
        raise Exception("L'entrée n'est pas une chaine de charactére/string")
