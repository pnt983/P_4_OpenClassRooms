from . import joueur
from vues.vue_tournoi import VueTournoi
from controllers.controller_tournois import ControleurTour
import controllers.controller as controller
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

    def nb_tours(self, nombre_tours) -> str:
        while True:  # Probleme de boucle infini puisque j'ai plus le input
            try:
                choix_utilisateur = nombre_tours
                if not choix_utilisateur:
                    return "4"
                elif int(choix_utilisateur):
                    return f"{choix_utilisateur}"
                else:
                    print("Veuillez choisir un nombre. Les lettres ne sont pas autorises !")
                    return "4"
            except ValueError:
                print("Veuillez choisir un nombre. Les lettres ne sont pas autorises !")
                return "4"

    def controle_temps(self, choix_input):
        choix = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}
        while True:   # Probleme de boucle infini puisque j'ai plus le input
            try:
                choix_utilisateur = choix_input
                if choix_utilisateur in choix:
                    return choix[choix_utilisateur]
                else:
                    print(f"Le choix {choix_utilisateur} ne fais pas partie des options possibles")
            except ValueError:
                print("Les lettres ne sont pas acceptees, veuillez saisir 1, 2 ou 3 pour faire votre choix")

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
            "Controle du temps": self.controle_du_temps,
            "Description": self.description
        }
        table_tournoi.insert(serialise)

    def reprendre_tournoi(self):
        pass


def main():
    Tournoi()


if __name__ == "__main__":
    main()
