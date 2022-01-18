from verificateur import Verification


class VueRapport:

    def __init__(self):
        pass

    @Verification.verifier_alphabetique_ou_classement
    def choisir_alphabetique_ou_classement(self):
        return int(input("Entrer 1 pour avoir le rapport par ordre alphabetique ou \
entrer 2 pour avoir le rapport par classement: "))

    @Verification.verifier_nom_dans_db
    def entrer_nom_tournoi(self):
        return input("Entrer le nom du tournoi dont vous voulez le rapport: ").capitalize()

    @Verification.verifier_lieu_dans_db
    def entrer_lieu_tournoi(self):
        return input("Entrer le lieu du tournoi dont vous voulez le rapport: ").capitalize()

    def montrer_message(self, message):
        print(message)

    def message_erreur(self):
        print("Le choix incorrect")
