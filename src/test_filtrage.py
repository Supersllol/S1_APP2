"""
GRO120: Tests unitaires pour le module filtrage

Auteur: Francois Ferland
Date: 18/09/2025

Modifié par: Simon Lacroix et Vincent Duchesne
Date: 07/10/2026
"""

import filtrage


#===========================================
def test_filtre_min_max():
    """
    DESC: Teste la fonction filtre_min_max
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs minimum et maximum spécifiées 
    """

    donnees = [1, 50, 0]
    reponse = [1, 10, -1]
    test = filtrage.filtre_min_max(donnees, 1, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = []
    reponse = []
    test = filtrage.filtre_min_max(donnees, 1, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [0]
    reponse = [-1]
    test = filtrage.filtre_min_max(donnees, 1, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [
        -234.234, 123456.4, 10
    ]  #dire dans le rapport que meme si n'est pas un cas qu'on va avoir on test les limite du code
    reponse = [-1, 10, 10]
    test = filtrage.filtre_min_max(donnees, 1, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [-1, -50, 0]
    reponse = [-1, -1, 0]
    test = filtrage.filtre_min_max(donnees, 0, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [1, -1, -10, 0, 19]
    reponse = [1, -1, -1, -1, 1]
    test = filtrage.filtre_min_max(donnees, 1, 1)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [-1, 50, 0, 5]
    reponse = [-1, 10.6, -1, 5]
    test = filtrage.filtre_min_max(donnees, 1.2, 10.6)
    assert test == reponse, f"Erreur: {test} != {reponse}"


def tests_filtre_moyenne_mobile():
    """
        DESC: Test la fonction filtre_moyenne_mobile
        
        NOTE: Je ne sais pas quoi mettre ici ########################################################### 
        """
    donnees = [1, 3, 2, 4, 5, 3]
    reponse = [2.0, 2.0, 3.0, 3.7, 4.0, 4.0]
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = []
    reponse = []
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [0]
    reponse = [0]
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [3, 3]
    reponse = [3, 3]
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [1.2, 1.6, 45.6]
    reponse = [1.4, 16.1, 23.6]
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [-1]
    reponse = [-1]
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [-1, 2, 7, 0]
    reponse = [0.5, 2.7, 3, 3.5]
    test = filtrage.filtre_moyenne_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"


def tests_filtre_mediane_mobile():

    donnees = [-1, 2, 7, 0]
    reponse = [-1, 2, 2, 0]
    test = filtrage.filtre_mediane_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = []
    reponse = []
    test = filtrage.filtre_mediane_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [0]
    reponse = [0]
    test = filtrage.filtre_mediane_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [1, 2, 3, 4, 5]
    reponse = [1, 2, 3, 4, 5]
    test = filtrage.filtre_mediane_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [-1, 0, 9.5, 5.6, 7, 4, -1]
    reponse = [-1, 0, 5.6, 7, 5.6, 4, -1]
    test = filtrage.filtre_mediane_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [0, 1, 1, 0]
    reponse = [0, 1, 1, 0]
    test = filtrage.filtre_mediane_mobile(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"


#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """
    test_filtre_min_max()
    tests_filtre_moyenne_mobile()
    tests_filtre_mediane_mobile()

    print("Tous les tests ont réussi.")
