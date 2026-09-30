"""
GRO120: Banc de test lidar 
        Permet de tester le filtrage d'échantillons de données lidar.
                
        LES 4 ÉTAPES DE TRAITEMENT ATTENDUES SONT : 
           1. Lire les données d'un fichier texte (entrée)
           2. Filtrer les données lues (selon choix)
           3. Écrire les données filtrées dans un fichier texte (sortie)
           4. Afficher les valeurs statistiques des données filtrées valides (>=0)

Auteurs: Simon Lacroix et Vincent Duchesne
Date: 07/10/2026
"""

import sys
import filtrage  #Importer le fichier qui comporte les trois différents filtre à appliquer


#Créer une fonction qui permet de transformer un fichier texte en liste
#Cette liste permettra ensuite de filtrer les données d'entrées
def lire_fichier(nom_fichier):

    #Créer une liste vide afin d'y ajouter les données du fichier
    donnee_liste = []

    #Créer un with afin de parcourir chaque ligne du fichier et de le mettre dans la nouvelle liste
    with open(nom_fichier, "r") as fichier:  #Ouvre le fichier en mode lecture

        for ligne in fichier:  #Sert a parcourir le fichier ligne par ligne
            valeur = float(
                ligne
            )  #Sert à transformer les valeur qui sont en string en float
            donnee_liste.append(
                valeur
            )  #Sert à mettre les valeurs de chaque ligne dans la nouvelle liste

    return donnee_liste


#Créer une fonction qui permet de renvoyer les statistiques à l'utilisateur


def stat(donnee_liste):
    if (len(donnee_liste) == 0):
        print("Aucune statistique à afficher, la liste de données est vide")
        return

    #Afficher la valeur minimale
    minimum = 100000000000000000
    maximum = 0
    numerateur = 0
    denominateur = 0
    nb_pt_valide = 0
    longueur_liste = len(donnee_liste)
    for donnee in donnee_liste:
        if (donnee >= 0):
            if (donnee < minimum):
                minimum = donnee

            if (donnee > maximum):
                maximum = donnee

            numerateur += donnee

            nb_pt_valide += 1

    print("Le minimum est :",minimum)
    print("Le maximum est :",maximum)


    moyenne = numerateur / longueur_liste

    print("La moyenne est :",moyenne)

    print("Le nombre de points d'entrées est:",longueur_liste)
    print("Le nombre de points valide est:",nb_pt_valide)
    
#======================================

    #Afficher la médiane
    mediane = 0
    
    if (0 == (longueur_liste) % 2):
        mediane = (donnee_liste[(longueur_liste / 2)] + donnee_liste[(longueur_liste / 2) - 1]) / 2
    else:
        mediane = donnee_liste[longueur_liste // 2]

    print("La médiane est :",mediane)


    









#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """
    print("Test lidar (GRO120)")

    # Code à compléter..."""
