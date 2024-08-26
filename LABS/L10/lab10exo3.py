class CompteBancaire:
    def __init__(self,nom="Dupont",solde=1000):
        self.nom=nom
        self.solde=solde

    def depot(self,somme):
        self.solde+=somme
    
    def retrait(self,somme):
        self.solde-=somme
        print("attention tu est dans le rouge!" if self.solde<0 else "")

    def affiche(self):
        print("Le solde du compte bancaire de",self.nom,"est de",str(self.solde),"dollars")

    def __eq__(self,autre):
        return self.nom==autre.nom and self.solde==autre.solde
    
    def __repr__(self):
        return "nom :",self.nom,"; solde",str(self.solde)


class CompteEpargne(CompteBancaire):
    def __init__(self,nom,solde):
        self.taux=0.3/100  
        CompteBancaire.__init__(self,nom,solde)

    def changeTaux(self,val):
        self.taux=val/100
    
    def capitalisation(self,nbMois):
        self.depot(nbMois*self.taux*self.solde)
        return "Capitalisation sur "+str(nbMois)+" mois au taux mensuel de "+str(self.taux*100)+"%"
    


c1=CompteEpargne("hamid",400)
c1.depot(350)   
c1.affiche()

c1.capitalisation(12)
c1.affiche()

c1.changeTaux(.5)
print(c1.capitalisation(12))
c1.affiche()
