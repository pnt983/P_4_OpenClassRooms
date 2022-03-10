from models.rapport import Rapport
from vues.vue_rapport import VueRapport
import utilitaires.menu as menu


class ControllerRapport:

    def __init__(self, db_table_joueur, db_table_tournoi, requete):
        self.rapport = None
        self.query = requete
        self.table_joueur = db_table_joueur
        self.table_tournoi = db_table_tournoi

    def afficher_rapport_acteurs(self):
        """Affiche le rapport de tous les joueurs de la base de données"""
        self.rapport = Rapport(self.table_joueur, self.table_tournoi, self.query)
        table_joueurs = self.rapport.recuperer_table_joueur()
        choix_utilisateur = VueRapport.choisir_alphabetique_ou_classement()
        if choix_utilisateur == 1:
            liste_ordre_alphabetique = self.rapport.classer_par_ordre_alphabetique(table_joueurs)
            VueRapport.montrer_message(liste_ordre_alphabetique)
            return liste_ordre_alphabetique
        elif choix_utilisateur == 2:
            liste_classement = self.rapport.classer_par_classement(table_joueurs)
            VueRapport.montrer_message(liste_classement)
            return liste_classement
        else:
            VueRapport.afficher_message_erreur()

    def afficher_joueurs_tournoi(self):
        """Affiche les joueurs d'un tournoi par ordre alphabetique ou par classement"""
        self.rapport = Rapport(self.table_joueur, self.table_tournoi, self.query)
        table_tournoi = self.rapport.recuperer_nom_tournois()
        if not table_tournoi:
            print("\nIl n'y a pas encore de tournois dans les rapports")
        else:
            VueRapport.montrer_message(table_tournoi)
            nom_tournoi = VueRapport.entrer_nom_tournoi()
            lieu_tournoi = VueRapport.entrer_lieu_tournoi()

            liste_joueurs = self.rapport.recuperer_joueurs_tournoi(nom_tournoi, lieu_tournoi)
            choix_utilisateur = VueRapport.choisir_alphabetique_ou_classement()
            if choix_utilisateur == 1:
                liste_ordre_alphabetique = self.rapport.classer_par_ordre_alphabetique(liste_joueurs)
                VueRapport.montrer_message(liste_ordre_alphabetique)
                return liste_ordre_alphabetique
            elif choix_utilisateur == 2:
                liste_classement = self.rapport.classer_par_classement(liste_joueurs)
                VueRapport.montrer_message(liste_classement)
                return liste_classement
            else:
                VueRapport.afficher_message_erreur()

    def afficher_tous_les_tournois(self):
        self.rapport = Rapport(self.table_joueur, self.table_tournoi, self.query)
        table_tournoi = self.rapport.recuperer_table_tournoi()
        if not table_tournoi:
            print("\nIl n'y a pas encore de tournois dans les rapports")
        else:
            VueRapport.montrer_message(table_tournoi)

    def afficher_tous_tours_tournoi(self):
        self.rapport = Rapport(self.table_joueur, self.table_tournoi, self.query)
        table_tournoi = self.rapport.recuperer_nom_tournois()
        if not table_tournoi:
            print("\nIl n'y a pas encore de tours dans les rapports")
        else:
            VueRapport.montrer_message(table_tournoi)
            nom_tournoi = VueRapport.entrer_nom_tournoi()
            lieu_tournoi = VueRapport.entrer_lieu_tournoi()
            table_rounds = self.rapport.recuperer_rounds_tournoi(nom_tournoi, lieu_tournoi)
            VueRapport.montrer_message(table_rounds)

    def afficher_tous_matchs_tournois(self):
        self.rapport = Rapport(self.table_joueur, self.table_tournoi, self.query)
        table_tournoi = self.rapport.recuperer_nom_tournois()
        if not table_tournoi:
            print("\nIl n'y a pas encore de match dans les rapports")
        else:
            VueRapport.montrer_message(table_tournoi)
            nom_tournoi = VueRapport.entrer_nom_tournoi()
            lieu_tournoi = VueRapport.entrer_lieu_tournoi()
            recuperer_matchs = self.rapport.recuperer_matchs_tournoi(nom_tournoi, lieu_tournoi)
            VueRapport.montrer_message(recuperer_matchs)

    def gerer_rapports(self):
        """ Gére la gestion des rapports dans le menu principal"""
        while True:
            menu_rapport = menu.Menu("Menu rapport", menu.option_rapport)
            choix_rapport = menu_rapport.afficher()
            if choix_rapport == "1":
                self.afficher_rapport_acteurs()
            elif choix_rapport == "2":
                self.afficher_joueurs_tournoi()
            elif choix_rapport == "3":
                self.afficher_tous_les_tournois()
            elif choix_rapport == "4":
                self.afficher_tous_tours_tournoi()
            elif choix_rapport == "5":
                self.afficher_tous_matchs_tournois()
            elif choix_rapport == "6":
                print("Retour en arriere")
                break
            else:
                print("Choix invalide !")
                pass
