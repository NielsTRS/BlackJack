import random


def mise_possible(mise, mise_init):
    return 0 < mise <= mise_init


def paquet():
    '''
    Créé un jeu de 52 cartes
    :return list: Renvoie le jeu de carte
    '''
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
    '''
    Détermine la valeur d'une carte
    :param str carte: Nom de la carte
    :return int|None: La valeure de la carte
    '''
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
    '''
    Création d'une pioche de n paquets de cartes
    :param int n: nombre de joueur
    :return list: pioche
    '''
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
    '''
    Pioche une ou plusieurs cartes dans le paquet et les enlèves de la liste
    :param list p: pioche
    :param int nb: nombre de carte(s) à piocher (1 par défaut)
    :return list: renvoie les cartes piochés
    '''
    cartes = []
    while nb >= 1:
        carte = p[0]
        cartes.append(carte)
        p.remove(p[0])
        nb -= 1
    return cartes


def initJoueurs(n):
    '''
    Récupère les noms des n joueurs
    :param int n: nombre de joueurs
    :return list: Liste des joueurs
    '''
    joueurs = []
    i = 1
    while i <= n:
        nom = input(f"Nom du joueur {i} : ")
        joueurs.append(nom)
        i += 1
    return joueurs


def initScores(joueurs, v=0):
    '''
    Initialisation des données pour les joueurs
    :param joueurs list: Liste des joueurs
    :param int v: Score de commencement
    :return dict: Dictionnaire de données
    '''
    scores = {}
    for nom_joueur in joueurs:
        scores[nom_joueur] = [v, True, 0]  # valeur de carte, encore en jeu, nombre de tour
    return scores


def initMise(joueurs, m=100):
    '''
    Initialisation de la mise de depart des joueurs
    :param joueurs list: Liste des joueurs
    :param int m: mise de commencement
    :return dict: Dictionnaire de données
    '''
    mises = {}
    for nom_joueur in joueurs:
        mises[nom_joueur] = [m, 0]  # banque, mise
    return mises


# demander pour param cartes
def premierTour(joueurs, cartes, mises):
    '''
    Selectionne 2 cartes pour chaque joueurs
    :param list joueurs: Liste des joueurs
    :param list cartes: La pioche
    :return:
    '''
    scores = initScores(joueurs)
    for nom_joueur in joueurs:
        pioche = piocheCarte(cartes, 2)
        print(f"Tour du joueur {nom_joueur} : {pioche}")
        m = int(input(f"Votre mise [1, {mises[nom_joueur][0]}] : "))
        while not mise_possible(m, mises[nom_joueur][0]):
            m = int(input(f"Votre mise [1, {mises[nom_joueur][0]}] : "))
        mises[nom_joueur][0] -= m
        mises[nom_joueur][1] = m
        for carte in pioche:
            scores[nom_joueur][0] += valeurCarte(carte)
        scores[nom_joueur][2] += 1
    return scores


# géré le cas d'égalité
def gagnant(scores):
    '''
    Détermine si il y a un gagant
    :param dict scores: Dictionnaire de données des joueurs
    :return list:
    '''
    max_score_legal = [None, 0, 1]
    for j in scores:
        if not (scores[j][1]) and max_score_legal[1] < scores[j][0] <= 21 or (
                max_score_legal[2] > scores[j][2] and max_score_legal[1] == scores[j][0]):
            max_score_legal = [j, scores[j][0], scores[j][2]]  # nom du joueur, score
    return max_score_legal[0]


# on ne peut pas utiliser le nom demander dans le document car deja pris dans python ("continue()") pour les boucles
def continu():
    '''
    Demande au joueur si il veut continuer de piocher des cartes
    :return bool:
    '''
    rep = input("Continuer ? (oui/non)")
    while rep != "oui" and rep != "non":
        rep = input("Continuer ? (oui/non)")
    if rep == "oui":
        return True
    else:
        return False


def tourJoueur(scores, j, cartes):
    '''
    Gestion du tour d'un joueur
    :param dict scores: Données des joueurs
    :param str j: Nom d'un joueur
    :param list cartes: Paquet de cartes
    :return:
    '''
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
    '''
    Gestion des tours des joueurs
    :param dict scores: données des joueurs
    :param list cartes: paquet de cartes
    :return:
    '''
    for nom in scores:
        tourJoueur(scores, nom, cartes)


def partieFinie(scores):
    '''
    Determine  si la pârtie est fini
    :param dict scores: Données des joueurs
    :return:
    '''
    result = True
    for j in scores:
        if scores[j][1]:  # si le joueur est encore en jeu
            result = False
    return result


def partieComplete(scores, cartes):
    '''
    Gestion d'une partie entière
    :param dict scores: Données des joueurs
    :param list cartes: Paquet de cartes
    :return:
    '''
    while not (partieFinie(scores)):
        tourComplet(scores, cartes)


def remiseMises(joueurs, gagnant, scores, mises):
    mise = 0
    for nom_joueur in scores:
        mise += mises[nom_joueur][1]
        mises[nom_joueur][1] = 0
        if nom_joueur != gagnant and mises[nom_joueur][0] == 0:
            joueurs.remove(nom_joueur)
            mises.pop(nom_joueur)
    mises[gagnant][0] += mise


# PROGAMME PRINCIPALE
nb_joueurs = 0
while nb_joueurs < 2:
    nb_joueurs = int(input("Nombre de joueurs : "))
rejouer = "oui"
joueurs = initJoueurs(nb_joueurs)
mises = initMise(joueurs)
while rejouer == "oui" and len(joueurs) >= 2:
    cartes = initPioche(len(joueurs))
    scores = premierTour(joueurs, cartes, mises)
    partieComplete(scores, cartes)
    vainqueur = gagnant(scores)
    if vainqueur is not None:
        remiseMises(joueurs, vainqueur, scores, mises)
        print("Le gagnant est :", vainqueur)
    else:
        print('Aucun gagant !')
    rejouer = input("Rejouer ? (oui/non)")
if len(joueurs) < 2:
    print("Il n'y a plus qu'un joueur restant ! Le vainqueur est :", joueurs[0])
print("Fin de la partie")
