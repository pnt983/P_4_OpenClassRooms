from verificateur import Verification


class VueJoueur:
    """Controle tous les inputs et tous les prints"""

    def __init__(self):
        pass

    @classmethod
    @Verification.verifier_input_remplit
    def creer_nom_joueur(cls):
        return input("Entrer le nom du joueur: ").capitalize()

    @classmethod
    @Verification.verifier_input_remplit
    def creer_prenom_joueur(cls):
        return input("Entrer le prenom du joueur: ").capitalize()

    @classmethod
    @Verification.verifier_sexe
    def creer_sexe_joueur(cls):
        return input("Entrer M pour les hommes et F pour les femmes: ").capitalize()

    @classmethod
    @Verification.verifier_classement
    def creer_classement_joueur(cls):
        return int(input("Classement du joueur: "))

    @classmethod
    @Verification.verifier_date_naissance
    def creer_date_naissance_joueur(cls):
        return input("Date de naissance du joueur. Format: jj/mm/aaaa: ")

    @classmethod
    @Verification.verifier_classement
    def modifier_classement(cls, table) -> int:
        for row in table:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur pour modifier son classement: "))

    @classmethod
    @Verification.verifier_classement
    def nouveau_classement(cls) -> int:
        return int(input("Entrer le nouveau classement du joueur: "))

    # def indice_joueur(self):
    #     for row in database.TABLE_JOUEUR:
    #         print(f"ID joueur: {row.doc_id} {row}")

    @classmethod
    def message_erreur(cls):
        print("Le choix est incorrect")

    @classmethod
    def afficher_message(cls, message):
        print(message)

    @classmethod
    def choix_ajouter_joueur(cls):
        return int(input("Entrer 1 pour creer un joueur ou 2 pour choisir dans la base de donnees: "))

    @classmethod
    @Verification.verifier_doc_id
    def choix_par_id(cls, table_joueur):
        for row in table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur: "))


def main():
    pass


if __name__ == "__main__":
    main()
