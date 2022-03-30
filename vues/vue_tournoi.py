from utilitaires.verificateur import Verification


class VueTournoi:
    def __init__(self):
        pass

    @classmethod
    @Verification.verifier_input_remplit
    def creer_nom_tournoi(cls):
        return input("\n" + "Entrer le nom de votre tournoi: ").capitalize()

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
    def choisir_nombre_tours_tournoi(cls):
        return input("Entrer le nombre de tours voulu. Si vous voulez 4 tours, appuyer directement sur entrée: ")

    @classmethod
    @Verification.verifier_controle_temps
    def choisir_controle_temps(cls):
        return int(input("Taper 1 pour choisir Bullet, 2 pour choisir Blitz ou 3 pour choisir Coup rapide: "))

    @classmethod
    @Verification.verifier_nombre_joueurs
    def choisir_nombre_joueurs(cls):
        return input("Entrer le nombre de joueurs à ajouter au tournoi. Si vous voulez 8 joueurs, appuyer \
directement sur entrée: ")

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
    def afficher_classement_final(cls, classement):
        print("\n", "Voici le classement final: ")
        for row in classement:
            print("\n", classement.index(row) + 1, row.nom, row.prenom, row.date_de_naissance,
                  row.classement_joueur)

    @classmethod
    @Verification.verifier_sortir_tournoi
    def valider_debut_round(cls):
        return input("\n" + "Appuyer sur 'Entrer' pour commencer le round ou appuyer sur 'Q' pour quitter \
le tournoi: ").capitalize()

    @classmethod
    @Verification.verifier_sortir_tournoi
    def valider_fin_round(cls):
        return input("\n" + "Appuyer sur 'Entrer' pour finir le round ou appuyer sur 'Q' pour quitter \
le tournoi: ").capitalize()


def main():
    pass


if __name__ == "__main__":
    main()
