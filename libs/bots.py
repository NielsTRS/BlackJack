# INF101 - Projet BlackJack
# @copyright Terese Niels - Chognon Loïc (IMA-1)

import random
import numpy


def choixDifficulteIACroupier():
    """
    Demande à l'utilisateur le choix de l'IA a appliqué au croupier
    :return int: Numéro du choix
    """
    difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : intelligente, 4 : impossible) : "))
    while difficulte != 1 and difficulte != 2 and difficulte != 3 and difficulte != 4:
        difficulte = int(
            input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : intelligente, 4 : impossible) : "))
    return difficulte


def ajoutCroupier(joueurs):
    """
    Permet d'ajouter le croupier au jeu
    :param dict joueurs: Dictionnaire des joueurs
    """
    joueurs["croupier"] = [False, choixDifficulteIACroupier(), None]


def choixValeurCarte(scores, nom_joueur):
    """
    Détermine quelle valeur choisir si l'as est tiré
    :param dict scores: Dictionnaire de données
    :param str nom_joueur: Nom d'un joueur
    :return int: Valeur du choix
    """
    if scores[nom_joueur][0] + 11 <= 21:
        value = 11
    else:
        value = 1
    print("Valeur de carte AS choisi : " + str(value))
    return value


def estJoueurCroupier(nom_joueur, joueurs):
    """
    Détermine si le joueur est un bot
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return bool: Retourne True si c'est un bot, False sinon
    """
    if joueurs[nom_joueur][0] and nom_joueur == "croupier":
        return False
    else:
        return True


def estJoueurBot(nom_joueur, joueurs):
    """
    Détermine si le joueur est un bot
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return bool: Retourne True si c'est un bot, False sinon
    """
    if joueurs[nom_joueur][0]:
        return False
    else:
        return True


def choixMiseBot(scores, mises, nom_joueur, joueurs):
    """
    Fonction qui appelle la bonne IA de gestion des mises
    :param dict scores: Données des joueurs
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return int: La mise du bot
    """
    difficulte = joueurs[nom_joueur][1]
    if difficulte == 1:
        mise = IAMiseAleatoire(mises, nom_joueur)
    elif difficulte == 2:
        mise = IAMiseProba(mises, nom_joueur, scores)
    elif difficulte == 3:
        mise = IAMiseIntelligente(mises, nom_joueur, scores)
    else:
        mise = IAMiseImpossible(mises, nom_joueur)
    print(f"Mise du joueur {nom_joueur} :  {mise}")
    return mise


def IAMiseAleatoire(mises, nom_joueur):
    """
    IA de mise stupide (mode aléatoire)
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :return int: La mise
    """
    return random.randint(0, mises[nom_joueur][0])


def IAMiseProba(mises, nom_joueur, scores):
    """
    IA de mise (mode proba)
    :param dict scores: Données des joueurs
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :return int: La mise
    """
    proba = (scores[nom_joueur][0] / 21)
    mise = round(mises[nom_joueur][0] * proba)
    return mise


def IAMiseIntelligente(mises, nom_joueur, scores):
    """
    IA de mise (mode intelligente)
    :param dict scores: Données des joueurs
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :return int: La mise
    """
    if scores[nom_joueur][0] == 21:
        pourcentage = 0.9
    else:
        pourcentage = 0.1
    return round(pourcentage * mises[nom_joueur][0])


def IAMiseImpossible(mises, nom_joueur):
    """
    IA de mise (mode impossible)
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :return int: La mise
    """
    return round((9 / 10) * mises[nom_joueur][0])


def continuBot(scores, nom_joueur, joueurs):
    """
    Fonction qui appelle la bonne IA de gestion de continuation
    :param dict scores: Données des joueurs
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return bool: True pour continuer, False sinon
    """
    difficulte = joueurs[nom_joueur][1]
    if difficulte == 1:
        continu = IAContinuAleatoire()
    elif difficulte == 2:
        continu = IAContinuProba(scores, nom_joueur)
    elif difficulte == 3:
        continu = IAContinuIntelligente(scores, nom_joueur, joueurs)
    else:
        continu = IAContinuImpossible()
    return continu


# IA FACILE (1)
def IAContinuAleatoire():
    """
    IA pour décider si il faut continuer de jouer (mode aleatoire)
    :return bool: True pour continuer, False sinon
    """
    return bool(random.choice([True, False]))


# IA MOYENNE (2)
def IAContinuProba(scores, nom_joueur, proba=None):
    """
    IA pour décider si il faut continuer de jouer (mode proba)
    :param dict scores: Données des joueurs
    :param str nom_joueur: Nom d'un joueur
    :param int|None proba: Probabilité à affecter
    :return bool: True pour continuer, False sinon
    """
    if proba is None:
        value = 1 - (scores[nom_joueur][
                         0] / 21)  # probabilité de continuer en fonction de son score, si score = 0, proba = 1, si score = 21, proba = 0
    else:
        value = proba
    if value == 0.5:
        return IAContinuAleatoire()
    else:
        return numpy.random.choice([True, False], p=[value, 1 - value])


# IA INTELLIGENTE (3)
def IAContinuIntelligente(scores, nom_joueur, joueurs):
    """
    IA pour décider si il faut continuer de jouer (mode intelligent)
    :param dict scores: Données des joueurs
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return bool: True pour continuer, False sinon
    """
    mon_score = scores[nom_joueur][0]
    if 0 <= mon_score <= 11:
        return True
    elif 18 <= mon_score <= 21:
        return False
    else:
        carte = -1
        for joueur in joueurs:
            if estJoueurCroupier(joueur, joueurs):
                carte = joueurs[joueur][2]  # deuxième carte du croupier
        if carte == -1:  # si il n'y a plus de croupier
            # for joueur in joueurs:
            #     if carte < joueurs[joueur][2]:
            #         carte = joueurs[joueur][2]
            return IAContinuProba(scores, nom_joueur)
        if mon_score == 12:
            if 4 <= carte <= 6:
                return False
            else:
                return True
        else:
            if 2 <= carte <= 6:
                return False
            else:
                return True


def IAContinuImpossible():
    return False
