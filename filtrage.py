"""
GRO120: Module filtrage - implémentation des filtres à appliquer sur les données lidar 

Auteurs: Vincent Duchesne
Date: 29/09/2026
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

        






    
  
    


    pass


#===========================================
# Autres fonctions à compléter...
#===========================================



