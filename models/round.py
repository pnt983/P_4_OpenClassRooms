from vues.vue_round import VueRound
from tinydb import TinyDB, Query
import time
from itertools import islice, repeat
from operator import itemgetter

db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


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
            self.enregistrer_round_dans_db(nom_tournoi, lieu_tournoi, matchs)
        return liste_matchs

    def generer_paires(self, nom_tournoi, lieu_tournoi):   # En cours
        """Cree des matchs par rapport au score des joueurs"""
        liste_joueurs = self.classer_joueurs(nom_tournoi, lieu_tournoi)
        for premier, deuxieme in zip(islice(liste_joueurs, 0, None, 2), islice(liste_joueurs, 1, None, 2)):
            print(premier, deuxieme)

    def enregistrer_round_dans_db(self, nom_tournoi, lieu_tournoi, matchs_recuperer):
        """ Enregistre le nom du tournoi, le nom du round et les matchs du round dans
        la table 'table_rounds_par_tournois' """
        matchs = matchs_recuperer
        serialise_joueur = {
            "nom_du_tournoi": nom_tournoi + "," + lieu_tournoi,
            "nom_round": self.nom,
            "matchs_du_round": matchs,
            "date": self.date_debut,
            "heure": self.heure_debut
        }
        table_rounds_par_tournoi.insert(serialise_joueur)
        return serialise_joueur

    def ajouter_points_joueur(self, joueur, nom_tournoi):
        table_rounds_par_tournoi.update({"score": joueur[5]}, user.nom == joueur[0])
        table_joueur_tournoi = table_joueur_par_tournoi.search(
            user.nom_du_tournoi == nom_tournoi and user.
            nom == joueur[0] and user.prenom == joueur[1])
        for row in table_joueur_tournoi:
            row["score"] += 1
            table_joueur_par_tournoi.update({"score": row["score"]}, user.nom == joueur[0])

    def classer_joueurs(self, nom_tournoi, lieu_tournoi, choix_classment):
        """ Recupere la liste de la table 'table_joueur_par_tournoi' dans la db par
        rapport au nom du tournoi et les classes par rapport au classement, a l'ordre alphabetique
        ou au score"""
        liste_joueurs = []
        choix_du_classement = choix_classment
        liste_du_tournoi = table_joueur_par_tournoi.search(user.nom_du_tournoi == nom_tournoi + "," + lieu_tournoi)
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
        if choix_du_classement == 1:
            liste_par_classement = sorted(liste_joueurs, key=itemgetter(4), reverse=True)
            return liste_par_classement
        elif choix_du_classement == 2:
            liste_par_ordre_alphabetique = sorted(liste_joueurs, key=itemgetter(0))
            return liste_par_ordre_alphabetique
        elif choix_du_classement == 3:
            liste_par_score = sorted(liste_joueurs, key=itemgetter(5), reverse=True)
            return liste_par_score
        else:
            print("Le choix est invalide")
        return liste_joueurs


def main():
    pass


if __name__ == "__main__":
    main()
