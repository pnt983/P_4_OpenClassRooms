from cgi import test
import database
from models.rapport import Rapport
from vues.vue_rapport import VueRapport


class ControllerRapport:

    def __init__(self):
        self.rapport = None
        self.query = database.USER
        self.table_joueur = database.TABLE_JOUEUR
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI
        self.table_rounds_par_tournoi = database.TABLE_ROUND_PAR_TOURNOI

    def afficher_rapport_acteurs(self):
        self.rapport = Rapport()
        table_joueurs = self.rapport.recuperer_table_joueur()
        choix_utilisateur = VueRapport.choisir_alphabetique_ou_classement(VueRapport)
        if choix_utilisateur == 1:
            liste_ordre_alphabetique = self.rapport.classer_par_ordre_alphabetique(table_joueurs)
            VueRapport.montrer_message(VueRapport, liste_ordre_alphabetique)
            return liste_ordre_alphabetique
        elif choix_utilisateur == 2:
            liste_classement = self.rapport.classer_par_classement(table_joueurs)
            VueRapport.montrer_message(VueRapport, liste_classement)
            return liste_classement
        else:
            VueRapport.message_erreur(VueRapport)

    def afficher_joueurs_tournoi(self):
        self.rapport = Rapport()
        table_tournoi = self.rapport.recuperer_nom_tournois()
        VueRapport.montrer_message(VueRapport, table_tournoi)
        nom_tournoi = VueRapport.entrer_nom_tournoi(VueRapport)
        lieu_tournoi = VueRapport.entrer_lieu_tournoi(VueRapport)

        table_joueur_par_tournoi = self.rapport.recuperer_joueurs_tournoi(nom_tournoi, lieu_tournoi)
        choix_utilisateur = VueRapport.choisir_alphabetique_ou_classement(VueRapport)
        if choix_utilisateur == 1:
            liste_ordre_alphabetique = self.rapport.classer_par_ordre_alphabetique(table_joueur_par_tournoi, 1)
            VueRapport.montrer_message(VueRapport, liste_ordre_alphabetique)
            return liste_ordre_alphabetique
        elif choix_utilisateur == 2:
            liste_classement = self.rapport.classer_par_classement(table_joueur_par_tournoi, 5)
            VueRapport.montrer_message(VueRapport, liste_classement)
            return liste_classement
        else:
            VueRapport.message_erreur(VueRapport)

    def afficher_tous_les_tournois(self):
        self.rapport = Rapport()
        table_tournoi = self.rapport.recuperer_table_tournoi()
        VueRapport.montrer_message(VueRapport, table_tournoi)

    def afficher_tous_tours_tournoi(self):
        self.rapport = Rapport()
        table_tournoi = self.rapport.recuperer_nom_tournois()
        VueRapport.montrer_message(VueRapport, table_tournoi)
        nom_tournoi = VueRapport.entrer_nom_tournoi(VueRapport)
        lieu_tournoi = VueRapport.entrer_lieu_tournoi(VueRapport)
        table_rounds = self.rapport.recuperer_rounds_tournoi(nom_tournoi, lieu_tournoi)
        VueRapport.montrer_message(VueRapport, table_rounds)

    def afficher_tous_matchs_tournois(self):
        self.rapport = Rapport()
        table_tournoi = self.rapport.recuperer_nom_tournois()
        VueRapport.montrer_message(VueRapport, table_tournoi)
        nom_tournoi = VueRapport.entrer_nom_tournoi(VueRapport)
        lieu_tournoi = VueRapport.entrer_lieu_tournoi(VueRapport)
        recuperer_matchs = self.rapport.recuperer_matchs_tournoi(nom_tournoi, lieu_tournoi)
        VueRapport.montrer_message(VueRapport, recuperer_matchs)
