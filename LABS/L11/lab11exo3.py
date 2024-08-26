def verif(l,length):
    if length == 0 :
        return True
    else :
        if not (0<=l[0]<=9) : return False
        return verif(l[1:],len(l)-1)
    
print(verif([1,2,3,9,4,6,1],7))
print(verif([1,2,3,90,4,6,1],7))


###########################################

def create(n,L=[],i=0):

    return L if i == n else create(n,L+[i],i+1)

print(create(int(input("donnez un nombre n: "))))


###########################################

def Euclide(x,y):

    print("x:",x,"%","y:",y,"=",x%y)

    if x % y == 0 and x >= y : return y

    else : return Euclide(y, x%y)

print(Euclide(1234,4321))
print(Euclide(8192,192))
print(Euclide(1625,3225))
