import tournoi


class VueJoueur:

    def __init__(self):
        pass

    def creer_infos_joueur(self):
        nom = input("Nom du joueur: ").capitalize()
        prenom = input("Prenom du joueur: ").capitalize()
        date_naissance = input("Date de naissance du joueur. Format: jj/mm/aaaa: ")
        sexe = input("Entrer M pour les hommes et F pour les femmes: ").capitalize()
        classement = int(input("Classement du joueur: "))
        dictionnaire = {
            "nom": nom,
            "prenom": prenom,
            "date_naissance": date_naissance,
            "sexe": sexe,
            "classement": classement
        }
        return dictionnaire

    def choix_utilisateur(self):
        return int(input("Taper 1 pour chercher par nom et prenom. Ou 2 \
    pour choisir par id: "))

    def choix_par_nom(self):
        return input("Entrer le nom du joueur: ").capitalize()

    def choix_par_prenom(self):
        return input("Entrer le prenom du joueur: ").capitalize()

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


def main():
    pass


if __name__ == "__main__":
    main()
