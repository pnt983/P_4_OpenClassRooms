from controllers import controller_joueurs
import database
from verificateur import Verification


class VueJoueur:
    """Controle tous les inputs et tous les prints"""

    def __init__(self):
        pass

    @Verification.verifier_input_remplit
    def creer_nom_joueur(self):
        return input("Entrer le nom du joueur: ").capitalize()

    @Verification.verifier_input_remplit
    def creer_prenom_joueur(self):
        return input("Entrer le prenom du joueur: ").capitalize()

    @Verification.verifier_sexe
    def creer_sexe_joueur(self):
        return input("Entrer M pour les hommes et F pour les femmes: ").capitalize()

    @Verification.verifier_classement
    def creer_classement_joueur(self):
        return int(input("Classement du joueur: "))

    @Verification.verifier_date_naissance
    def creer_date_naissance_joueur(self):
        return input("Date de naissance du joueur. Format: jj/mm/aaaa: ")

    @Verification.verifier_classement
    def modifier_classement(self, table) -> int:
        for row in table:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur pour modifier son classement: "))

    @Verification.verifier_classement
    def nouveau_classement(self) -> int:
        return int(input("Entrer le nouveau classement du joueur: "))

    def indice_joueur(self):
        for row in database.TABLE_JOUEUR:
            print(f"ID joueur: {row.doc_id} {row}")

    def message_erreur(self):
        print("Le choix est incorrect")

    def afficher_message(self, message):
        print(message)

    def choix_ajouter_joueur(self):
        return int(input("Entrer 1 pour creer un joueur ou 2 pour choisir dans la base de donnees: "))

    @Verification.verifier_doc_id
    def choix_par_id(self):
        table_joueur = database.TABLE_JOUEUR
        for row in table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur: "))


def main():
    pass


if __name__ == "__main__":
    main()
