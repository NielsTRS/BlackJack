import random
import numpy


def choixDifficulteIACroupier():
    """
    Demande à l'utilisateur le choix de l'IA a appliqué au croupier
    :return int: Numéro du choix
    """
    difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : intelligente, 4 : impossible) : "))
    while difficulte != 1 and difficulte != 2 and difficulte != 3 and difficulte != 4:
        difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : intelligente, 4 : impossible) : "))
    return difficulte


def ajoutCroupier(joueurs):
    """
    Permet d'ajouter le croupier au jeu
    :param dict joueurs: Dictionnaire des joueurs
    """
    joueurs["croupier"] = [False, choixDifficulteIACroupier()]


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
        mise = IAMiseIntelligent(scores, mises, nom_joueur)
    else:
        mise = IAContinuMasterClass()
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


def IAMiseProba(scores, mises, nom_joueur):
    """
    IA de mise intelligente (mode proba)
    :param dict scores: Données des joueurs
    :param dict mises: Dictionnaire des mises
    :param str nom_joueur: Nom d'un joueur
    :return int: La mise
    """
    proba = (scores[nom_joueur][0] / 21)
    mise = round(mises[nom_joueur][0] * proba)
    return mise


def continuBot(scores, nom_joueur, joueurs):
    """
    Fonction qui appelle la bonne IA de gestion de continuation
    :param dict scores: Données des joueurs
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return:
    """
    difficulte = joueurs[nom_joueur][1]
    if difficulte == 1:
        continu = IAContinuAleatoire()
    elif difficulte == 2:
        continu = IAContinuProba(scores, nom_joueur)
    else:
        continu = IAContinuMasterClass()
    return continu


# IA FACILE (1)
def IAContinuAleatoire():
    return bool(random.choice([True, False]))


# IA MOYENNE (2)
def IAContinuProba(scores, nom_joueur):
    proba = 1 - (scores[nom_joueur][
                     0] / 21)  # probabilité de continuer en fonction de son score, si score = 0, proba = 1, si score = 21, proba = 0
    return proba(proba)


def proba(proba):
    if proba == 0.5:
        return IAContinuAleatoire()
    else:
        return numpy.random.choice([True, False], p=[proba, 1 - proba])


# IA INTELLIGENTE (3)
def IAContinuMasterClass():
    # faire IA
    return False
