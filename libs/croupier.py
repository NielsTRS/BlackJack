def ajoutCroupier(joueurs):
    joueurs.append("croupier")


def choixMiseCroupier(v=10):
    return int(v)


def choixValeurCarteCroupier():
    return 1


def estJoueurCroupier(joueur):
    return joueur == "croupier"


def continuCroupier():
    return True


def IAContinuAleatoire():
    return False


def IAContinuProba():
    return False
