from .croupier import *


def mettreMise(scores, mises, joueur):
    if estJoueurCroupier(joueur):
        m = choixMiseCroupier(scores, mises, joueur)
    else:
        m = int(input(f"Votre mise [1, {mises[joueur][0]}] : "))
        while not mise_possible(m, mises[joueur][0]):
            m = int(input(f"Votre mise [1, {mises[joueur][0]}] : "))
    mises[joueur][0] -= m
    mises[joueur][1] = m


def initScores(joueurs, v=0):
    """
    Initialisation des données pour les joueurs
    :param list joueurs: Liste des joueurs
    :param int v: Score de commencement
    :return dict: Dictionnaire de données
    """
    scores = {}
    for nom_joueur in joueurs:
        scores[nom_joueur] = [v, True, 0]  # valeur de carte, encore en jeu, nombre de tour
    return scores


def initMise(joueurs, m=100, jouerAvecMise=True):
    """
    Initialisation de la mise de depart des joueurs
    :param list joueurs: Liste des joueurs
    :param int m: mise de commencement
    :param bool jouerAvecMise: Partie avec ou sans mises
    :return dict|None: Dictionnaire de données ou rien
    """
    if jouerAvecMise:
        mises = {}
        for nom_joueur in joueurs:
            mises[nom_joueur] = [m, 0]  # banque, mise
        return mises
    else:
        return None


def remiseMises(joueurs, gagnant, scores, mises):
    """
    Attribut les mises aux joueurs si le jeu est avec des mises
    :param list joueurs: Tableau des joueurs de la partie
    :param str gagnant: Nom du gagnant
    :param dict scores: Dictionnaire de données
    :param dict mises: Dictionnaire des mises
    """
    if mises is not None:
        mise = 0
        for nom_joueur in scores:
            mise += mises[nom_joueur][1]
            mises[nom_joueur][1] = 0
            if nom_joueur != gagnant and mises[nom_joueur][0] == 0:
                joueurs.remove(nom_joueur)
                mises.pop(nom_joueur)
        mises[gagnant][0] += mise


def mise_possible(mise, mise_init):
    """
    Détermine si le joueur peut miser une certaine somme
    :param int mise: Somme que l'utilisateur veut miser
    :param mise_init: Banque de l'utilisateur
    :return bool:
    """
    return 0 < mise <= mise_init


def jouerAvecMises():
    """
    Demande si le jeu sera avec des mises
    :return bool:
    """
    rep = input('Jouer avec des mises ? (oui/non)')
    while rep != "oui" and rep != "non":
        rep = input('Jouer avec des mises ? (oui/non)')
    if rep == "oui":
        return True
    else:
        return False
