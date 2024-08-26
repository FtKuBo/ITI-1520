from math import *

x = int(input("donnez la valeur a : "))
y = int(input("donnez la valeur b : "))

print("division entiére :", x//y,"le restant :", x%y)


####################################################


def transform (Celsius):
    # transform température en Fahrenheit float
    return Celsius *  1.8000 + 32.00




###################################################

def calcule(devmoy, partiel, examen):
    # calcule moyenne finale float
    return devmoy*(25/100) + partiel*(25/100) + examen*(50/100)




###################################################


def calculeSurface(c1, c2, c3):
    # calcule suface float
    p = c1 + c2 + c3
    return sqrt(p*(p-2*c1)*(p-2*c2)*(p-2*c3))/4


print(transform(25))
print(calcule(60,75,95))
print(calculeSurface(5,6,7))

