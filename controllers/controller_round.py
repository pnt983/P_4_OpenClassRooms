from vues.vue_round import VueRound
from models.round import Round
from models import round
import time


class ControllerRound:

    def __init__(self):
        pass

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
        return matchs

    def fin_round(self, nom_tournoi, nom_round):
        date = time.strftime("%A %d %B %Y")
        heure = time.strftime("%X")
        VueRound.afficher_fin_round(VueRound, nom_round, date, heure)
        self.entrer_resultat_matchs(nom_tournoi, nom_round)

    def entrer_resultat_matchs(self, nom_tournoi, nom_round):
        """Permet au gestionnaire de rentrer les resultats. Ils sont ensuite enregistrés
        dans la db 'table_joueur_par_tournoi'"""
        acces_db = round.table_rounds_par_tournoi.search(round.user.nom_du_tournoi == nom_tournoi and round.
                                                         user.nom_round == nom_round)
        for matchs in acces_db:
            print(matchs['matchs_du_round'])
            choix_gagnant = VueRound.qui_gagne(VueRound)
            if choix_gagnant == 1:
                joueur_1 = matchs['matchs_du_round'][0]
                joueur_1[5] += 1
                Round.ajouter_points_joueur(Round, joueur_1, nom_tournoi)
            elif choix_gagnant == 2:
                joueur_2 = matchs['matchs_du_round'][1]
                joueur_2[5] += 1
                Round.ajouter_points_joueur(Round, joueur_2, nom_tournoi)
            elif choix_gagnant == 3:
                joueur_1 = matchs['matchs_du_round'][0]
                joueur_1[5] += 0.5
                Round.ajouter_points_joueur(Round, joueur_1, nom_tournoi)
                joueur_2 = matchs['matchs_du_round'][1]
                joueur_2[5] += 0.5
                Round.ajouter_points_joueur(Round, joueur_2, nom_tournoi)
