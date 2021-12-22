class CreationRound:
    """ Tous les inputs pour la creation d'un tour"""

    def __init__(self):
        pass

    def nom(self) -> str:
        return input("Entrer le nom du tour: ")

    def qui_gagne(self) -> int:
        return int(input("Entrer 1 si c'est le joueur de gauche qui a gagné ou 2 si c'est celui de droite: "))

    def choix_pour_classer(self):
        return int(input("Pour classer par classement, entrer \
1. Par ordre alphabetique, entrer 2. Par score, entrer 3: "))
