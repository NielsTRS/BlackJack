from libs.joueurs import *
from libs.partie import *
from libs.bot import *

# demande le nombre de joueur
nb_joueurs = 0
while nb_joueurs < 1:
    nb_joueurs = int(input("Nombre de joueurs : "))

# initialisation des données
joueurs = initJoueurs(nb_joueurs)
ajoutCroupier(joueurs)
jouer_mise = jouerAvecMises()
mises = initMise(joueurs, jouerAvecMise=jouer_mise)

# bouclage pour rejouer tant que la réponse est "oui" et tant qu'il y a plus de 2 joueurs
rejouer = "oui"
stats = {}
nb_partie = 0
while rejouer == "oui" and len(joueurs) >= 2:
    # initalisation de la pioche
    cartes = initPioche(len(joueurs))

    # gestion de la partie
    scores = premierTour(joueurs, cartes, mises)
    partieComplete(scores, cartes, joueurs)
    vainqueur = gagnant(scores)
    nb_partie += 1
    if vainqueur is not None:
        if vainqueur in stats:
            stats[vainqueur] += 1
        else:
            stats[vainqueur] = 1
        # remise des prix si il le jeu est avec des mises
        remiseMises(joueurs, vainqueur, scores, mises)
        print("######################")
        print("Le gagnant est :", vainqueur)
    else:
        print("######################")
        print('Aucun gagant !')

    print("######################")
    queBots = True
    for j in joueurs:
        if not estJoueurBot(j, joueurs):
            queBots = False
    if queBots:
        if nb_partie < 10000:
            rejouer = "oui"
        else:
            rejouer = "non"
    else:
        rejouer = input("Rejouer ? (oui/non)")
        while rejouer != "oui" and rejouer != "non":
            rejouer = input("Rejouer ? (oui/non)")
print(stats)
if len(joueurs) < 2:
    print("Il n'y a plus qu'un joueur restant ! Le vainqueur est :", list(joueurs.keys())[0])
print("Fin de la partie")
