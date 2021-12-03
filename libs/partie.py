from .cartes import *
from .data import *
from .croupier import *


def premierTour(joueurs, cartes, mises=None):
    """
    Sélectionne 2 cartes pour chaque joueurs
    :param list joueurs: Liste des joueurs
    :param list cartes: La pioche
    :param dict mises: Dictionnaire des mises pouvant être nul si jeu sans mises
    :return dict: Dictionnaire de données
    """
    scores = initScores(joueurs)
    for nom_joueur in joueurs:
        pioche = piocheCarte(cartes, 2)
        print(f"Tour du joueur {nom_joueur} : {pioche}")
        if mises is not None:
            mettreMise(mises, nom_joueur)
        for carte in pioche:
            scores[nom_joueur][0] += valeurCarte(carte, nom_joueur)
        scores[nom_joueur][2] += 1  # ajout nb tour
    return scores


def continu(j):
    """
    Demande au joueur si il veut continuer de piocher des cartes
    :return bool:
    """
    if estJoueurCroupier(j):
        return continuCroupier()
    else:
        rep = input("Continuer ? (oui/non)")
        while rep != "oui" and rep != "non":
            rep = input("Continuer ? (oui/non)")
        if rep == "oui":
            return True
        else:
            return False


def tourJoueur(scores, j, cartes):
    """
    Gestion du tour d'un joueur
    :param dict scores: Données des joueurs
    :param str j: Nom d'un joueur
    :param list cartes: Paquet de cartes
    """
    if j in scores and scores[j][1]:
        scores[j][2] += 1
        print("******************")
        print("Nom :", j)
        print("Score :", scores[j][0])
        print("Tour :", scores[j][2])
        if continu(j):
            carte = piocheCarte(cartes)[0]
            valeur = valeurCarte(carte, j)
            scores[j][0] += valeur
            print(carte)
            if scores[j][0] >= 21:
                scores[j][1] = False
        else:
            scores[j][1] = False


def tourComplet(scores, cartes):
    """
    Gestion des tours des joueurs
    :param dict scores: données des joueurs
    :param list cartes: paquet de cartes
    """
    for nom in scores:
        tourJoueur(scores, nom, cartes)


def partieFinie(scores):
    """
    Determine  si la partie est fini
    :param dict scores: Données des joueurs
    :return bool:
    """
    result = True
    for j in scores:
        if scores[j][1]:  # si le joueur est encore en jeu
            result = False
    return result


def partieComplete(scores, cartes):
    """
    Gestion d'une partie entière
    :param dict scores: Données des joueurs
    :param list cartes: Paquet de cartes
    """
    while not (partieFinie(scores)):
        tourComplet(scores, cartes)