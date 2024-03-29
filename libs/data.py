# INF101 - Projet BlackJack
# @copyright Terese Niels - Chognon Loïc (IMA-1)

from .bots import *


def mettreMise(scores, mises, nom_joueur, joueurs):
    """
    Fonction qui permet de mettre une mise en jeu
    :param dict scores: Données des joueurs
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    """
    if estJoueurBot(nom_joueur, joueurs):
        m = choixMiseBot(scores, mises, nom_joueur, joueurs)
    else:
        m = int(input(f"Votre mise [1, {mises[nom_joueur][0]}] : "))
        while not mise_possible(m, mises[nom_joueur][0]):
            m = int(input(f"Votre mise [1, {mises[nom_joueur][0]}] : "))
    mises[nom_joueur][0] -= m
    mises[nom_joueur][1] = m


def initScores(joueurs, v=0):
    """
    Initialisation des données pour les joueurs
    :param dict joueurs: Dictionnaire des joueurs
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
    :param dict joueurs: Dictionnaire des joueurs
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
    :param dict joueurs: Tableau des joueurs de la partie
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
                joueurs.pop(nom_joueur)
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
