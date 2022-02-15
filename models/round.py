from vues.vue_round import VueRound
import datetime
from itertools import islice
from operator import itemgetter


class Round:
    """ Creation des tours pour le tournoi"""

    compteur_round = 0
    liste_des_matchs = []

    def __init__(self, nom=None, date_debut_round=None, date_fin_round=None, etat_round=None, matchs_round=None):
        self.date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.date_fin = "En_cours"
        self.avancer_round = "En_cours"
        self.nom = VueRound.nom(VueRound)
        self.match = []
        Round.compteur_round += 1

    def premieres_paires(self, liste_joueurs):
        " Classe les joueurs par meilleur classement et divise la liste en deux pour les associer"
        self.liste_des_matchs.clear()
        liste_a_classer = liste_joueurs
        liste_matchs = []
        separation_liste = len(liste_a_classer) / 2
        for premier, deuxieme in zip(liste_a_classer, islice(liste_a_classer, int(separation_liste), None)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
        return liste_matchs

    def generer_paires(self, liste_joueurs):   # Revoir pour si un match est en double
        """Cree des matchs par rapport au score des joueurs"""
        liste_matchs = []
        for premier, deuxieme in zip(islice(liste_joueurs, 0, None, 2), islice(liste_joueurs, 1, None, 2)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
        return liste_matchs

    def serialiser_round(self):
        liste_matchs_serialise = []
        for row in self.liste_des_matchs[1]:
            joueur_serialise = [joueur.serialiser_joueur() for joueur in row]
            liste_matchs_serialise.append(joueur_serialise)
        serialise = {
            "nom_round": self.nom,
            "date_debut_round": self.date,
            "date_fin_round": self.date_fin,
            "etat_round": self.avancer_round,
            "matchs_round": liste_matchs_serialise
        }
        return serialise

    @classmethod
    def deserialiser_round(cls, infos_round):
        nom = infos_round["nom_round"]
        date_debut_round = infos_round["date_debut_round"]
        date_fin_round = infos_round["date_fin_round"]
        etat_round = infos_round["etat_round"]
        matchs_round = infos_round["matchs_round"]
        round = Round(nom, date_debut_round, date_fin_round, etat_round, matchs_round)
        return round

    def ajouter_date_fin_round(self):
        self.date_fin = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        return self.date_fin

    def cloturer_round(self):
        self.avancer_round = "Round completement fini"
        return self.avancer_round

    def classer_par_ordre_alphabetique(self, liste_joueurs):
        liste_par_alphabet = sorted(liste_joueurs, key=itemgetter(0), reverse=True)
        return liste_par_alphabet

    def classer_par_classement(self, liste_joueurs):
        liste_par_classement = sorted(liste_joueurs, key=lambda joueur: joueur.classement_joueur, reverse=True)
        return liste_par_classement

    def classer_par_score(self, liste_joueurs):
        liste_par_score = sorted(liste_joueurs, key=lambda joueur: joueur.score, reverse=True)
        return liste_par_score


def main():
    pass


if __name__ == "__main__":
    main()
