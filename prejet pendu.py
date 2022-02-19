# -*- coding: utf-8 -*-

"""
PROJET DU JEU DU PENDU
-----------------------

"""

# On importe les bibliothèsque utiles:
import random

# Ci-dessous, on importe la fonction dessinPendu à partir du fichier dessinPendu.py que vous avez créé
# grace à la syntaxe:   from  <FICHIER_PYTHON> import <NOM_FONCTIO>
from dessinPendu import  dessinPendu 

# TEST -------------
#print(dessinPendu(7))

# ------------------------------------------------------------------
# ------- DONNEES --------------------------------------------------
# ------------------------------------------------------------------

#"""On définit quelques données, sous la forme de variables,
#utiles au programme pendu"""

# Liste des mots possibles (Vous pouvez en ajouter si vous le souhaitez.)
liste_mots = [
    "armoire","boucle","buisson","bureau","chaise","carton","couteau","fichier","garage","glace","journal","kiwi","lampe","liste","montagne",
    "remise","sandale","taxi","vampire","volant"] 

# TEST -------------
#print(liste_mots[0])


# ------------------------------------------------------------------
# ------- FONCTIONS ------------------------------------------------
# ------------------------------------------------------------------

def recup_Mot_Hasard(liste_mots):
    """
    IN: liste_mots (type list)
    OUT: un string qui est un mot de la liste pioché au hasard.    
    """
    # On compte le nombre de mot
    n = len(liste_mots)
    nb_hasard = random.randint(1,n)
    
    mot_choisi = liste_mots[nb_hasard - 1] # puisque le premier élément a l'indice 0 et pas 1.
    
    return mot_choisi

# TEST
#print(recup_Mot_Hasard(liste_mots))
# ------------------------------------------------------------------

def saisir_une_lettre():
    """ 
    Cette fonction demande à l'utilisateur de saisir une lettre minuscule.
    
    IN: Rien
    OUT: une lettre (chaîne de 1 caractère) saisie par l'utilisateur
    """
    
    # Boucle infinie jusqu'à ce que la saisie soit correcte.
    while True:
        lettre = input("Proposez une lettre minuscule :")

        # si "Q" est donné le program quit
        if lettre =="Q":
            exit() 

        
        # Si la saisie est vide ou qu'elle n'est pas une lettre de l'alphabet minuscule
        if (len(lettre) == 0) or lettre not in "abcdefghijklmnopqrstuvwxyz":
            print("Votre saisie est incorecte")
        else:
            # la saisie est correcte, donc on sort de la fonction en renvoyant la lettre saisie
            return lettre        
        
# TEST
#saisir_une_lettre()
#print(lettres_deja_proposees)
# ------------------------------------------------------------------


def recup_Mot_Masque(mot_complet, lettres_proposee):
    """
    Renvoie un mot masqué (avec des tirets) et avec les lettres déjà trouvées apparentes.
    
    IN: - mot_complet (type str) qui est le mot d'origine
        - lettres (type list) déjà proposées 

    OUT: Renvoie une string qui est le mot d'origine avec des '-' remplaçant 
    les lettres que l'on n'a pas encore trouvées.
    """
    
    mot_masque = ""
    
    for lettre in mot_complet: #boucle de la longeur du mot complet ou on compare chaque lettre une à une à la lettre proposée
        # si la lettre est dans les lettres déjà proposées, 
        # alors elle apparait en clair, sinon, on met un tiret.
        if lettre in lettres_deja_proposees:          # si la lettre est dans les lettres déjà proposées, 
            mot_masque = mot_masque + lettre
        else:
            mot_masque = mot_masque + "-" #nous mettons un tiret pour les lettre pas encore trouver
    
    return mot_masque #nous renvoyons le mot masqué

# TEST
#print(recup_Mot_Masque( "glace", ["a","e","u"] ) )
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# ------- PROGRAMME PRINCIPAL --------------------------------------
# ------------------------------------------------------------------
    
#Initialisation
nb_erreur = 0
nb_essai =0
lettres_deja_proposees=[]
win = False # une variable pour que à la fin le message donnéé coréspond à si le joeur à ganger ou perdu, il est faux il changera seulemnt si le joueur gange

# On tire un mot au hasard
mot_solution = recup_Mot_Hasard(liste_mots)
#print(mot_solution) 

print("\nBienvenu au jeu du PENDU.\n ---------------------")                               #Message de initialisation
print("Vous devez trouver le mot mystère avant que le bonhomme ne soit pendu.\n")

print("Voici le mot mystère:  " + recup_Mot_Masque(mot_solution, lettres_deja_proposees))

while (nb_erreur<9): # à la 9ème erreur, le bonhomme est pendu, c'est perdu
    
    # On saisi une nouvelle lettre 
    lettre = saisir_une_lettre()
    nb_essai +=1 #si la lettre est conforme on incremente le nombre d'essaie même si la lettre donnéé est juste ou fausse
    
    # On teste si la lettre a déjà été proposée.
    if lettre in lettres_deja_proposees:
        # lettre déjà proposée.
        print("C'est dommage, vous aviez déjà proposé cette lettre")
    else:
        # on ajoute la lettre à la liste des lettres déjà proposées
        lettres_deja_proposees.append(lettre)
        
    
    # On test si la nouvelle lettre est dans le mot solution
    if lettre in mot_solution:
        # la lettre est bonne ! On ré-affiche le mot masqué
        print("Bien joué !")
        print("Mot mystère:", recup_Mot_Masque(mot_solution , lettres_deja_proposees) )  #nous remplacon les tiret par la lettre trouvé corespendante
    else:
        # la lettre n'est pas dans le mot, ça fait une erreur de plus.
        print("ERREUR, cette lettre n'est pas dans le mot !\n")
        print(chr(7)) # emmet un bip
        print("Mot mystère:", recup_Mot_Masque(mot_solution , lettres_deja_proposees))
        nb_erreur += 1 #on incrémente le nombre d'erreur par 1
        # On affiche le dessin du Pendu. 
        print(dessinPendu(nb_erreur)) #en fonction du nombre d'erreur une image apparait si le joueur fait une erreur
    
    # Si le mot a été trouvé entièrement
    if mot_solution == recup_Mot_Masque(mot_solution, lettres_deja_proposees) :
        win = True  # al condition win est Vraie donc le message vraie apparaitra
        # le mot a été trouvé entièrement, on sort du while
        break    

              
# On est sorti du while.
# On teste si on a gagné
if win == True :
    # Gagné
    print("C'est gagné en " + str(nb_essai) + " essais.")
else:
    # Perdu
    print("C'est perdu ! Le mot était:", mot_solution)
