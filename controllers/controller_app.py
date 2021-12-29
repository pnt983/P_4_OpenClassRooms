from .controller_tournois import ControleurTournoi


def run():
    tournoi_1 = ControleurTournoi()
    resultat = tournoi_1.creer_tournoi()
    tournoi_1.ajouter_joueur_au_tournoi(resultat.nom, resultat.lieu)


def main():
    pass


if __name__ == "__main__":
    main()
