from .cartes import *
from .data import *
from .bot import *


def premierTour(joueurs, cartes, mises=None):
    """
    Sélectionne 2 cartes pour chaque joueurs
    :param dict joueurs: Dictionnaire des joueurs
    :param list cartes: La pioche
    :param dict mises: Dictionnaire des mises pouvant être nul si jeu sans mises
    :return dict: Dictionnaire de données
    """
    scores = initScores(joueurs)
    for nom_joueur in joueurs:
        pioche = piocheCarte(cartes, 2)
        print(f"Tour du joueur {nom_joueur} : {pioche}")
        for carte in pioche:
            value = valeurCarte(scores, carte, nom_joueur, joueurs)
            scores[nom_joueur][0] += value
            joueurs[nom_joueur][2] = value
        if mises is not None:
            mettreMise(scores, mises, nom_joueur, joueurs)
        scores[nom_joueur][2] += 1  # ajout nb tour
    return scores


def continu(scores, nom_joueur, joueurs):
    """
    Demande au joueur si il veut continuer de piocher des cartes
    :param dict scores: Données des joueurs
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return bool:
    """
    if estJoueurBot(nom_joueur, joueurs):
        return continuBot(scores, nom_joueur, joueurs)
    else:
        rep = input("Continuer ? (oui/non)")
        while rep != "oui" and rep != "non":
            rep = input("Continuer ? (oui/non)")
        if rep == "oui":
            return True
        else:
            return False


def tourJoueur(scores, nom_joueur, cartes, joueurs):
    """
    Gestion du tour d'un joueur
    :param dict scores: Données des joueurs
    :param str nom_joueur: Nom d'un joueur
    :param list cartes: Paquet de cartes
    :param dict joueurs: Dictionnaire des joueurs
    """
    if nom_joueur in scores and scores[nom_joueur][1]:
        scores[nom_joueur][2] += 1
        print("******************")
        print("Nom :", nom_joueur)
        print("Score :", scores[nom_joueur][0])
        print("Tour :", scores[nom_joueur][2])
        if continu(scores, nom_joueur, joueurs):
            carte = piocheCarte(cartes)[0]
            valeur = valeurCarte(scores, carte, nom_joueur, joueurs)
            scores[nom_joueur][0] += valeur
            print(carte)
            if scores[nom_joueur][0] >= 21:
                scores[nom_joueur][1] = False
        else:
            scores[nom_joueur][1] = False


def tourComplet(scores, cartes, joueurs):
    """
    Gestion des tours des joueurs
    :param dict scores: données des joueurs
    :param list cartes: paquet de cartes
    :param dict joueurs: Dictionnaire des joueurs
    """
    for nom_joueur in scores:
        tourJoueur(scores, nom_joueur, cartes, joueurs)


def partieFinie(scores):
    """
    Determine  si la partie est fini
    :param dict scores: Données des joueurs
    :return bool:
    """
    result = True
    for nom_joueur in scores:
        if scores[nom_joueur][1]:  # si le joueur est encore en jeu
            result = False
    return result


def partieComplete(scores, cartes, joueurs):
    """
    Gestion d'une partie entière
    :param dict scores: Données des joueurs
    :param list cartes: Paquet de cartes
    :param dict joueurs: Dictionnaire des joueurs
    """
    while not (partieFinie(scores)):
        tourComplet(scores, cartes, joueurs)
