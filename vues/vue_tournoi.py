from models import tournoi
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

    def choix_ajouter_joueur(self):
        return int(input("Entrer 1 pour creer un joueur ou 2 pour choisir dans la base de donnees: "))

    def choix_par_id(self):
        for row in tournoi.table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur: "))

    def choisir_nombre_joueurs(self):
        return input("Entrer le nombre de joueurs a ajouter au tournoi: ")

    def message_erreur(self):
        print("Votre choix n'est pas valide.")


def main():
    pass


if __name__ == "__main__":
    main()
