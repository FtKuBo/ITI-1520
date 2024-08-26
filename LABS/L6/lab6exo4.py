s1="bon"
s2="mauvais"
s3="fou"

print("ou" in s3)
print(" " not in s1)
print(" " in s1+s2+s3)
print(s3*10)
print(len(s1+s2+s3))



###################################

aha = "abcdefgh"

print(aha[:4])
print(aha[3:6])
print(aha[-1])
print(aha[-3:-1])
print(aha[-5:])
print(aha[-3:])
print(aha[0]+aha[3]+aha[6])
print(aha[1]+aha[3])


##################################


s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''
nS=s.replace("."," ").replace(","," ").replace(";"," ").replace("\n"," ")
print(nS)
nS=nS.strip()
print(nS)
nS=nS.lower()
print(nS)
print(nS.count("de"))
nS=nS.replace("était","est")
print(nS)



##################################

def compte(s,a):
    return s.count(a)

def comptebis(s,a):
    return sum([1 if s[i]==a else 0 for i in range(len(s))])

s=input("donnez une chaine de carachtére: ")
a=input("donnez un carachtére ou plusieurs: ")
print(compte(s,a),comptebis(s,a))



