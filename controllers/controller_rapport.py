from cgi import test
import database
from models.rapport import Rapport
from vues.vue_rapport import VueRapport


class ControllerRapport:

    def __init__(self, essai):
        self.essai = essai
        self.query = database.USER
        self.table_joueur = database.TABLE_JOUEUR
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI
        self.table_rounds_par_tournoi = database.TABLE_ROUND_PAR_TOURNOI

    def afficher_rapport_acteurs(self):
        table_joueurs = Rapport.recuperer_table_joueur(Rapport)
        choix_utilisateur = VueRapport.choisir_alphabetique_ou_classement(VueRapport)
        if choix_utilisateur == 1:
            liste_ordre_alphabetique = Rapport.classer_par_ordre_alphabetique(Rapport, table_joueurs)
            VueRapport.montrer_message(VueRapport, liste_ordre_alphabetique)
            return liste_ordre_alphabetique
        elif choix_utilisateur == 2:
            liste_classement = Rapport.classer_par_classement(Rapport, table_joueurs)
            VueRapport.montrer_message(VueRapport, liste_classement)
            return liste_classement
        else:
            VueRapport.message_erreur(VueRapport)

    def afficher_joueurs_tournoi(self):
        table_tournoi = Rapport.recuperer_nom_tournois(Rapport)
        VueRapport.montrer_message(VueRapport, table_tournoi)
        nom_tournoi = VueRapport.entrer_nom_tournoi(VueRapport)
        lieu_tournoi = VueRapport.entrer_lieu_tournoi(VueRapport)

        table_joueur_par_tournoi = Rapport.recuperer_joueurs_tournoi(Rapport, nom_tournoi, lieu_tournoi)
        choix_utilisateur = VueRapport.choisir_alphabetique_ou_classement(VueRapport)
        if choix_utilisateur == 1:
            liste_ordre_alphabetique = Rapport.classer_par_ordre_alphabetique(Rapport, table_joueur_par_tournoi, 1)
            VueRapport.montrer_message(VueRapport, liste_ordre_alphabetique)
            return liste_ordre_alphabetique
        elif choix_utilisateur == 2:
            liste_classement = Rapport.classer_par_classement(Rapport, table_joueur_par_tournoi, 5)
            VueRapport.montrer_message(VueRapport, liste_classement)
            return liste_classement
        else:
            VueRapport.message_erreur(VueRapport)

    def afficher_tous_les_tournois(self):
        table_tournoi = Rapport.recuperer_table_tournoi(Rapport)
        VueRapport.montrer_message(VueRapport, table_tournoi)

    def afficher_tous_tours_tournoi(self):
        table_tournoi = Rapport.recuperer_nom_tournois(Rapport)
        VueRapport.montrer_message(VueRapport, table_tournoi)
        nom_tournoi = VueRapport.entrer_nom_tournoi(VueRapport)
        lieu_tournoi = VueRapport.entrer_lieu_tournoi(VueRapport)
        table_rounds = Rapport.recuperer_rounds_tournoi(Rapport, nom_tournoi, lieu_tournoi)
        VueRapport.montrer_message(VueRapport, table_rounds)

    def afficher_tous_matchs_tournois(self):
        table_tournoi = Rapport.recuperer_nom_tournois(Rapport)
        VueRapport.montrer_message(VueRapport, table_tournoi)
        nom_tournoi = VueRapport.entrer_nom_tournoi(VueRapport)
        lieu_tournoi = VueRapport.entrer_lieu_tournoi(VueRapport)
        recuperer_matchs = Rapport.recuperer_matchs_tournoi(Rapport, nom_tournoi, lieu_tournoi)
        VueRapport.montrer_message(VueRapport, recuperer_matchs)
