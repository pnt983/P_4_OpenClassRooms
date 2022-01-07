from vues.vue_round import VueRound
from controllers import controller_round as c_r
import time
from itertools import islice
from operator import itemgetter


class Round:
    """ Creation des tours pour le tournoi"""

    def __init__(self):
        self.date_debut = time.strftime("%A %d %B %Y")
        self.heure_debut = time.strftime("%X")
        self.nom = VueRound.nom(VueRound)

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
            "date_debut_round": self.date_debut,
            "heure_debut_round": self.heure_debut,
            "date_fin_round": "Le round n'est pas encore fini",
            "heure_fin_round": "Le round n'est pas encore fini"
        }
        c_r.ControllerRound().table_rounds_par_tournoi.insert(serialise_joueur)
        return serialise_joueur

    def ajouter_points_joueur(self, joueur, nom_tournoi):
        c_r.ControllerRound().table_rounds_par_tournoi.update({"score": joueur[5]},
                                                              c_r.ControllerRound().query.nom == joueur[0])
        
        table_joueur_tournoi = c_r.ControllerRound().table_joueur_par_tournoi.search(c_r.ControllerRound().query.nom_du_tournoi == nom_tournoi and c_r.ControllerRound().query.
                                        nom == joueur[0] and c_r.ControllerRound().query.prenom == joueur[1])
        for row in table_joueur_tournoi:
            row["score"] += 1
            c_r.ControllerRound().table_joueur_par_tournoi.update({"score": row["score"]},
                                                                  c_r.ControllerRound().query.nom == joueur[0])

    def deserialiser_joueurs(self, nom_tournoi, lieu_tournoi):
        """ Recupere la liste de la table 'table_joueur_par_tournoi' dans la db par
        rapport au nom du tournoi"""
        liste_joueurs = []
        liste_du_tournoi = c_r.ControllerRound().table_joueur_par_tournoi.search(c_r.ControllerRound().
                                                                                 query.nom_du_tournoi == nom_tournoi + "," + lieu_tournoi)
        for row in liste_du_tournoi:
            deserialise_joueur = [
                row["nom"],
                row["prenom"],
                row["naissance"],
                row["sexe"],
                row["classement"],
                row["score"]
            ]
            liste_joueurs.append(deserialise_joueur)
        return liste_joueurs

    def ajouter_date_fin_round(self, nom_tournoi, lieu_tournoi, nom_round, date, heure):
        c_r.ControllerRound().table_rounds_par_tournoi.update({"date_fin_round": date, "heure_fin_round": heure},
                                                              c_r.ControllerRound().query.nom_du_tournoi == nom_tournoi + "," + lieu_tournoi and c_r.
                                                              ControllerRound().query.nom_round == nom_round)

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
