from models.rapport import Rapport
from models.round import Round
from .controller_rapport import ControllerRapport
from controllers.controller_joueurs import ControllerJoueur
from models.tournoi import Tournoi
from .controller_tournois import ControleurTournoi
from .controller_round import ControllerRound


class ControllerApp:

    def __init__(self):
        pass

    def run(self):
        tournoi_1 = ControleurTournoi()
        # tournoi = tournoi_1.creer_tournoi()
        # tournoi_1.ajouter_joueur_au_tournoi(tournoi.nom, tournoi.lieu)
        # premier_round = ControllerRound.creer_premier_round(ControllerRound, tournoi.nom, tournoi.lieu)
        # time.sleep(120)
        # ControllerRound.fin_round(ControllerRound, tournoi.nom, tournoi.lieu, premier_round[1])
        # round_suivant = ControllerRound.creer_les_rounds_suivant(ControllerRound, tournoi.nom, tournoi.lieu)
        # time.sleep(120)
        # ControllerRound.fin_round(ControllerRound, tournoi.nom, tournoi.lieu, round_suivant[1])


def main():
    pass


if __name__ == "__main__":
    main()
