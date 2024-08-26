def transaction(age):
    print("Transaction accepté" if 18<=int(age)<=55 else "Transaction refusée")

age = input("Insérez votre age: ")

transaction(age)



##################################################################



def activité(temp):
    
    """
    chaque activité a un numéro celon la température une activité est conseillée
    
    """
    
    actv = {1:"la natation",2:"le soccer",3:"le volleyball",4:"le ski"}
    
    key = 1 if temp >= 80 else 2 if 60.0 <= temp < 80 else 3 if 40.0 <= temp < 60.0 else 4
    
    print("il vous ai conséiller de faire l'activité n°"+str(key),"soit", actv[key])

température = float(input("fait il beau aujourd'hui ? Insérer la température: "))

activité(température)




##################################################################




def estDivisible(entier) :
    """
    L’algorithme estDivisible analyse l’entier et retourne un entier qui indique le résultat de
    l’analyse: 1 (divisible par 2 et par 3), 2 (divisible par 2 ou par 3), 0 (pas divisible ni par 2 ni par 3)

    """
    print(1 if entier%2==entier%3==0 else 2 if entier%2==0 or entier%3==0 else 0 )



val = int(input("Insérez un entier: "))

estDivisible(val)




##################################################################



def nbRacine(a, b, c):
    """
    Développez un programme qui détermine combien de
    racines réelles existent pour une équation quadratique:
    ax2 + bx + c = 0 (a, b, et c sont des constantes réelles)
    
    """

    print("cette équation admet 2 racines réelles distinctes" if b**2-4*a*c > 0 else "cette équation admet une seul racine réelle" if b**2-4*a*c == 0 else "cette équation n'admet pas de racines réelles")

a = float(input("donnez la valeur de a: "))
b = float(input("donnez la valeur de b: "))
c = float(input("donnez la valeur de c: "))

nbRacine(a, b, c)

# ça ne marche pas pour n'importe quelle cas car je pense qu'il y' a une limite de nombre aprés la virgule qui est pris en compte par la méthode float
