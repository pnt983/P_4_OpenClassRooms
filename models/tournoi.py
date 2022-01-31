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
        self.user = database.USER

    def serialiser_tournoi(self):
        serialise = {
            "nom_du_tournoi": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nombre_de_tour": self.nb_tour,
            "controle_du_temps": self.controle_du_temps,
            "description": self.description,
            "etat_tournoi": "en_cours"
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

    def cloturer_tournoi(self):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == self.nom and self.user.lieu == self.lieu)
        for row in table_tournoi:
            row["etat_tournoi"]
            self.table_tournoi.update({"etat_tournoi": "Fini"}, self.user.nom_du_tournoi == self.nom and self.user.lieu == self.
                                      lieu)


def main():
    pass


if __name__ == "__main__":
    main()
