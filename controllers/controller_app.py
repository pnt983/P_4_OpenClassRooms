from .controller_rapport import ControllerRapport
from controllers.controller_joueurs import ControllerJoueur
from .controller_tournois import ControleurTournoi
from .controller_round import ControllerRound
import menu
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
        for round in tournoi.rounds:
            if round.etat_round == "En_cours":
                print(f"Vous reprenez le tournoi {tournoi.nom}-{tournoi.lieu} au tour n°{round.compte_round}")
                round.ajouter_date_fin_round()
                # for row in round.match:
                #     for joueur in row:
                #         test = Joueur.deserialise_joueur(joueur)
                # print(type(joueur), joueur)
                # self.controller_round.entrer_resultat_matchs(round.match)
                round.cloturer_round()
            else:
                for round in tournoi.rounds:
                    print(f"Vous reprenez le tournoi {tournoi.nom}-{tournoi.lieu} au tour n°{round.compte_round}")
                    tournoi.joueurs = [tournoi.joueurs]
                    for i in range(int(tournoi.nb_tour) - round.compte_round):
                        round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
                        tournoi.enregistrer_round(round_suivant)
                        input("Appuyer sur 'Entrer' pour finir le round")
                        round_suivant.ajouter_date_fin_round()
                        self.controller_round.entrer_resultat_matchs(round_suivant.match)
                        round_suivant.cloturer_round()
                        i += 1
                    tournoi.sauvegarder_tournoi()
                    tournoi.cloturer_tournoi()
                    break

    def gerer_joueurs(self):
        menu_joueur = menu.Menu("Menu joueur", menu.option_joueur)
        choix_joueur = menu_joueur.display()
        if choix_joueur == "1":
            self.controller_joueur.creer_joueur()
        elif choix_joueur == "2":
            self.controller_joueur.modifier_classement_joueur()
        elif choix_joueur == "3":
            print("Retour en arriere")
        else:
            print("Choix invalide !")

    def gerer_rapports(self):
        menu_rapport = menu.Menu("Menu rapport", menu.option_rapport)
        choix_rapport = menu_rapport.display()
        if choix_rapport == "1":
            self.controller_rapport.afficher_rapport_acteurs()
        elif choix_rapport == "2":
            self.controller_rapport.afficher_joueurs_tournoi()
        elif choix_rapport == "3":
            self.controller_rapport.afficher_tous_les_tournois()
        elif choix_rapport == "4":
            self.controller_rapport.afficher_tous_tours_tournoi()
        elif choix_rapport == "5":
            self.controller_rapport.afficher_tous_matchs_tournois()
        elif choix_rapport == "6":
            print("Retour en arriere")
        else:
            print("Choix invalide !")
            pass

    def menu_principal(self):
        while True:
            menu_general = menu.Menu("Menu principal", menu.option_principale)
            choix_principal = menu_general.display()
            if choix_principal == "1":
                menu_tournoi = menu.Menu("Menu tournoi", menu.option_tournoi)
                choix_tournoi = menu_tournoi.display()
                if choix_tournoi == "1":
                    self.run_tournoi()
                elif choix_tournoi == "2":
                    self.reprendre_tournoi()
                elif choix_tournoi == "3":
                    print("Retour au menu principal")
                else:
                    print("Choix invalide !")
            elif choix_principal == "2":
                self.gerer_joueurs()
            elif choix_principal == "3":
                self.gerer_rapports()
            elif choix_principal == "4":
                print("A bientot")
                break
            else:
                print("Choix invalide !")


def main():
    pass


if __name__ == "__main__":
    main()
