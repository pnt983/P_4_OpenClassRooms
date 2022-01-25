import database
import datetime


class Tournoi:

    def __init__(self, nom, lieu, description, nb_tour, controle_du_temps, nombre_joueur: int = 8):
        self.nom = nom
        self.lieu = lieu
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.nb_tour = nb_tour
        self.controle_du_temps = controle_du_temps
        self.description = description
        self.players = []
        self.rounds = []
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI

    def serialiser_tournoi(self):
        serialise = {
            "Nom du tournoi": self.nom,
            "Lieu": self.lieu,
            "Date": self.date,
            "Nombre de tour": self.nb_tour,
            "Controle du temps": self.controle_du_temps,
            "Description": self.description
        }
        return serialise

    def enregistrer_tournoi(self):
        data = self.serialiser_tournoi()
        self.table_tournoi.insert(data)

    def sauvegarder_joueur_du_tournoi_dans_db(self, joueur_recuperer):
        """Ajoute le joueur a la table 'table_joueur_par_tournoi' de la db"""
        info_joueur = joueur_recuperer
        for joueur in info_joueur:
            serialise_joueur = {
                "nom_du_tournoi": self.nom + "," + self.lieu,
                "nom": joueur.nom,
                "prenom": joueur.prenom,
                "naissance": joueur.date_de_naissance,
                "sexe": joueur.sexe_joueur,
                "classement": joueur.classement_joueur,
                "score": 0
            }
            self.table_joueur_par_tournoi.insert(serialise_joueur)
        return serialise_joueur


def main():
    pass


if __name__ == "__main__":
    main()
