
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
print(histotuple((1,2,3,7,7,7,8,8,9)))
        
