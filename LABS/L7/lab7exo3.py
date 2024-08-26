
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

print(somme_de_trois((1,2,-3,3,6)))


    
        
