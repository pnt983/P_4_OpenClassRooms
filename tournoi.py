import joueur
from vue_tournoi import CreerTournoi
import controller
from tinydb import TinyDB, Query
import time


db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


class Tournoi:

    def __init__(self, nombre_joueur: int = 8):
        self.nom = CreerTournoi.nom_tournoi(CreerTournoi)
        self.lieu = CreerTournoi.lieu_tournoi(CreerTournoi)
        self.date = time.strftime("%d-%m-%Y")
        self.nb_tour = CreerTournoi.nb_tours(CreerTournoi)
        self.controle_temps = CreerTournoi.controle_temps(CreerTournoi)
        self.description = CreerTournoi.description(CreerTournoi)
        self.ajouter_joueur = self.ajouter_joueur_au_tournoi(nombre_joueur)
        self.tournoi_db = self.enregistrer_tournoi()

    def ajouter_joueur_au_tournoi(self, nombre_joueur: int = 8):
        i = 0
        for i in range(nombre_joueur):
            joueur.Joueur.entrer_joueur(joueur.Joueur, self.nom, self.lieu)
            i += 1

    def enregistrer_tournoi(self):
        serialise = {
            "Nom du tournoi": self.nom,
            "Lieu": self.lieu,
            "Nombre de tour": self.nb_tour,
            "Controle du temps": self.controle_temps,
            "Description": self.description
        }
        table_tournoi.insert(serialise)

    def reprendre_tournoi(self):
        pass


def main():
    Tournoi()


if __name__ == "__main__":
    main()
