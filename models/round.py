from vues.vue_round import VueRound
import database
import datetime
from itertools import islice
from operator import itemgetter


class Round:
    """ Creation des tours pour le tournoi"""

    def __init__(self):
        self.date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.nom = VueRound.nom(VueRound)
        self.table_rounds_par_tournoi = database.TABLE_ROUND_PAR_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI
        self.user = database.USER

    def premieres_paires(self, nom_tournoi, lieu_tournoi, liste_joueurs):
        " Classe les joueurs par meilleur classement et divise la liste en deux pour les associer"
        liste_a_classer = liste_joueurs
        liste_matchs = []
        separation_liste = len(liste_a_classer) / 2
        for premier, deuxieme in zip(liste_a_classer, islice(liste_a_classer, int(separation_liste), None)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
        self.enregistrer_round_dans_db(nom_tournoi, lieu_tournoi, liste_matchs)
        return liste_matchs

    def generer_paires(self, nom_tournoi, lieu_tournoi, liste_joueurs):   # Revoir pour si un match est en double
        """Cree des matchs par rapport au score des joueurs"""
        liste_matchs = []
        for premier, deuxieme in zip(islice(liste_joueurs, 0, None, 2), islice(liste_joueurs, 1, None, 2)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
        self.enregistrer_round_dans_db(nom_tournoi, lieu_tournoi, liste_matchs)
        return liste_matchs

    def enregistrer_round_dans_db(self, nom_tournoi, lieu_tournoi, matchs_recuperer):
        """ Enregistre le nom du tournoi, le nom du round et les matchs du round dans
        la table 'table_rounds_par_tournois' """
        matchs = matchs_recuperer
        serialise_joueur = {
            "nom_du_tournoi": nom_tournoi + "," + lieu_tournoi,
            "nom_round": self.nom,
            "matchs_du_round": matchs,
            "date_debut_round": self.date,
            "date_fin_round": "Le round n'est pas encore fini"
        }
        self.table_rounds_par_tournoi.insert(serialise_joueur)
        return serialise_joueur

    def enregistrer_points_joueur(self, joueur, nom_tournoi, lieu_tournoi, score):   # revoir pourquoi 'self' ne marche pas
        table_joueur_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI.search(database.USER.nom_du_tournoi == nom_tournoi + "," + lieu_tournoi and database.USER.nom == joueur[0])
        for row in table_joueur_tournoi:
            row["score"] += score
            database.TABLE_JOUEUR_PAR_TOURNOI.update({"score": row["score"]}, database.USER.
                                                       nom_du_tournoi == nom_tournoi + "," + lieu_tournoi and database.
                                                       USER.nom == joueur[0])

    def deserialiser_joueurs(self, nom_tournoi, lieu_tournoi):
        """ Recupere la liste de la table 'table_joueur_par_tournoi' dans la db par
        rapport au nom du tournoi"""
        liste_joueurs = []
        liste_du_tournoi = self.table_joueur_par_tournoi.search(self.user.
                                                                nom_du_tournoi == nom_tournoi + "," + lieu_tournoi)
        for joueur in liste_du_tournoi:
            deserialise_joueur = [
                joueur["nom"],
                joueur["prenom"],
                joueur["naissance"],
                joueur["sexe"],
                joueur["classement"],
                joueur["score"]
            ]
            liste_joueurs.append(deserialise_joueur)
        return liste_joueurs

    def ajouter_date_fin_round(self, nom_tournoi, lieu_tournoi):
        date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.table_rounds_par_tournoi.update({"date_fin_round": date}, self.user.
                                             nom_du_tournoi == nom_tournoi + "," + lieu_tournoi and self.user.
                                             nom_round == self.nom)

    def classer_par_ordre_alphabetique(self, liste_joueurs):
        liste_par_alphabet = sorted(liste_joueurs, key=itemgetter(0), reverse=True)
        return liste_par_alphabet

    def classer_par_classement(self, liste_joueurs):
        liste_par_classement = sorted(liste_joueurs, key=itemgetter(4), reverse=True)
        return liste_par_classement

    def classer_par_score(self, liste_joueurs):
        liste_par_score = sorted(liste_joueurs, key=itemgetter(5), reverse=True)
        return liste_par_score


def main():
    pass


if __name__ == "__main__":
    main()
