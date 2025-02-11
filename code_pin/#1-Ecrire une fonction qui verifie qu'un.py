#1-Ecrire une fonction qui verifie qu'une chaine a uniquement 4 caracteres
#2Ecrire une fonction qui verifie qu'une chaine ne contient que des chiffres
#3 Ecrire un programme principal en bouche qui demande un code PIN (4caracteres)et verifie qu'il est valide
 
 
#Comparer 2 chaines de caracteres
#chaine 1 : chaine de réference
#chaine 2 : chaine a comparer
#Renvoie : True si chaine1=chaine2,False sinon
 
 def Comparer2 Chaine (chaine1,chaine2):
    if(chaine1==chaine2):
        return True
    else
    return False
 
#verifier q'une chaine a 4 Caracteres
#chaine1: chaine a verifier
#renvoye:vrai si il y a 4 caracteres sinon faux
 
def Verifier4caracteres(chaine1):
    if(len(chaine1)==4):
        return True
    else :
        return False
 
 
#verifier qu'il y a que des chiffres
#chaine1:chaine a verifier
#renvoye :vrai s'il y a que des chiffres sinon faux
 
def liste_chiffres(chiffres):
   chiffres = [0,1,2,3,4,5,6,7,8,9]
 
def Verifierchiffre(chaine1):
   if (int(chaine1)):
      return True
   else :
      return False