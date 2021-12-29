from vues.vue_joueurs import VueJoueur
from operator import itemgetter
from tinydb import TinyDB, Query

db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


class Joueur:
    """Enregistrer les nouveaux joueurs ou charger ceux enregistrés dans la base de donnees"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_naissance
        self.sexe_joueur = sexe
        self.classement_joueur = classement

    def sexe(self, choix_input) -> str:
        while True:    # Probleme de boucle infini puisque j'ai plus le input
            choix = choix_input
            longueur = choix.__len__()
            if longueur > 0 and longueur < 2:
                if choix == "M" or choix == "F":
                    return choix
                else:
                    print("Seulement F ou M.")
            else:
                print("Seulement un seul caractere.")

    def classement(self, choix_classement) -> int:
        while True:   # Probleme de boucle infini puisque j'ai plus le input
            choix = choix_classement
            if choix >= 0:
                return choix
            else:
                print("Le classement d'un joueur ne peut pas etre negatif.")

    def serialise_joueur(self, joueur):
        joueur_info = joueur
        serialise = {
            "nom": joueur_info.nom,
            "prenom": joueur_info.prenom,
            "naissance": joueur_info.date_de_naissance,
            "sexe": joueur_info.sexe_joueur,
            "classement": joueur_info.classement_joueur
        }
        return serialise

    def ajouter_joueur_du_tournoi_a_db(self, nom_tournoi, lieu_tournoi, joueur_recuperer):
        """Ajoute le joueur a la table 'table_joueur_par_tournoi' de la db"""
        info_joueur = joueur_recuperer
        serialise_joueur = {
            "nom_du_tournoi": nom_tournoi + "," + lieu_tournoi,
            "nom": info_joueur["nom"],
            "prenom": info_joueur["prenom"],
            "naissance": info_joueur["naissance"],
            "sexe": info_joueur["sexe"],
            "classement": info_joueur["classement"],
            "score": 0
        }
        table_joueur_par_tournoi.insert(serialise_joueur)
        return serialise_joueur

    def modifier_classement_joueur(self) -> str:
        """L'utilisateur peut modifier le classement d'un joueur par son ID"""
        while True:
            try:
                joueur_a_modifier = VueJoueur.modifier_classement()
                joueur_trouve = table_joueur.get(doc_id=joueur_a_modifier)
                if joueur_trouve is not None:
                    nouveau_classement = VueJoueur.nouveau_classement()
                    table_joueur.update({"classement": nouveau_classement}, doc_ids=[joueur_a_modifier])
                    return joueur_trouve
                else:
                    print("L'id ne fait pas partie de la DB.")
            except ValueError:
                print("Seulement les chiffres et les nombres sont acceptés")

    def recuperer_joueur_db(self, choix):
        """ Recupere le joueur dans la base de donnees par son 'id' """
        chercher_id = table_joueur.get(doc_id=choix)
        if chercher_id != []:
            print(chercher_id)
            return chercher_id
        else:
            print("Le joueur n'est pas enregistrer dans la DB")

    def classer_par_classement(self, table_db):  # Peut-etre a mettre dans 'raport', peut-etre utile pour 'round'
        """Pour que dans le rapport, les joueurs soient classés par ordre de classement"""
        liste_joueur = []
        for row in table_db:
            deserialise_joueur = [
                row["nom"],
                row["prenom"],
                row["naissance"],
                row["sexe"],
                row["classement"]
            ]
            liste_joueur.append(deserialise_joueur)
        liste_par_classement = sorted(liste_joueur, key=itemgetter(4), reverse=True)
        return liste_par_classement

    def classer_par_ordre_alphabetique(self, table_db):  # Peut-etre a mettre dans 'raport', peut-etre utile pour 'round'
        """Pour que dans le rapport, les joueurs soient classés par ordre alphabetique"""
        liste_joueur = []
        for row in table_db:
            deserialise_joueur = [
                row["nom"],
                row["prenom"],
                row["naissance"],
                row["sexe"],
                row["classement"]
            ]
            liste_joueur.append(deserialise_joueur)
        liste_par_ordre_alphabetique = sorted(liste_joueur, key=itemgetter(0))
        return liste_par_ordre_alphabetique


def main():
    pass


if __name__ == "__main__":
    main()
