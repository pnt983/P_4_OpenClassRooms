
from verificateur import Verification


class VueTournoi:
    def __init__(self):
        pass

    @Verification.verifier_input_remplit
    def creer_nom_tournoi(self):
        return input("Entrer le nom de votre tournoi: ").capitalize()

    @Verification.verifier_input_remplit
    def creer_lieu_tournoi(self):
        return input("Entrer lieu du tournoi: ").capitalize()

    @Verification.verifier_input_remplit
    def creer_description_tournoi(self):
        return input("Mot du directeur: ").capitalize()

    @Verification.verifier_nombre_tours
    def nombre_tours_tournoi(self):
        return input("Entrer le nombre de tours voulu. Si vous voulez 4 tours, appuyer directement sur entree: ")

    @Verification.verifier_controle_temps
    def controle_temps(self):
        return int(input("Taper 1 pour choisir Bullet, 2 pour choisir Blitz ou 3 pour choisir Coup rapide: "))

    def choisir_nombre_joueurs(self):
        return input("Entrer le nombre de joueurs a ajouter au tournoi: ")

    def message_erreur(self):
        print("Veuillez choisir un nombre. Les lettres ne sont pas autorises !")


def main():
    pass


if __name__ == "__main__":
    main()
