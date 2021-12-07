import random
import numpy


def choixDifficulteIACroupier():
    difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : forte) : "))
    while difficulte != 1 and difficulte != 2 and difficulte != 3:
        difficulte = int(input(f"Choix de l'IA du croupier (1 : faible, 2 : moyenne, 3 : forte) : "))
    return difficulte


def ajoutCroupier(joueurs):
    joueurs["croupier"] = [False, choixDifficulteIACroupier()]


def choixValeurCarte(scores, j):
    if scores[j][0] + 11 <= 21:
        value = 11
    else:
        value = 1
    print("Valeur de carte AS choisi : " + str(value))
    return value


def estJoueurBot(joueur, joueurs):
    if joueurs[joueur][0]:
        return False
    else:
        return True


def choixMiseBot(scores, mises, j, joueurs):
    difficulte = joueurs[j][1]
    if difficulte == 1:
        mise = IAMiseAleatoire(mises, j)
    elif difficulte == 2:
        mise = IAMiseIntelligent(scores, mises, j)
    else:
        mise = IAContinuMasterClass()
    print(f"Mise du joueur : {j} :  {mise}")
    return mise


def IAMiseAleatoire(mises, j):
    return random.randint(0, mises[j][0])


def IAMiseIntelligent(scores, mises, j):
    proba = (scores[j][0] / 21)
    mise = round(mises[j][0] * proba)
    return mise


def continuBot(scores, j, joueurs):
    difficulte = joueurs[j][1]
    if difficulte == 1:
        continu = IAContinuAleatoire()
    elif difficulte == 2:
        continu = IAContinuIntelligent(scores, j)
    else:
        continu = IAContinuMasterClass()
    return continu


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
