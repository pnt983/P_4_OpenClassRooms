from verificateur import Verification


class VueRound:
    """ Tous les inputs pour la creation d'un tour"""

    def __init__(self):
        pass

    @Verification.verifier_input_remplit
    def nom(self) -> str:
        return input("Entrer le nom du tour: ")

    @Verification.verifier_qui_gagne
    def qui_gagne(self) -> int:
        return int(input("Entrer 1 si c'est le joueur de gauche qui a \
gagné, 2 si c'est celui de droite ou 3 en cas de match nul: "))

    def afficher_debut_round(self, nom_round, date):
        print(f"Le {nom_round} commence le {date}.")

    def afficher_fin_round(self, nom_round, date):
        print(f"Le {nom_round} vient de finir le {date}.")

    def montrer_message(self, message):
        print(message)
