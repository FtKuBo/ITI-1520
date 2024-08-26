
def histogramme(chc):
    '''char->list'''
    return list({elt:list(chc).count(elt) for elt in sorted(list(set(list(chc))))}.items())

print(histogramme("hellooo"))

