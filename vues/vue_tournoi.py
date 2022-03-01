from utilitaires.verificateur import Verification


class VueTournoi:
    def __init__(self):
        pass

    @classmethod
    @Verification.verifier_input_remplit
    def creer_nom_tournoi(cls):
        return input("Entrer le nom de votre tournoi: ").capitalize()

    @classmethod
    @Verification.verifier_input_remplit
    def creer_lieu_tournoi(cls):
        return input("Entrer lieu du tournoi: ").capitalize()

    @classmethod
    @Verification.verifier_input_remplit
    def creer_description_tournoi(cls):
        return input("Mot du directeur: ").capitalize()

    @classmethod
    @Verification.verifier_nombre_tours
    def nombre_tours_tournoi(cls):
        return input("Entrer le nombre de tours voulu. Si vous voulez 4 tours, appuyer directement sur entree: ")

    @classmethod
    @Verification.verifier_controle_temps
    def controle_temps(cls):
        return int(input("Taper 1 pour choisir Bullet, 2 pour choisir Blitz ou 3 pour choisir Coup rapide: "))

    # def choix_ajouter_joueur(self):
    #     return int(input("Entrer 1 pour creer un joueur ou 2 pour choisir dans la base de donnees: "))

    # @Verification.verifier_doc_id
    # def choix_par_id(self):
    #     table_joueur = database.TABLE_JOUEUR
    #     for row in table_joueur:
    #         print(f"ID joueur: {row.doc_id} {row}")
    #     return int(input("Entrer l'id du joueur: "))

    @classmethod
    @Verification.verifier_nombre_joueurs
    def choisir_nombre_joueurs(cls):
        return input("Entrer le nombre de joueurs a ajouter au tournoi: ")

    @classmethod
    @Verification.verifier_nom_tournoi
    def rechercher_nom_tournoi(cls):
        return input("Entrer le nom du tournoi que vous voulez reprendre: ").capitalize()

    @classmethod
    @Verification.verifier_lieu_tournoi
    def rechercher_lieu_tournoi(cls):
        return input("Entrer le lieu du tournoi que vous voulez reprendre: ").capitalize()

    @classmethod
    def afficher_message(cls, message):
        print(message)

    @classmethod
    def message_erreur(cls):
        print("Votre choix n'est pas valide.")


def main():
    pass


if __name__ == "__main__":
    main()
