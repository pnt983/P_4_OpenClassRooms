import database
import time


class Tournoi:

    def __init__(self, nom, lieu, description, nb_tour, controle_du_temps, nombre_joueur: int = 8):
        self.nom = nom
        self.lieu = lieu
        self.date = time.strftime("%d-%m-%Y")
        self.nb_tour = nb_tour
        self.controle_du_temps = controle_du_temps
        self.description = description
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI

    def serialiser_tournoi(self):
        serialise = {
            "Nom du tournoi": self.nom,
            "Lieu": self.lieu,
            "Nombre de tour": self.nb_tour,
            "Controle du temps": self.controle_du_temps,
            "Description": self.description
        }
        return serialise

    def enregistrer_tournoi(self):
        data = self.serialiser_tournoi()
        self.table_tournoi.insert(data)

    def sauvegarder_joueur_du_tournoi_dans_db(self, nom_tournoi, lieu_tournoi, joueur_recuperer):
        """Ajoute le joueur a la table 'table_joueur_par_tournoi' de la db"""
        info_joueur = joueur_recuperer
        liste = []
        for joueur in info_joueur:
            serialise_joueur = {
                "nom": joueur["nom"],
                "prenom": joueur["prenom"],
                "naissance": joueur["naissance"],
                "sexe": joueur["sexe"],
                "classement": joueur["classement"],
                "score": 0
            }
            liste.append(serialise_joueur)
        test = {
            "nom_du_tournoi": nom_tournoi + "," + lieu_tournoi,
            "joueur": liste
        }
        database.TABLE_JOUEUR_PAR_TOURNOI.insert(test)
        return test


def main():
    pass


if __name__ == "__main__":
    main()
