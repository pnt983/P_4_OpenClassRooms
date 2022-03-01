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

    def run_tournoi(self):
        tournoi = self.controller_tournoi.creer_tournoi()
        liste_joueurs = self.controller_joueur.ajouter_joueur(tournoi.nombre_joueur)
        tournoi.enregistrer_joueur(liste_joueurs)
        tournoi.sauvegarder_tournoi()
        input("Appuyer sur 'Entrer' pour commencer le round")
        round_1 = self.controller_round.creer_premier_round(tournoi.joueurs)
        tournoi.enregistrer_round(round_1)
        tournoi.sauvegarder_tournoi()
        input("Appuyer sur 'Entrer' pour finir le round")
        round_1.ajouter_date_fin_round()
        tournoi.sauvegarder_tournoi()
        self.controller_round.entrer_resultat_matchs(round_1.match)
        round_1.cloturer_round()
        tournoi.sauvegarder_tournoi()
        for i in range(int(tournoi.nb_tour) - 1):
            round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
            tournoi.enregistrer_round(round_suivant)
            tournoi.sauvegarder_tournoi()
            input("Appuyer sur 'Entrer' pour finir le round")
            round_suivant.ajouter_date_fin_round()
            tournoi.sauvegarder_tournoi()
            self.controller_round.entrer_resultat_matchs(round_suivant.match)
            round_suivant.cloturer_round()
            i += 1
        tournoi.sauvegarder_tournoi()
        tournoi.cloturer_tournoi()

    def reprendre_tournoi(self):    # A finir
        tournoi = self.controller_tournoi.reprendre_tournoi()
        tournoi.table_tournoi = self.controller_tournoi.table_tournoi
        tournoi.user = self.controller_tournoi.user
        liste_rounds = []
        for round in tournoi.rounds:
            liste_rounds.append(round)
        if liste_rounds[-1].etat_round == "En_cours":
            round = liste_rounds[-1]
            print(f"Vous reprenez le tournoi {tournoi.nom}-{tournoi.lieu} au tour n°{len(liste_rounds)}")
            tournoi.joueurs = [tournoi.joueurs]
            round.ajouter_date_fin_round()
            self.controller_round.entrer_resultat_matchs(round.match)
            round.cloturer_round()
            tournoi.test_sauvegarder_tournoi()
            for i in range(int(tournoi.nb_tour) - len(liste_rounds)):
                round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
                tournoi.enregistrer_round(round_suivant)
                input("Appuyer sur 'Entrer' pour finir le round")
                round_suivant.ajouter_date_fin_round()
                self.controller_round.entrer_resultat_matchs(round_suivant.match)
                round_suivant.cloturer_round()
                i += 1
            tournoi.test_sauvegarder_tournoi()
            tournoi.cloturer_tournoi()
        else:
            round = liste_rounds[-1]
            print(f"Vous reprenez le tournoi {tournoi.nom}-{tournoi.lieu}. Le tour précédent etait \
le tour n°{len(liste_rounds)}")
            tournoi.joueurs = [tournoi.joueurs]
            for i in range(int(tournoi.nb_tour) - len(liste_rounds)):
                round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
                tournoi.enregistrer_round(round_suivant)
                input("Appuyer sur 'Entrer' pour finir le round")
                round_suivant.ajouter_date_fin_round()
                self.controller_round.entrer_resultat_matchs(round_suivant.match)
                round_suivant.cloturer_round()
                i += 1
            tournoi.test_sauvegarder_tournoi()
            tournoi.cloturer_tournoi()

    def menu_principal(self):
        while True:
            menu_general = menu.Menu("Menu principal", menu.option_principale)
            choix_principal = menu_general.display()
            if choix_principal == "1":
                while True:
                    menu_tournoi = menu.Menu("Menu tournoi", menu.option_tournoi)
                    choix_tournoi = menu_tournoi.display()
                    if choix_tournoi == "1":
                        self.run_tournoi()
                    elif choix_tournoi == "2":
                        self.reprendre_tournoi()
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
