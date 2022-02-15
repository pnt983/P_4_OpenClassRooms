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
        controller = ControllerApp()
        controller.controller_tournoi.reprendre_tournoi()

    def run_tournoi(self):
        controller = ControllerApp()
        tournoi = controller.controller_tournoi.creer_tournoi()
        controller.controller_tournoi.ajouter_joueur_au_tournoi()
        tournoi.sauvegarder_tournoi()
        input("Appuyer sur 'Entrer' pour commencer le round")
        round_1 = tournoi.creer_premier_round()
        tournoi.sauvegarder_tournoi()
        input("Appuyer sur 'Entrer' pour finir le round")
        round_1[1].ajouter_date_fin_round()
        tournoi.sauvegarder_tournoi()
        controller.controller_round.entrer_resultat_matchs(round_1[0])
        round_1[1].cloturer_round()
        tournoi.sauvegarder_tournoi()
        for i in range(int(tournoi.nb_tour) - 1):
            round_suivant = tournoi.creer_rounds_suivant()
            tournoi.sauvegarder_tournoi()
            input("Appuyer sur 'Entrer' pour finir le round")
            round_suivant[1].ajouter_date_fin_round()
            tournoi.sauvegarder_tournoi()
            controller.controller_round.entrer_resultat_matchs(round_suivant[0])
            round_suivant[1].cloturer_round()
            i += 1
        tournoi.sauvegarder_tournoi()
        tournoi.cloturer_tournoi()

    def gerer_joueurs(self):
        menu_joueur = menu.Menu("Menu joueur", menu.option_joueur)
        choix_joueur = menu_joueur.display()
        controller = ControllerApp()
        if choix_joueur == "1":
            controller.controller_joueur.creer_joueur()
        elif choix_joueur == "2":
            controller.controller_joueur.modifier_classement_joueur()
        elif choix_joueur == "3":
            print("Retour en arriere")
        else:
            print("Choix invalide !")

    def gerer_rapports(self):
        menu_rapport = menu.Menu("Menu rapport", menu.option_rapport)
        choix_rapport = menu_rapport.display()
        controller = ControllerApp()
        if choix_rapport == "1":
            controller.controller_rapport.afficher_rapport_acteurs()
        elif choix_rapport == "2":
            controller.controller_rapport.afficher_joueurs_tournoi()
        elif choix_rapport == "3":
            controller.controller_rapport.afficher_tous_les_tournois()
        elif choix_rapport == "4":
            controller.controller_rapport.afficher_tous_tours_tournoi()
        elif choix_rapport == "5":
            controller.controller_rapport.afficher_tous_matchs_tournois()
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
                    ControllerApp().run_tournoi()
                elif choix_tournoi == "2":
                    print(f"Je suis dans {choix_tournoi}")
                    # Methode pour reprendre un tournoi ici
                elif choix_tournoi == "3":
                    print("Retour au menu principal")
                else:
                    print("Choix invalide !")
            elif choix_principal == "2":
                ControllerApp().gerer_joueurs()
            elif choix_principal == "3":
                ControllerApp().gerer_rapports()
            elif choix_principal == "4":
                print("A bientot")
                break
            else:
                print("Choix invalide !")


def main():
    pass


if __name__ == "__main__":
    main()
