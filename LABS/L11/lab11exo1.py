def verif(l,length):
    if length == 0 :
        return True
    else :
        if not (0<=l[0]<=9) : return False
        return verif(l[1:],len(l)-1)
    
print(verif([1,2,3,9,4,6,1],7))
print(verif([1,2,3,90,4,6,1],7))


###########################################