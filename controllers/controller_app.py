from .controller_tournois import ControleurTournoi
from .controller_round import ControllerRound


def run():
    tournoi_1 = ControleurTournoi()
    tournoi = tournoi_1.creer_tournoi()
    tournoi_1.ajouter_joueur_au_tournoi(tournoi.nom, tournoi.lieu)
    premier_round = ControllerRound.creer_premier_round(ControllerRound, tournoi.nom, tournoi.lieu)
    ControllerRound.entrer_resultat_matchs(ControllerRound, tournoi.nom, premier_round[1])
    ControllerRound.creer_les_rounds_suivant(ControllerRound, tournoi.nom, tournoi.lieu)


def main():
    pass


if __name__ == "__main__":
    main()
