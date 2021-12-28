from . import tournoi
from . import joueur
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

    def premieres_paires(self, nom_tournoi):
        " Classe les joueurs par meilleur classement et divise la liste en deux pour les associer"
        liste_classe = self.classer_joueurs(nom_tournoi)
        for premier, deuxieme in zip(liste_classe, islice(liste_classe, 4, None)):
            matchs = (premier, deuxieme)
            self.enregistrer_round_dans_db(nom_tournoi, matchs)

    def generer_paires(self):   # En cours
        """Cree des matchs par rapport au score des joueurs"""
        liste_joueurs = self.classer_joueurs("World,Vegas")
        for premier, deuxieme in zip(islice(liste_joueurs, 0, None, 2), islice(liste_joueurs, 1, None, 2)):
            print(premier, deuxieme)

    def enregistrer_round_dans_db(self, nom_tournoi, matchs_recuperer):
        """ Enregistre le nom du tournoi, le nom du round et les matchs du round dans
        la table 'table_rounds_par_tournois' """
        matchs = matchs_recuperer
        serialise_joueur = {
            "nom_du_tournoi": nom_tournoi,
            "nom_round": self.nom,
            "matchs_du_round": matchs
        }
        table_rounds_par_tournoi.insert(serialise_joueur)
        return serialise_joueur

    def stocker_liste_des_matchs(self):
        pass

    def classer_joueurs(self, nom_tournoi):
        """ Recupere la liste de la table 'table_joueur_par_tournoi' dans la db par
        rapport au nom du tournoi et les classes par rapport au classement, a l'ordre alphabetique
        ou au score"""
        liste_joueurs = []
        choix_du_classement = VueRound.choix_pour_classer(VueRound)
        liste_du_tournoi = table_joueur_par_tournoi.search(user.nom_du_tournoi == nom_tournoi)
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

    def entrer_resultat_matchs(self, nom_tournoi, nom_round):
        """Permet au gestionnaire de rentrer les resultats. Ils sont ensuite enregistrés
        dans la db 'table_joueur_par_tournoi' """
        acces_db = table_rounds_par_tournoi.search(user.nom_du_tournoi == nom_tournoi and user.nom_round == nom_round)
        for matchs in acces_db:
            print(matchs['matchs_du_round'])
            choix_gagnant = VueRound.qui_gagne(VueRound)
            if choix_gagnant == 1:
                joueur_1 = matchs['matchs_du_round'][0]
                joueur_1[5] += 1
                table_rounds_par_tournoi.update({"score": joueur_1[5]}, user.nom == joueur_1[0])
                table_joueur_tournoi = table_joueur_par_tournoi.search(
                    user.nom_du_tournoi == nom_tournoi and user.
                    nom == joueur_1[0] and user.prenom == joueur_1[1])
                for row in table_joueur_tournoi:
                    row["score"] += 1
                    table_joueur_par_tournoi.update({"score": row["score"]}, user.nom == joueur_1[0])
            elif choix_gagnant == 2:
                joueur_2 = matchs['matchs_du_round'][1]
                joueur_2[5] += 1
                table_rounds_par_tournoi.update({"score": joueur_2[5]}, user.nom == joueur_2[0])
                table_joueur_tournoi = table_joueur_par_tournoi.search(
                    user.nom_du_tournoi == nom_tournoi and user.
                    nom == joueur_2[0] and user.prenom == joueur_2[1])
                for row in table_joueur_tournoi:
                    row["score"] += 1
                    table_joueur_par_tournoi.update({"score": row["score"]}, user.nom == joueur_2[0])
            elif choix_gagnant == 3:
                joueur_1 = matchs['matchs_du_round'][0]
                joueur_1[5] += 0.5
                table_rounds_par_tournoi.update({"score": joueur_1[5]}, user.nom == joueur_1[0])
                table_joueur_tournoi = table_joueur_par_tournoi.search(
                    user.nom_du_tournoi == nom_tournoi and user.nom == joueur_1[0] and user.prenom == joueur_1[1])
                for row in table_joueur_tournoi:
                    row["score"] += 0.5
                    table_joueur_par_tournoi.update({"score": row["score"]}, user.nom == joueur_1[0])
                joueur_2 = matchs['matchs_du_round'][1]
                joueur_2[5] += 0.5
                table_rounds_par_tournoi.update({"score": joueur_2[5]}, user.nom == joueur_2[0])
                table_joueur_tournoi = table_joueur_par_tournoi.search(
                    user.nom_du_tournoi == nom_tournoi and user.nom == joueur_2[0] and user.prenom == joueur_2[1])
                for row in table_joueur_tournoi:
                    row["score"] += 0.5
                    table_joueur_par_tournoi.update({"score": row["score"]}, user.nom == joueur_2[0])

    def resultat_round(self):
        pass


def main():
    round_1 = Round()
    round_1.premieres_paires("World,Vegas")
    round_1.entrer_resultat_matchs("World,Vegas", "Round 1")
    round_2 = Round()
    round_2.generer_paires()
    round_2.entrer_resultat_matchs("World,Vegas", "Round 2")
    round_3 = Round()
    round_3.generer_paires()
    round_3.entrer_resultat_matchs("World,Vegas", "Round 3")


if __name__ == "__main__":
    main()
