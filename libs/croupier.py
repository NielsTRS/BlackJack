import random
import numpy


def choixDifficulteIACroupier():
    difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : forte) : "))
    while difficulte != 1 and difficulte != 2 and difficulte != 3:
        difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : forte) : "))
    return difficulte


def ajoutCroupier(joueurs):
    joueurs["croupier"] = [False, choixDifficulteIACroupier()]


def choixMiseCroupier(scores, mises, j):
    proba = (scores[j][0] / 21)
    mise = round(mises[j][0] * proba)
    return mise


def choixValeurCarteCroupier(scores, j):
    if scores[j][0] + 11 <= 21:
        return 11
    else:
        return 1


def estJoueurCroupier(joueur):
    return joueur == "croupier"


def continuCroupier(scores, j, joueurs):
    difficulte = joueurs[j][1]
    if difficulte == 1:
        print("Aleatoire")
        return IAContinuAleatoire()
    elif difficulte == 2:
        print("Moyenne")
        return IAContinuIntelligent(scores, j)
    else:
        return IAContinuMasterClass()


# IA FACILE (1)
def IAContinuAleatoire():
    return bool(random.choice([True, False]))


# IA MOYENNE (2)
def IAContinuIntelligent(scores, j):
    proba = 1 - (scores[j][
                     0] / 21)  # probabilité de continuer en fonction de son score, si score = 0, proba = 1, si score = 21, proba = 0
    return IAContinuProba(proba)


def IAContinuProba(proba):
    if proba == 0.5:
        return IAContinuAleatoire()
    else:
        return numpy.random.choice([True, False], p=[proba, 1 - proba])


# IA INTELLIGENTE (3)
def IAContinuMasterClass():
    # faire IA
    return False
