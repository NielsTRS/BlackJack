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
while rejouer == "oui" and len(joueurs) >= 2:
    # initalisation de la pioche
    cartes = initPioche(len(joueurs))

    # gestion de la partie
    scores = premierTour(joueurs, cartes, mises)
    partieComplete(scores, cartes, joueurs)
    vainqueur = gagnant(scores)

    if vainqueur is not None:
        # remise des prix si il le jeu est avec des mises
        remiseMises(joueurs, vainqueur, scores, mises)
        print("######################")
        print("Le gagnant est :", vainqueur)
    else:
        print("######################")
        print('Aucun gagant !')

    print("######################")
    rejouer = input("Rejouer ? (oui/non)")

if len(joueurs) < 2:
    vainqueur = ""
    for j in joueurs:
        vainqueur = j
    print("Il n'y a plus qu'un joueur restant ! Le vainqueur est :", vainqueur)
print("Fin de la partie")
