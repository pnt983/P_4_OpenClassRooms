from .controller_rapport import ControllerRapport
from controllers.controller_joueurs import ControllerJoueur
from .controller_tournois import ControleurTournoi
from .controller_round import ControllerRound


class couleur:
    VERT = '\033[92m'
    JAUNE = '\033[93m'
    ROUGE = '\033[91m'
    BLEU = '\033[94m'
    VIOLET = '\033[95m'
    RESET = '\033[0m'   # RESET COLOR


class ControllerApp:

    def __init__(self):
        self.controller_tournoi = ControleurTournoi()
        self.controller_joueur = ControllerJoueur()
        self.controller_round = ControllerRound()
        self.controller_rapport = ControllerRapport()

    def run(self):
        pass
        # controller_tournoi = ControleurTournoi()
        # tournoi = controller_tournoi.creer_tournoi()
        # controller_tournoi.ajouter_joueur_au_tournoi(tournoi.nom, tournoi.lieu)
        # premier_round = ControllerRound.creer_premier_round(ControllerRound, tournoi.nom, tournoi.lieu)
        # ControllerRound.fin_round(ControllerRound, tournoi.nom, tournoi.lieu, premier_round[1])
        # round_suivant = ControllerRound.creer_les_rounds_suivant(ControllerRound, tournoi.nom, tournoi.lieu)
        # ControllerRound.fin_round(ControllerRound, tournoi.nom, tournoi.lieu, round_suivant[1])

    def menu_principal(self):
        while True:
            choix_principal = input(f"{couleur.VERT}Entrer 1 pour gerer les tournois\nEntrer 2 pour gerer les joueurs\nEntrer \
3 pour gerer les rapport\nEntrer 'q' pour quitter le logiciel\n{couleur.ROUGE}Entrer est votre choix: {couleur.RESET}")

            try:
                if choix_principal == "1":
                    while True:
                        choix_tournoi = input(f"{couleur.BLEU}Entrer 1 pour creer un nouveau tournoi\nEntrer 2 pour \
reprendre un tournoi\nEntrer 'r' pour revenir au menu principal\n{couleur.ROUGE}Entrer votre choix: {couleur.RESET}")
                        try:
                            if choix_tournoi == "1":
                                controller = ControllerApp()
                                # creer tournoi
                                tournoi = controller.controller_tournoi.creer_tournoi()
                                # ajouter joueur
                                liste_joueurs = controller.controller_tournoi.ajouter_joueur_au_tournoi()
                                tournoi.sauvegarder_joueur_du_tournoi_dans_db(liste_joueurs)
                                # question 'commencer le round ?'
                                while True:
                                    choix_commencer = input("Entrer 'y' pour commencer le round: ")
                                    try:
                                        if choix_commencer == "y" or choix_commencer == "Y":
                                            # debut du  premier round
                                            round_1 = controller.controller_round.creer_premier_round(tournoi.nom,
                                                                                                      tournoi.lieu)
                                            break
                                        else:
                                            print("Choix invalide !")
                                    except ValueError:
                                        print("Choix invalide !")
                                # question 'round fini ?'
                                while True:
                                    choix_fin = input("Entrer 'y' pour fin le round: ")
                                    try:
                                        if choix_fin == "y" or choix_fin == "Y":
                                            # fin du premier round
                                            round_1.ajouter_date_fin_round(tournoi.nom, tournoi.lieu)
                                            controller.controller_round.entrer_resultat_matchs(tournoi.nom, tournoi.lieu)
                                            for i in range(int(tournoi.nb_tour) - 1):
                                                # boucle sur nombre de round pour la suite
                                                round_suivant = controller.controller_round.creer_les_rounds_suivant(tournoi.nom, tournoi.lieu)
                                                input("Entrer quand le round est terminé")
                                                round_suivant.ajouter_date_fin_round(tournoi.nom, tournoi.lieu)
                                                controller.controller_round.entrer_resultat_matchs(tournoi.nom, tournoi.lieu)
                                                i += 1
                                            break
                                        else:
                                            print("Choix invalide !")
                                    except ValueError:
                                        print("Choix invalide !")
                                break
                            elif choix_tournoi == "2":
                                # reprendre tournoi
                                print(f"Je suis dans {choix_tournoi}")
                                break
                            elif choix_tournoi == 'r' or choix_tournoi == 'R':
                                # revenir au menu principal
                                break
                            else:
                                # message d'erreur
                                print("Choix invalide !")
                        except ValueError:
                            print("Choix invalide !")

                elif choix_principal == "2":
                    while True:
                        choix_joueur = input(f"{couleur.JAUNE}Entrer 1 pour enregistrer un joueur dans la base de données\nEntrer 2 modifier le classement \
d'un joueur\nEntrer 'r' pour revenir au menu principal\n{couleur.ROUGE}Entrer votre choix: {couleur.RESET}")
                        try:
                            if choix_joueur == "1":
                                # creer joueur
                                ControllerJoueur.creer_joueur(ControllerJoueur)
                                break
                            elif choix_joueur == "2":
                                # modifier classement joueur
                                controller = ControllerApp()
                                controller.controller_joueur.modifier_classement_joueur()
                                break
                            elif choix_joueur == 'r' or choix_joueur == 'R':
                                break
                            else:
                                # message d'erreur
                                print("Choix invalide !")
                        except ValueError:
                            print("Choix invalide")

                elif choix_principal == "3":
                    while True:
                        choix_rapport = input(f"{couleur.VIOLET}Entrer 1 pour voir tous les joueurs de la base de \
donnees\nEntrer 2 pour voir tous les joueurs d'un tournoi\nEntrer 3 pour voir tous les tournois\nEntrer 4 pour voir \
tous les tours d'un tournoi\nEntrer 5 pour voir tous les matchs d'un tournoi\nEntrer 'r' pour revenir au menu \
principal\n{couleur.ROUGE}Entrer votre choix: {couleur.RESET}")
                        try:
                            if choix_rapport == "1":
                                # tous les joueurs de bd
                                controller = ControllerApp()
                                controller.controller_rapport.afficher_rapport_acteurs()
                                break
                            elif choix_rapport == "2":
                                # tous les joueurs d'un tournoi
                                controller = ControllerApp()
                                controller.controller_rapport.afficher_joueurs_tournoi()
                                break
                            elif choix_rapport == "3":
                                # tous les tournois
                                controller = ControllerApp()
                                controller.controller_rapport.afficher_tous_les_tournois()
                                break
                            elif choix_rapport == "4":
                                # tous les tours d'un tournoi
                                controller = ControllerApp()
                                controller.controller_rapport.afficher_tous_tours_tournoi()
                                break
                            elif choix_rapport == "5":
                                # tous les matchs d'un tournoi
                                controller = ControllerApp()
                                controller.controller_rapport.afficher_tous_matchs_tournois()
                                break
                            elif choix_rapport == 'r' or choix_rapport == 'R':
                                break
                            else:
                                # message d'erreur
                                print("Choix invalide !")
                                pass
                        except ValueError:
                            print("Choix invalide !")
                elif choix_principal == 'q' or choix_principal == 'Q':
                    print("A bientot")
                    break
                else:
                    # message d'erreur
                    print("Choix invalide !")
            except ValueError:
                print("Choix invalide !")


def main():
    pass


if __name__ == "__main__":
    main()
