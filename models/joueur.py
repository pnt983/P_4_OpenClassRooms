from database import DataBase
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

    def recuperer_joueur_db(self, choix):
        """ Recupere le joueur dans la base de donnees par son 'id' """
        chercher_id = table_joueur.get(doc_id=choix)
        if chercher_id != []:
            print(chercher_id)
            return chercher_id
        else:
            print("Le joueur n'est pas enregistrer dans la DB")

    def enregistrer_joueur_dans_db(self, serialise, nom_joueur, prenom_joueur):
        """Ajoute le joueur a 'table_joueur' de la db. Si il y est deja, il met a jour les infos données"""
        table_joueur.upsert(serialise, user.nom == nom_joueur and user.prenom == prenom_joueur)


def main():
    pass


if __name__ == "__main__":
    main()
