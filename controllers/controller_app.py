from .controller_rapport import ControllerRapport
from controllers.controller_joueurs import ControllerJoueur
from .controller_tournois import ControleurTournoi
from .controller_round import ControllerRound
import utilitaires.menu as menu
from tinydb import TinyDB, Query


DB = TinyDB("db.json")
USER = Query()
TABLE_JOUEUR = DB.table("Joueur")
TABLE_TOURNOI = DB.table("Tournoi")


class ControllerApp:

    def __init__(self):
        self.controller_tournoi = ControleurTournoi(TABLE_TOURNOI, USER)
        self.controller_joueur = ControllerJoueur(TABLE_JOUEUR, USER)
        self.controller_round = ControllerRound()
        self.controller_rapport = ControllerRapport(TABLE_JOUEUR, TABLE_TOURNOI, USER)

    def test(self):
        self.controller_tournoi.reprendre_tournoi()

    def menu_principal(self):
        while True:
            menu_general = menu.Menu("Menu principal", menu.option_principale)
            choix_principal = menu_general.display()
            if choix_principal == "1":
                while True:
                    menu_tournoi = menu.Menu("Menu tournoi", menu.option_tournoi)
                    choix_tournoi = menu_tournoi.display()
                    if choix_tournoi == "1":
                        self.controller_tournoi.commencer_tournoi()
                    elif choix_tournoi == "2":
                        self.controller_tournoi.reprise_tournoi()
                    elif choix_tournoi == "3":
                        print("Retour au menu principal")
                        break
                    else:
                        print("Choix invalide !")
            elif choix_principal == "2":
                self.controller_joueur.gerer_joueurs()
            elif choix_principal == "3":
                self.controller_rapport.gerer_rapports()
            elif choix_principal == "4":
                print("A bientot")
                break
            else:
                print("Choix invalide !")


def main():
    pass


if __name__ == "__main__":
    main()
