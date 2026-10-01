# *** Questions: besoin de valider entrée? (fichier + input de l'utilisateur)
#     Filtres utilisent les données non-valides? (sous zéro)
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

import filtrage


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
    # Ouvrir le fichier de sortie en mode write, ce qui le crée ou l'efface de tout contenu
    with open(nom_fichier, "w") as fichier:
        for donnee in points_sortie:
            # Écrire chaque point dans le fichier de sortie
            print(donnee, file=fichier)  # Une décimale


def stat(donnee_liste):
    """
        DESC: Fonction qui permet d'afficher les statistiques des données d'entrée et de sortie.
    """
    longueur_liste = len(donnee_liste)

    # Gérer le cas d'une liste vide
    if (longueur_liste == 0):
        print("Aucune statistique à afficher, la liste de données est vide")
        return

    print()
    print("Statisiques sur les données d'entrée:")
    print("Le nombre de points d'entrée est:", longueur_liste)
    print()
    print("Statistiques sur les données de sortie:")
    minimum = 100000000000000000
    maximum = 0
    somme = 0
    nb_pt_valide = 0
    liste_pt_valide = []
    for donnee in donnee_liste:
        # Seulement tenir compte des points valides
        if (donnee >= 0):
            # Garder en mémoire le minimum
            if (donnee < minimum):
                minimum = donnee

            # Garder en mémoire le maximum
            if (donnee > maximum):
                maximum = donnee

            # Garder en mémoire la somme pour la moyenne
            somme += donnee

            # Garder un compteur du nombre de points valides
            nb_pt_valide += 1

            #Mettre les données valides dans une liste afin de calculer la médiane
            liste_pt_valide.append(donnee)

            #Trouver la longueur de la liste
            longueur_liste_valide = len(liste_pt_valide)
        


    # Afficher les statistiques calculées
    print("Le minimum est :", minimum)
    print("Le maximum est :", maximum)
    """
    ICI moyenne et mediane utilisent les infos de toute la liste mais devraient utiliser seulement les valides
    """
    moyenne = somme / nb_pt_valide 
    print(f"La moyenne est :", round(moyenne, 1))  # Une décimale

    # Afficher la médiane avec une décimale
    mediane = 0
    donnee_liste.sort()  # Mettre en ordre pour aller chercher la médiane
    # Si longueur paire, faire la moyenne des deux éléments du milieu
    # Exemple: longueur de 6, prendre index 2 et 3
    if (0 == (longueur_liste_valide) % 2):
        mediane = (donnee_liste[(longueur_liste_valide // 2)] +
                   donnee_liste[(longueur_liste_valide // 2) - 1]) / 2
    # Si longueur impaire prendre l'élément du milieu
    # Il correpond à la longueur divisée entière par 2 (ex. 3 => 1):
    else:
        mediane = donnee_liste[longueur_liste_valide // 2]

    print("La médiane est :", round(mediane, 1))

    # Afficher les nombres de points
    print("Le nombre de points valides est:", nb_pt_valide)


#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """
    print("Test lidar (GRO120)")
    # Demander à l'utilisateur l'information nécessaire pour le programme
    fichier_entree = input("Veuillez entrer le nom du fichier d'entrée: ")
    fichier_sortie = input("Veuillez entrer le nom du fichier de sortie: ")
    choix_algo = int(
        input(
            "Veuillez choisir le type d'algorithme à utiliser (1, 2 ou 3): "))

    # Lire le fichier d'entrée pour le convertir en tableau
    points_entree = lire_fichier_entree(fichier_entree)

    # Filtrer les données d'entrée
    points_sortie = []
    if (choix_algo == 1):
        points_sortie = filtrage.filtre_min_max(points_entree)
    elif (choix_algo == 2):
        points_sortie = filtrage.filtre_moyenne_mobile(points_entree)
    elif (choix_algo == 3):
        points_sortie = filtrage.filtre_mediane_mobile(points_entree)

    # Écrire dans un fichier de sortie des données de sortie
    ecrire_fichier_sortie(points_sortie, fichier_sortie)

    # Afficher à l'utilisateur les statistiques sur les données
    stat(points_sortie)
