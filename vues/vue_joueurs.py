from models import tournoi
from verificateur import Verification

class VueJoueur:

    def __init__(self):
        pass

    def creer_infos_joueur(self):
        date_naissance = input("Date de naissance du joueur. Format: jj/mm/aaaa: ")
        dictionnaire = {
            "date_naissance": date_naissance
        }
        return dictionnaire

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

    def choix_ajouter_joueur(self):
        return int(input("Entrer 1 pour creer un joueur ou 2 pour choisir dans la base de donnees: "))

    def choix_utilisateur(self):
        return int(input("Taper 1 pour chercher par nom et prenom. Ou 2 \
    pour choisir par id: "))

    def choix_par_id(self):
        for row in tournoi.table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur: "))

    def modifier_classement(self) -> int:
        for row in tournoi.table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")
        return int(input("Entrer l'id du joueur: "))

    def nouveau_classement(self) -> int:
        return int(input("Entrer le nouveau classement du joueur: "))

    def indice_joueur(self):
        for row in tournoi.table_joueur:
            print(f"ID joueur: {row.doc_id} {row}")

    def message_erreur(self):
        print("Votre choix n'est pas valide.")


def main():
    VueJoueur.creer_nom_joueur(VueJoueur)
    VueJoueur.creer_prenom_joueur(VueJoueur)
    VueJoueur.creer_sexe_joueur(VueJoueur)
    VueJoueur.creer_classement_joueur(VueJoueur)
    VueJoueur.creer_date_naissance_joueur(VueJoueur)


if __name__ == "__main__":
    main()
