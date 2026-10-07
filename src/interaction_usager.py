"""
GRO120: Gestion de l'interaction avec l'usager pour le filtrage de données lidar

Auteurs: Simon Lacroix et Vincent Duchesne
Date: 07/10/2026
"""

import os


def valider_fichier_entree(fichier):
    """
    DESC: Fonction qui vérifie si le nom de fichier local entré par l'utilisateur est valide, en
    s'assurant qu'il existe dans le répertoire d'entrée du programme.
    Le répertoire d'entrée est nommé "entree" et est placé au même niveau que le répertoire "src".

    RETOUR: Chemin du fichier dans le répertoire d'entrée s'il est valide, chaîne vide sinon.
    """
    # modifier la valeur entrée pour prendre en compte l'organisation des dossiers
    # retourner au parent du dossier du script, pour aller chercher dans le répertoire entree
    fichier = os.path.dirname(os.path.dirname(__file__)) + "/entree/" + fichier
    # si le fichier existe à cet endroit, retourner la valeur
    if (os.path.exists(fichier)):
        return fichier
    # sinon, retourner une chaîne vide pour signifier que c'est invalide
    return ""


def demander_fichier_entree():
    """
    DESC: Fonction qui demande à l'utilisateur le nom du fichier d'entrée, et qui 
    redemande jusqu'à ce qu'il entre le nom d'un fichier valide.

    RETOUR: Nom du fichier d'entrée.
    """
    # Boucler tant que la valeur entrée n'est pas valide
    while True:
        # demander un fichier d'entrée à l'utilisateur
        print(
            "Le fichier d'entrée doit être situé dans le répertoire 'entree', "
            + "au même niveau que le dossier parent de ce script.")
        fichier = input("Veuillez entrer le nom du fichier texte d'entrée: ")

        # si le fichier est valide, retourner la valeur
        fichier = valider_fichier_entree(fichier)
        if (fichier != ""):
            return fichier
        # sinon, recommencer la boucle
        else:
            print("Ce nom de fichier est invalide, veuillez réessayer.")


def demander_fichier_sortie():
    """
    DESC: Fonction qui demande à l'utilisateur le nom du fichier de sortie. 
    Il sera placé dans le répertoire de sortie du programme.

    RETOUR: Nom du fichier de sortie, placé dans le répertoire de sortie.
    """
    # Demander le nom du fichier de sortie et le placer dans le bon répertoire
    fichier = input(
        "Veuillez entrer le nom du fichier de sortie, sans extension: ")

    # si l'usager a entré une extension (avec un point), l'enlever
    index_pt = fichier.find(".")
    if (index_pt != -1):
        fichier = fichier[:index_pt]

    # le répertoire de sortie est au même niveau que le répertoire contenant le script
    repertoire_sortie = os.path.dirname(os.path.dirname(__file__)) + "/sortie/"
    # retourner le nom du fichier dans le bon répertoire, avec l'extension .txt
    return repertoire_sortie + fichier + ".txt"


def demander_choix_algo():
    """
    DESC: Fonction qui demande à l'utilisateur le type d'algorithme à utiliser. 
    Redemande jusqu'à ce qu'un choix valide soit entré.

    RETOUR: Chiffre qui correspond au choix d'algorithme (1 pour min-max, 2 pour
    moyenne mobile, 3 pour médiane mobile).
    """
    # Boucler tant que la valeur entrée n'est pas valide
    while True:
        # Prendre le choix de l'utilisateur
        print("Veuillez entrer l'algorithme choisi:")
        print("""\t1 - min-max\n\t2 - moyenne mobile\n\t3 - médiane mobile""")
        choix = input()
        try:
            # Essayer de le convertir en int
            num_choix = int(choix)
            # Si c'est un chiffre valide (1, 2, ou 3), le retourner
            if (num_choix >= 1 and num_choix <= 3):
                return num_choix
            # Si hors des limites, redemander
            else:
                print("Veuillez entrer un chiffre entre 1 et 3.")
        # S'il y a un problème lors de la conversion en int, redemander
        except:
            print("Veuillez entrer un choix valide.")


def demander_suite_programme():
    """
    DESC: Demande à l'utilisateur ce qu'il souhaite continuer l'exécution du programme.

    RETOUR: Le caractère entré par l'utilisateur, en majuscule. Signification:
    R -> réutiliser le même fichier d'entrée
    S -> utiliser le dernier fichier de sortie comme entrée
    N -> utiliser un nouveau fichier d'entrée
    Autre -> quitter le programme
    """
    print("\nContinuer l'exécution du programme?")
    userInput = input(
        "\tR pour réutiliser le même fichier d'entrée\n" +
        "\tS pour utiliser le dernier fichier de sortie comme entrée\n" +
        "\tN pour utiliser un nouveau fichier d'entrée\n" +
        "\tAutre pour quitter\n")

    # en majuscules pour simplifier le traitement de données
    return userInput.upper()
