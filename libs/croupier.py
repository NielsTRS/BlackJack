import random
import numpy


def ajoutCroupier(joueurs):
    joueurs.append("croupier")


def choixMiseCroupier(v=10):
    return int(v)


def choixValeurCarteCroupier():
    return 1


def estJoueurCroupier(joueur):
    return joueur == "croupier"


def continuCroupier(scores, j):
    # result = IAContinuAleatoire()
    result = IAContinuIntelligent(scores, j)
    return result


def IAContinuAleatoire():
    return bool(random.choice([True, False]))


def IAContinuIntelligent(scores, j):
    proba = 1 - (scores[j][0] / 21)
    print(proba)
    return IAContinuProba(proba)


def IAContinuProba(proba):
    if proba == 0.5:
        return IAContinuAleatoire()
    else:
        return numpy.random.choice([True, False], p=[proba, 1 - proba])
