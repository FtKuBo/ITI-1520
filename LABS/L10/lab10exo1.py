from math import *
class Temps:
  '''classe temporelle'''

  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.heure = h
    self.minute = m
    self.seconde = s
    self.setTemps(self.heure,self.minute,self.seconde)

  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''        
    if not 0<=self.minute<=59:
      self.heure=self.minute%60
      self.minute//=60
    if not 0<=self.seconde<=59:
      self.minute=self.seconde%60
      self.seconde//=60
    self.heure = h%24 
    self.minute = m
    self.seconde = s

  def affiche_heure(self):
    '''(Temps)-> None'''
    print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)) 

  def __repr__(self):
    '''(Temps)-> str'''
    return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

  def __eq__(self, autre):
    '''(Temps)-> bool'''
    return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde
  
  def estAvant(self, autre):
    return self.heure<autre.heure if self.heure !=autre.heure else self.minute<autre.minute if self.minute!=autre.minute else self.seconde != autre.seconde
  
  def durée(self, autre):
    t3= Temps(abs(self.heure-autre.heure),abs(self.minute-autre.minute),abs(self.seconde-autre.seconde))
    return t3
  

t1 = Temps(12,4,0)
t2 = Temps(10,2,1)
print(t1.estAvant(t2))
print(t2.estAvant(t1))
t2.setTemps(12,45,2)
print(t1.estAvant(t2))
print(t1.durée(t2))

