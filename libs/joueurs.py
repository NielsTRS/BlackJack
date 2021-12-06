def initJoueurs(n):
    """
    Récupère les noms des n joueurs
    :param int n: nombre de joueurs
    :return list: Liste des joueurs
    """
    joueurs = {}
    i = 1
    while i <= n:
        nom = input(f"Nom du joueur {i} : ")
        while nom.lower() == "croupier" or nom in joueurs:
            nom = input(f"Impossible de prendre ce nom, Nom du joueur {i} : ")
        humain = input(f"Ce joueur est humain ? (oui/non)")
        while humain != "oui" and humain != "non":
            humain = input(f"Ce joueur est humain ? (oui/non)")
        if humain == "oui":
            joueurs[nom] = [True]
        else:
            difficulte = int(input(f"Choix de l'IA pour ce joueur (1 : faible, 2 : moyenne, 3 : forte) : "))
            while difficulte != 1 and difficulte != 2 and difficulte != 3:
                difficulte = int(input(f"Choix de l'IA pour ce joueur (1 : faible, 2 : moyenne, 3 : forte) : "))
            joueurs[nom] = [False, difficulte]
        i += 1
    return joueurs


def gagnant(scores):
    """
    Détermine si il y a un gagant
    :param dict scores: Dictionnaire de données des joueurs
    :return str: Nom du gagnant
    """
    max_score_legal = [None, 0, 1]
    for j in scores:
        if not (scores[j][1]) and max_score_legal[1] < scores[j][0] <= 21 or (
                max_score_legal[2] > scores[j][2] and max_score_legal[1] == scores[j][0]):
            max_score_legal = [j, scores[j][0], scores[j][2]]  # nom du joueur, score, nombre de tour
    return max_score_legal[0]
