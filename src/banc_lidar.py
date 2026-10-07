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
import interaction_usager
import entree_sortie
import analyse
import sys

#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """
    print("Test lidar (GRO120)")

    # 1er argument par ligne de commande est toujours le nom du script lui-même
    # s'il y a plus qu'un argument l'usager passe le nom du fichier d'entrée
    if (len(sys.argv) > 1):
        # valider le fichier d'entrée passé par ligne de commande
        fichier_entree = interaction_usager.valider_fichier_entree(sys.argv[1])
        if (fichier_entree == ""):
            print(
                "Mauvais fichier entré par ligne de commande, veuillez réessayer."
            )
    else:
        fichier_entree = ""

    while True:
        # demander le fichier d'entrée à l'utilisateur si la variable est vide
        # 1ère itération, demande de l'usager de changer d'entrée, ou paramètre de ligne de commande invalide
        if (fichier_entree == ""):
            fichier_entree = interaction_usager.demander_fichier_entree()
        fichier_sortie = interaction_usager.demander_fichier_sortie()
        choix_algo = interaction_usager.demander_choix_algo()

        # Lire le fichier d'entrée pour le convertir en tableau
        points_entree = entree_sortie.lire_fichier_entree(fichier_entree)

        # Filtrer les données d'entrée
        points_sortie = []
        if (choix_algo == 1):
            points_sortie = filtrage.filtre_min_max(points_entree)
        elif (choix_algo == 2):
            points_sortie = filtrage.filtre_moyenne_mobile(points_entree)
        elif (choix_algo == 3):
            points_sortie = filtrage.filtre_mediane_mobile(points_entree)

        # Écrire dans le fichier de sortie les données de sortie
        entree_sortie.ecrire_fichier_sortie(points_sortie, fichier_sortie)

        # Afficher à l'utilisateur les statistiques sur les données
        analyse.affiche_stats(points_sortie)

        # Afficher les instructions sur les choix pour continuer à boucler
        choix = interaction_usager.demander_suite_programme()

        if (choix == "R"):
            # fichier_entree conserve sa valeur pour la prochaine boucle
            pass
        elif (choix == "S"):
            # assigner le nouveau fichier créé au prochain fichier d'entrée
            fichier_entree = fichier_sortie
        elif (choix == "N"):
            # le programme redemandera un fichier d'entrée à la prochaine boucle
            fichier_entree = ""
        else:
            # si pas parmi ces choix, sortir de la boucle et quitter le programme
            break

        print()
