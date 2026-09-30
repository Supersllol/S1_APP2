"""
GRO120: Module filtrage - implémentation des filtres à appliquer sur les données lidar 

Auteurs: Simon Lacroix et Vincent Duchesne
Date: 07/10/2026
"""


#===========================================
def filtre_min_max(points, distance_min=0.5, distance_max=15.0):
    """
    DESC: Filtre les points en éliminant ceux qui sont hors des bornes min/max.
          Les valeurs inférieures à la borne min sont remplacées par -1.
          Les valeurs supérieures à la borne max sont remplacées par max.
          
    RETOUR: Tableau de données filtrées
    """

    #créer un tableau vide afin d'y mettre la solution
    points_filtre = []

    #créer un boucle for afin de parcourir le tableau
    for i in range(len(points)):

        #créer des conditions à l'aide de if, elif et else
        #afin de changer la valeur si besoin
        if (points[i] < distance_min):
            points_filtre.append(-1)

        elif (points[i] > distance_max):
            points_filtre.append(distance_max)

        else:
            points_filtre.append(points[i])

    #Retourner points_filtre afin de ne pas modifier points qui est l'original
    return points_filtre


def filtre_moyenne_mobile(points):
    """
    DESC: Filtre les points en remplaçant chaque point par une moyenne mobile.
          La moyenne est calculée avec une fenêtre de 3 points (le point lui-même et ceux avant et après).
          Pour les valeurs aux extrémités, seulement une fenêtre de 2 points est utilisée.
          
    RETOUR: Tableau de données filtrées
    """
    # nouvelle liste de points pour éviter de modifier l'originale
    points_filtres = []

    # itérer à travers les points
    for index in range(len(points)):
        # garder une liste des éléments à moyenner
        # l'initialiser avec l'élément correspondant à l'index actuel
        elements = [points[index]]
        # si ce n'est pas le premier élément, rajouter l'élément précédent
        if (index > 0):
            elements.append(points[index - 1])
        # si ce n'est pas le dernier élément, rajouter l'élément suivant
        if (index < (len(points) - 1)):
            elements.append(points[index + 1])

        # faire la moyenne des éléments
        moyenne = sum(elements) / len(elements)
        # ajouter le nouveau point calculé à une décimale
        if (moyenne < 10 and moyenne > 9.7): print(moyenne)
        points_filtres.append(round(moyenne, 1))

    # retourner le tableau de données filtrées
    return points_filtres


def filtre_mediane_mobile(points):
    """
    DESC: Filtre les points en remplaçant chaque point par une médiane mobile.
          La médiane est calculée avec une fenêtre de 3 points (le point lui-même et ceux avant et après).
          Pour les valeurs aux extrémités, le point original est conservé.
          
    RETOUR: Tableau de données filtrées
    """
    # nouvelle liste de points pour éviter de modifier l'originale
    points_filtres = []

    # itérer à travers les points
    for index in range(len(points)):
        # si c'est le premier ou dernier élément, garder le même point
        if ((index == 0) or (index == len(points) - 1)):
            points_filtres.append(points[index])
        # sinon, prendre en compte le point original et les points précédant et suivant
        else:
            elements = [points[index - 1], points[index], points[index + 1]]
            # organiser les éléments en ordre croissant
            elements.sort()
            # prendre la médiane (le 2e élément)
            points_filtres.append(elements[1])

    # retourner le tableau de données filtrées
    return points_filtres
