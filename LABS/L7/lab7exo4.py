
def histogramme(chc):
    '''char->list'''
    return list({elt:list(chc).count(elt) for elt in sorted(list(set(list(chc))))}.items())



###########################################

def histotuple(tpl):
    '''(tuple)->dict
 Retourne un dictionnaire
 Precondition: le tuple contient des entiers
 >>> t = (1,2,-3,3,4,-3,3,3)
 >>> histo_n(t)
 {1: 1, 2: 1, 3: 3, 4: 1, -3: 2}
 '''
    return {elt:tpl.count(elt) for elt in sorted(tpl)}

###########################################


def somme_de_trois(x):
    '''tuple -> bool'''
    for i in range(0,len(x)-2):
        v=sum(x[i:i+3])
        if v==0:
            return True
    return False

#########################################

def move_zeros_v1(x):
    '''list->tuple(list)'''
    L=[]
    for elt in x:
        if not elt == 0:
            L.append(elt)
    return x, L+[0]*x.count(0)

def move_zeros_v2(x):
    '''ça marche aussi pour le move_zeros_3'''
    
    nb=x.count(0)
    while 0 in x: x.remove(0)
    x+=[0]*nb
    
def move_zeros_v3(x):
    front =  0
    back = len(x)-1
    while front < back :
        if x[front] == 0 and x[back]!= 0:
            x[front]=x[back]
            x[back]=0
            front += 1
            back-=1
        elif x[front] == 0 and x[back] ==0:
            back-=1
        else:
            front+=1

print(histogramme("aaabbbbcccc"))
print(histotuple((1,2,3,4,4,5,5,5)))
print(somme_de_trois((1,2,-3,5,6,7)))
print(move_zeros_v1([1,2,0,9,0,0,9,8,6]))
L=[1,2,0,9,0,0,9,8,6]
move_zeros_v2(L)
print(L)
L1=[1,2,0,9,0,0,0,4,5]
move_zeros_v3(L1)
print(L1)
