"""
GRO120: Analyse de filtrage de données lidar

Auteurs: Simon Lacroix et Vincent Duchesne
Date: 07/10/2026
"""


def insertion_sort(liste):
    """
    DESC: Trie en ordre croissant une liste de nombres entrée en paramètre,
    basé sur l'algorithme 'insertion sort'.

    RETOUR: Une liste de nombres triée en ordre croissant.
    """
    # faire une copie de la liste pour éviter de modifier l'originale
    liste = liste + []
    # sauter le premier élément de la liste, on considère qu'il est trié
    for i in range(1, len(liste)):
        # garder en mémoire l'élément actuel à insérer
        actuel = liste[i]
        # commencer avec l'élément à gauche de l'actuel
        j = i - 1
        # tant qu'il reste d'autres éléments à gauches et qu'ils sont plus élevés que l'actuel,
        # les tasser d'une place vers la droite (pour créer un trou pour l'actuel)
        while (j >= 0 and liste[j] > actuel):
            liste[j + 1] = liste[j]
            j -= 1
        # insérer l'actuel au trou formé dans la liste
        liste[j + 1] = actuel

    return liste


def affiche_stats(donnee_liste):
    """
    DESC: Fonction qui permet d'afficher les statistiques des données d'entrée et de sortie.
    """
    longueur_liste_entree = len(donnee_liste)

    # Gérer le cas d'une liste vide
    if (longueur_liste_entree == 0):
        print("Aucune statistique à afficher, la liste de données est vide")
        return

    print("\nStatisiques sur les données d'entrée:")
    print("Le nombre de points d'entrée est:", longueur_liste_entree)
    print("\nStatistiques sur les données de sortie:")

    minimum = 10_000_000
    maximum = 0
    somme = 0
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

            # Mettre les données valides dans une liste
            liste_pt_valide.append(donnee)

    # La longueur de la liste valide est le nombre de points valides
    nb_pts_valides = len(liste_pt_valide)

    if (nb_pts_valides == 0):
        print("Aucun point valide, aucune statistique à afficher.")
        return

    # Afficher les nombres de points
    print("Le nombre de points valides est:", nb_pts_valides)

    # Afficher les statistiques calculées
    print("Le minimum est :", minimum)
    print("Le maximum est :", maximum)

    # La moyenne est la somme des éléments valides divisés par leur nombre
    moyenne = somme / nb_pts_valides
    print(f"La moyenne est :", round(moyenne, 2))  # Deux décimales

    mediane = 0
    liste_pt_valide.sort()  # Mettre en ordre
    # Si longueur paire, faire la moyenne des deux éléments du milieu
    # Exemple: longueur de 6 => ([2] + [3]) / 2
    if (0 == (nb_pts_valides) % 2):
        mediane = (liste_pt_valide[(nb_pts_valides // 2)] +
                   liste_pt_valide[(nb_pts_valides // 2) - 1]) / 2
    # Si longueur impaire prendre l'élément du milieu
    # Il correpond à la longueur divisée entière par 2 (ex. 3 => 1):
    else:
        mediane = liste_pt_valide[nb_pts_valides // 2]

    print("La médiane est :", round(mediane, 2))  # Deux décimales
