from . import controller_joueurs
from . import controller_tournois


def run():
    test = controller_tournois.ControleurTournoi()
    resultat = test.creer_tournoi()
    test.ajouter_joueur_au_tournoi(resultat.nom, resultat.lieu)


def main():
    pass


if __name__ == "__main__":
    main()
