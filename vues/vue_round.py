class VueRound:
    """ Tous les inputs pour la creation d'un tour"""

    def __init__(self):
        pass

    def nom(self) -> str:
        return input("Entrer le nom du tour: ")

    def qui_gagne(self) -> int:
        return int(input("Entrer 1 si c'est le joueur de gauche qui a gagné ou 2 si c'est celui de droite: "))

    def choix_pour_classer(self):
        return int(input("Entrer 1 pour classer par classement, entrer 2 pour classer par \
ordre alphabetique. Entrer 3 pour classer par score: "))

    def afficher_debut_round(self, nom_round, date, heure):
        print(f"Le {nom_round} commence le {date}, a {heure}.")

    def afficher_fin_round(self, nom_round, date, heure):
        print(f"Le {nom_round} vient de finir le {date}, a {heure}.")

    def message_erreur(self):
        print("Le choix est invalide")
