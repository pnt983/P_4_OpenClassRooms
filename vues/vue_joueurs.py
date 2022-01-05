from models import tournoi
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

    def choix_utilisateur(self):
        return int(input("Taper 1 pour chercher par nom et prenom. Ou 2 \
    pour choisir par id: "))

    def modifier_classement(self) -> int:
        for row in tournoi.table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur: "))

    def nouveau_classement(self) -> int:
        return int(input("Entrer le nouveau classement du joueur: "))

    def indice_joueur(self):
        for row in tournoi.table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")


def main():
    pass


if __name__ == "__main__":
    main()
