INF101 - Projet BlackJack
@copyright Terese Niels - Chognon Loïc (IMA-1)

Le programme a été diviser en plusieurs fichiers sous formes de librairies. On lance le jeu en exécutant le fichier principal : main.py
On utilise dans notre projet les librairies déjà existantes suivantes :
- random
- numpy

° Pour commencer, nous avons respecté les règles du BlackJack indiquées sur le sujet.
Les parties du jeu qui ont été programmées sont :
- le jeu principal
- le jeu avec ou sans mises
- l'IA est sur 3 niveaux (Facile : aléatoire, Moyen : probabilité, Intelligent : stratégie vue sur internet)
- statistique en fin de partie comptant le nombre de victoires de chaque joueur

° Règles:
- choix du nombre de joueurs
- choix si le joueur est humain ou bot
- choix de mise ou non
- choix de la difficulté du croupier (obligation de presence du croupier)
- donc possibilité de faire jouer un ou plusieurs bots contre le croupier
- a chaque partie, selection de la mise (il n'y a pas de surmise)
- possibilité continuer la partie ou non : si continuation, récupération d'une carte supplémentaire
- fin de partie lorsque : tous les joueurs ont décidé d'arrêter de jouer ou ne peuvent plus jouer
- vainqueur : celui qui a le plus grand nombre inférieur ou égal à 21 (si tous les joueurs dépassent 21, il n'y a aucun vainqueur)
- cas d'égalité :
    - de score : le vainqueur est celui qui a le moins de tour
    - de score + tour : le vainqueur est le premier qui est arrivé en jeu
- possibilité de rejouer en gardant les mises et les noms des joueurs des parties précédentes

° Pour les tests :
Chaque fonction a été testée séparément via la console python.
Puis le code principal mettant en commun toutes les fonctions a été testés à de nombreuses reprises

° Repartition du travail :
Pour plus de facilité, nous avons décidé de travailler à l'aide de GIT, avec un repository privé synchronisé sur le site github.com.
La majorité du programme et de la documentation a été fait par Niels
Loïc a décidé de séparer le code en plusieurs fichiers afin d'augmenter la lisibilité.
Il a également travaillé sur l'élaboration de l'IA "Intelligente" mais nous avons a la fin décider de trouver une stratégie sur Wikipédia.
Les tests et verification du respect des règles du BlackJack ont été majoritairement réaliser par Loïc
