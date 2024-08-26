"""
exercice 1
"""

compteur = 10

while (compteur > 0):
    print(compteur)
    compteur -= 1



###########################


"""
exercice 2
"""

value = int(input("donnez une valeur N: "))

for i in range(1,value+1):
    print(i)


#################################
"""
exercice 3
"""

from random import *

def devine():
    num = randint(1,10)
    dev = int(input("devine le chiffre entre 1 et 10: "))
    x = 0
    
    while dev != num :
        x+=1
        dev = int(input("réessaies ce n'est pas le bon nombre: "))
    print("bravo vous avez réussi au bout de",x,"tentatives")

devine()
        

                  
    
