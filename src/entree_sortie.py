"""
GRO120: Gestion des fichiers d'entrée et de sortie pour les données de filtrage de lidar

Auteurs: Simon Lacroix et Vincent Duchesne
Date: 07/10/2026
"""

import os


def lire_fichier_entree(nom_fichier):
    """
        DESC: Fonction qui permet de lire un fichier texte pour former un tableau.
        Ce tableau permettra ensuite de filtrer les données d'entrée.
              
        RETOUR: Tableau de données
    """
    # Créer une liste vide afin d'y ajouter les données du fichier
    donnee_liste = []

    # Créer un with afin de parcourir chaque ligne du fichier et de le mettre dans la nouvelle liste
    with open(nom_fichier, "r") as fichier:  # Ouvre le fichier en mode lecture
        for ligne in fichier:  # Sert a parcourir le fichier ligne par ligne
            valeur = float(
                ligne
            )  # Sert à transformer les valeur qui sont en string en float
            donnee_liste.append(
                valeur
            )  # Sert à mettre les valeurs de chaque ligne dans la nouvelle liste

    return donnee_liste


def ecrire_fichier_sortie(points_sortie, nom_fichier):
    """
        DESC: Fonction qui permet d'écrire dans un fichier de sortie spécifié une liste
        de points entrée en paramètre.
    """
    # si le répertoire de sortie n'existe pas, le créer
    repertoire_sortie = os.path.dirname(nom_fichier)
    if (not os.path.exists(repertoire_sortie)):
        print("created sortie")
        os.makedirs(repertoire_sortie)

    # Ouvrir le fichier de sortie en mode write, ce qui le crée ou l'efface de tout contenu
    with open(nom_fichier, "w") as fichier:
        for donnee in points_sortie:
            # Écrire chaque point dans le fichier de sortie, chacun sur une ligne
            fichier.write(str(donnee) + "\n")
