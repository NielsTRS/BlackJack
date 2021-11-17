import random


def mise_possible(mise, mise_init):
    while mise < 0 and mise > mise_init:
        mise = int(input("mise impossible.Donnez une autre mise:"))
    return mise


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
    for nom_joueur in joueurs:
        scores[nom_joueur] = [v, True, 0]  # valeur de carte, encore en jeu, nombre de tour
    return scores


# demander pour param cartes
def premierTour(joueurs, cartes):
    scores = initScores(joueurs)
    for nom_joueur in joueurs:
        pioche = piocheCarte(cartes, 2)
        print(f"Tour du joueur {nom_joueur} : {pioche}")
        for carte in pioche:
            scores[nom_joueur][0] += valeurCarte(carte)
        scores[nom_joueur][2] += 1
    return scores


def gagnant(scores):  # géré le cas d'égalité
    max_score_legal = [None, 0]
    for j in scores:
        if max_score_legal[1] < scores[j][0] <= 21:
            max_score_legal = [j, scores[j][0]]
    return max_score_legal


def continu():  # on ne peut pas utiliser le nom demander dans le document car deja pris dans python ("continue()") pour les boucles
    rep = input("Continuer ? (oui/non)")
    while rep != "oui" and rep != "non":
        rep = input("Continuer ? (oui/non)")
    if rep == "oui":
        return True
    else:
        return False


def tourJoueur(scores, j, cartes):
    if j in scores and scores[j][1]:
        scores[j][2] += 1
        print("Nom :", j)
        print("Score :", scores[j][0])
        print("Tour :", scores[j][2])
        if continu():
            carte = piocheCarte(cartes)[0]
            valeur = valeurCarte(carte)
            scores[j][0] += valeur
            print(carte)
            if scores[j][0] >= 21:
                scores[j][1] = False
        else:
            scores[j][1] = False


def tourComplet(scores, cartes):
    for nom in scores:
        tourJoueur(scores, nom, cartes)


def partieFinie(scores):
    result = True
    for j in scores:
        if scores[j][1]:
            result = False
    return result


def partieComplete(scores, cartes):
    while not (partieFinie(scores)):
        tourComplet(scores, cartes)


# PROGAMME PRINCIPALE
nb_joueurs = 0
while nb_joueurs < 2:
    nb_joueurs = int(input("Nombre de joueurs : "))
rejouer = "oui"
joueurs = initJoueurs(nb_joueurs)
while rejouer == "oui":
    cartes = initPioche(len(joueurs))
    scores = premierTour(joueurs, cartes)
    partieComplete(scores, cartes)
    print(scores)
    print(gagnant(scores))
    rejouer = input("Rejouer ? (oui/non)")
print("Fin de la partie")
