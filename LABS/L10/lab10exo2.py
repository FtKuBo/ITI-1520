class Voiture:

    def __init__(self,marque="Ford",couleur="rouge"):
        self.marque=marque
        self.couleur=couleur
        self.pilote="personne"
        self.vitesse=0

    def choix_conducteur(self,nom):
        self.pilote=nom
    
    def accelerer(self,taux,duree):
        if self.pilote!="personne":
            self.vitesse=taux*duree
        else: raise Exception ("there is no pilote")

    def affiche_tout(self):
        print("la marque de la voiture est",self.marque, end=" ")
        print("la couleur de la voiture est",self.couleur, end=" ")
        print("le pilote de la voiture est",self.pilote, end=" ")
        print("la vitesse de la voiture est",self.vitesse, end=" " )

    def __repr__(self):
        return "la voiture est un(e)",self.marque,"elle est",self.couleur,"son pilote est",self.pilote,"sa vitesse est",str(self.vitesse),"m/s"
            
    def __eq__(self, autre: object) -> bool:
        return self.marque==autre.marque and self.couleur==autre.couleur and self.pilote==autre.pilote and self.vitesse==autre.vitesse
    
a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a3.choix_conducteur("Jul")
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)
a2.affiche_tout()