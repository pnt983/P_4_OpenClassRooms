from utilitaires.verificateur import Verification


class VueRound:
    """ Tous les inputs pour la creation d'un tour"""

    def __init__(self):
        pass

    @classmethod
    @Verification.verifier_input_remplit
    def creer_nom_round(cls) -> str:
        return input("Entrer le nom du tour: ")

    @classmethod
    @Verification.verifier_qui_gagne
    def entrer_resultat(cls) -> int:
        return int(input("Entrer 1 si c'est le joueur de gauche qui a \
gagné, 2 si c'est celui de droite ou 3 en cas de match nul: "))

    @classmethod
    def afficher_debut_round(cls, nom_round, date):
        print(f"Le {nom_round} commence le {date}.")

    @classmethod
    def montrer_message(cls, message):
        print(message)

    @classmethod
    def afficher_les_matchs(cls, liste_des_matchs):
        for match in liste_des_matchs:
            print(match)
