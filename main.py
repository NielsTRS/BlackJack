import random


def paquet():
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


def valeurCarte(carte):
    if carte in paquet():
        id = carte.split()[0]
        if id == "as":
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


def piocheCarte(p, nb=1):
    cartes = []
    while nb >= 1:
        carte = p[0]
        cartes.append(carte)
        p.remove(p[0])
        nb -= 1
    return cartes


def initJoueurs(n):
    joueurs = []
    i = 1
    while i <= n:
        nom = input(f"Nom du joueur {i} : ")
        joueurs.append(nom)
        i += 1
    return joueurs


def initScores(joueurs, v=0):
    scores = {}
    for joueur in joueurs:
        scores[joueur] = v
    return scores


def premierTour(joueurs):
    scores = initScores(joueurs)
    cartes = initPioche(len(joueurs))
    for joueur in joueurs:
        pioche = piocheCarte(cartes, 2)
        print(f"Tour du joueur {joueur} : {pioche}")
        for carte in pioche:
            scores[joueur] += valeurCarte(carte)
    return scores


def gagnant(scores):
    max_score_legal = [None, 0]
    for joueur in scores:
        if max_score_legal[1] < scores[joueur] <= 21:
            max_score_legal = [joueur, scores[joueur]]
    return max_score_legal


joueurs = initJoueurs(2)
tour = premierTour(joueurs)
print(gagnant(tour))
