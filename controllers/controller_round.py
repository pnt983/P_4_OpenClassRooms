from vues.vue_round import VueRound
from models.round import Round
from . import controller_app
import time


class ControllerRound:

    def __init__(self):
        self.table_joueur_par_tournoi = controller_app.ControllerApp().table_joueur_par_tournoi
        self.table_rounds_par_tournoi = controller_app.ControllerApp().table_rounds_par_tournoi
        self.query = controller_app.ControllerApp().user

    def creer_premier_round(self, nom_tournoi, lieu_tournoi):
        round = Round()
        deserialisation_joueur = round.deserialiser_joueurs(nom_tournoi, lieu_tournoi)
        liste_joueurs = round.classer_par_classement(deserialisation_joueur)
        matchs = round.premieres_paires(nom_tournoi, lieu_tournoi, liste_joueurs)
        VueRound.afficher_debut_round(VueRound, round.nom, round.date_debut, round.heure_debut)
        return matchs, round.nom

    def creer_les_rounds_suivant(self, nom_tournoi, lieu_tournoi):
        round = Round()
        deserialisation_joueur = round.deserialiser_joueurs(nom_tournoi, lieu_tournoi)
        liste_joueurs = round.classer_par_score(deserialisation_joueur)
        matchs = round.generer_paires(nom_tournoi, lieu_tournoi, liste_joueurs)
        VueRound.afficher_debut_round(VueRound, round.nom, round.date_debut, round.heure_debut)
        return matchs, round.nom

    def fin_round(self, nom_tournoi, lieu_tournoi, nom_round):
        date = time.strftime("%A %d %B %Y")
        heure = time.strftime("%X")
        Round.ajouter_date_fin_round(Round, nom_tournoi, lieu_tournoi, nom_round, date, heure)
        VueRound.afficher_fin_round(VueRound, nom_round, date, heure)
        self.entrer_resultat_matchs(self, nom_tournoi, nom_round)

    def entrer_resultat_matchs(self, nom_tournoi, nom_round):
        """Permet au gestionnaire de rentrer les resultats. Ils sont ensuite enregistrés
        dans la db 'table_joueur_par_tournoi'"""
        acces_db = controller_app.ControllerApp().table_rounds_par_tournoi.search(controller_app.ControllerApp().user.
                                                        nom_du_tournoi == nom_tournoi and controller_app.ControllerApp().user.
                                                        nom_round == nom_round)  # Voir avec Olivier, je ne sais pas pourquoi self.query et self.table ne marche pas ?
        for matchs in acces_db:
            recuperation_matchs = matchs['matchs_du_round']
        for joueur in recuperation_matchs:
            VueRound.montrer_message(VueRound, joueur)
            choix_gagnant = VueRound.qui_gagne(VueRound)
            if choix_gagnant == 1:
                joueur_1 = joueur[0]
                score = 1
                Round.ajouter_points_joueur(Round, joueur_1, nom_tournoi, score)
            elif choix_gagnant == 2:
                joueur_2 = joueur[1]
                score = 1
                Round.ajouter_points_joueur(Round, joueur_2, nom_tournoi, score)
            elif choix_gagnant == 3:
                joueur_1 = joueur[0]
                score = 0.5
                Round.ajouter_points_joueur(Round, joueur_1, nom_tournoi, score)
                joueur_2 = joueur[1]
                score = 0.5
                Round.ajouter_points_joueur(Round, joueur_2, nom_tournoi, score)
