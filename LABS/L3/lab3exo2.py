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


