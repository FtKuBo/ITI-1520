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
