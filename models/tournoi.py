from tinydb import TinyDB, Query
import time


db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


class Tournoi:

    def __init__(self, nom, lieu, description, nb_tour, controle_du_temps, nombre_joueur: int = 8):
        self.nom = nom
        self.lieu = lieu
        self.date = time.strftime("%d-%m-%Y")
        self.nb_tour = nb_tour
        self.controle_du_temps = controle_du_temps
        self.description = description

    def enregistrer_tournoi(self, info_tournoi):
        infos = info_tournoi
        serialise = {
            "Nom du tournoi": infos.nom,
            "Lieu": infos.lieu,
            "Nombre de tour": infos.nb_tour,
            "Controle du temps": infos.controle_du_temps,
            "Description": infos.description
        }
        table_tournoi.insert(serialise)

    def reprendre_tournoi(self):
        pass


def main():
    Tournoi()


if __name__ == "__main__":
    main()
