from vues.vue_round import VueRound
from models.round import Round
import database
import time


class ControllerRound:

    def __init__(self):
        self.round = None
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI
        self.table_rounds_par_tournoi = database.TABLE_ROUND_PAR_TOURNOI
        self.user = database.USER

    def creer_premier_round(self, nom_tournoi, lieu_tournoi):
        self.round = Round()
        deserialisation_joueur = self.round.deserialiser_joueurs(nom_tournoi, lieu_tournoi)
        liste_joueurs = self.round.classer_par_classement(deserialisation_joueur)
        matchs = self.round.premieres_paires(nom_tournoi, lieu_tournoi, liste_joueurs)
        VueRound.afficher_debut_round(VueRound, self.round.nom, self.round.date)
        # return matchs, round.nom
        return self.round

    def creer_les_rounds_suivant(self, nom_tournoi, lieu_tournoi):
        self.round = Round()
        deserialisation_joueur = self.round.deserialiser_joueurs(nom_tournoi, lieu_tournoi)
        liste_joueurs = self.round.classer_par_score(deserialisation_joueur)
        matchs = self.round.generer_paires(nom_tournoi, lieu_tournoi, liste_joueurs)
        VueRound.afficher_debut_round(VueRound, self.round.nom, self.round.date)
        # return matchs, round.nom
        return self.round

    def fin_round(self, nom_tournoi, lieu_tournoi, nom_round):
        date = time.strftime("%A %d %B %Y")
        heure = time.strftime("%X")
        Round.ajouter_date_fin_round(Round, nom_tournoi, lieu_tournoi, nom_round, date, heure)
        VueRound.afficher_fin_round(VueRound, nom_round, date, heure)
        self.entrer_resultat_matchs(self, nom_tournoi, nom_round)

    def entrer_resultat_matchs(self, nom_tournoi, lieu_tournoi):
        """Permet au gestionnaire de rentrer les resultats. Ils sont ensuite enregistrés
        dans la db 'table_joueur_par_tournoi'"""
        acces_db = acces_db = self.table_rounds_par_tournoi.search(self.user.nom_du_tournoi == nom_tournoi and self.
                                                                   user.nom_round == self.round.nom)
        for matchs in acces_db:
            recuperation_matchs = matchs['matchs_du_round']
        for joueur in recuperation_matchs:
            VueRound.montrer_message(VueRound, joueur)
            choix_gagnant = VueRound.qui_gagne(VueRound)
            if choix_gagnant == 1: 
                joueur_1 = joueur[0]
                score = 1
                Round.enregistrer_points_joueur(Round, joueur_1, nom_tournoi, lieu_tournoi, score)
            elif choix_gagnant == 2:
                joueur_2 = joueur[1]
                score = 1
                Round.enregistrer_points_joueur(Round, joueur_2, nom_tournoi, lieu_tournoi, score)
            elif choix_gagnant == 3:
                joueur_1 = joueur[0]
                score = 0.5
                Round.enregistrer_points_joueur(Round, joueur_1, nom_tournoi, lieu_tournoi, score)
                joueur_2 = joueur[1]
                score = 0.5
                Round.enregistrer_points_joueur(Round, joueur_2, nom_tournoi, lieu_tournoi, score)
