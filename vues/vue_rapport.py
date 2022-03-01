from utilitaires.verificateur import Verification


class VueRapport:

    def __init__(self):
        pass

    @classmethod
    @Verification.verifier_alphabetique_ou_classement
    def choisir_alphabetique_ou_classement(cls):
        return int(input("Entrer 1 pour avoir le rapport par ordre alphabetique ou \
entrer 2 pour avoir le rapport par classement: "))

    @classmethod
    @Verification.verifier_nom_dans_db
    def entrer_nom_tournoi(cls):
        return input("Entrer le nom du tournoi dont vous voulez le rapport: ").capitalize()

    @classmethod
    @Verification.verifier_lieu_dans_db
    def entrer_lieu_tournoi(cls):
        return input("Entrer le lieu du tournoi dont vous voulez le rapport: ").capitalize()

    @classmethod
    def montrer_message(cls, message):
        print(message)

    @classmethod
    def message_erreur(cls):
        print("Le choix incorrect")
