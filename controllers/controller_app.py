from .controller_tournois import ControleurTournoi
from .controller_round import ControllerRound
from .controller_joueurs import ControllerJoueur
from .controller_rapport import ControllerRapport
from models.rapport import Rapport
from tinydb import TinyDB, Query


class ControllerApp:

    def __init__(self):
        self.db = TinyDB("db.json")
        self.user = Query()
        self.table_joueur = self.db.table("Joueur")
        self.table_tournoi = self.db.table("Tournoi")
        self.table_joueur_par_tournoi = self.db.table("Joueur_du_tournoi")
        self.table_rounds_par_tournoi = self.db.table("Rounds")

    def run(self):
        ControllerRapport.afficher_tous_tours_tournoi(ControllerRapport)
        # tournoi_1 = ControleurTournoi()
        # tournoi = tournoi_1.creer_tournoi()
        # tournoi_1.ajouter_joueur_au_tournoi(tournoi.nom, tournoi.lieu)
        # premier_round = ControllerRound.creer_premier_round(ControllerRound, tournoi.nom, tournoi.lieu)
        # ControllerRound.entrer_resultat_matchs(ControllerRound, tournoi.nom, premier_round[1])
        # ControllerRound.creer_les_rounds_suivant(ControllerRound, tournoi.nom, tournoi.lieu)


def main():
    pass


if __name__ == "__main__":
    main()
