# INF101 - Projet BlackJack
# @copyright Terese Niels - Chognon Loïc (IMA-1)

from .bots import *


def paquet():
    """
    Créé un jeu de 52 cartes
    :return list: Renvoie le jeu de carte
    """
    cartes = []
    types = ["pique", "carreau", "trefle", "coeur"]
    for card in range(1, 14):
        for type in types:
            if card == 1:
                text = "as de " + type
            elif card == 11:
                text = "valet de " + type
            elif card == 12:
                text = "dame de " + type
            elif card == 13:
                text = "roi de " + type
            else:
                text = str(card) + " de " + type
            cartes.append(text)
    return cartes


def valeurCarte(scores, carte, nom_joueur, joueurs):
    """
    Détermine la valeur d'une carte
    :param dict scores: Données des joueurs
    :param str carte: Nom de la carte
    :param str nom_joueur: Nom d'un joueur
    :param dict joueurs: Dictionnaire des joueurs
    :return int|None: La valeur de la carte
    """
    if carte in paquet():
        id = carte.split()[0]
        if id == "as":
            if estJoueurBot(nom_joueur, joueurs):
                valeur = choixValeurCarte(scores, nom_joueur)
            else:
                valeur = 0
                while valeur != 1 and valeur != 11:
                    valeur = int(input("Valeur voulue (1 ou 11) ?"))
            return valeur
        elif id == "valet" or id == "dame" or id == "roi":
            return 10
        else:
            return int(id)
    else:
        return None


def initPioche(n):
    """
    Création d'une pioche de n paquets de cartes
    :param int n: nombre de joueur
    :return list: pioche
    """
    n_cartes = []
    while n > 0:
        cartes = paquet()
        taille = len(cartes)
        while taille > 0:
            rand_index_card = random.randint(0, taille - 1)
            n_cartes.append(cartes[rand_index_card])
            cartes.pop(rand_index_card)
            taille -= 1
        n -= 1
    return n_cartes


def piocheCarte(pioche, nb=1):
    """
    Pioche une ou plusieurs cartes dans le paquet et les enlèves de la liste
    :param list pioche: pioche
    :param int nb: nombre de carte(s) à piocher (1 par défaut)
    :return list: renvoie les cartes piochés
    """
    cartes = []
    while nb >= 1:
        carte = pioche[0]
        cartes.append(carte)
        pioche.remove(pioche[0])
        nb -= 1
    return cartes
