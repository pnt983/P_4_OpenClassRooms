import database
from operator import itemgetter


class Rapport:

    def __init__(self):
        self.user = database.USER
        self.table_joueur = database.TABLE_JOUEUR
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI
        self.table_rounds_par_tournoi = database.TABLE_ROUND_PAR_TOURNOI

    def recuperer_table_joueur(self):
        joueur_dans_db = self.table_joueur.all()
        liste_joueurs = []
        for joueur in joueur_dans_db:
            deserialise = [
                joueur["nom"],
                joueur["prenom"],
                joueur["naissance"],
                joueur["sexe"],
                joueur["classement"]
            ]
            liste_joueurs.append(deserialise)
        return liste_joueurs

    def recuperer_joueurs_tournoi(self, nom_tournoi, lieu_tournoi):
        joueur_par_tournoi = self.table_joueur_par_tournoi.search(self.user.
                                                                  nom_du_tournoi == nom_tournoi + "," + lieu_tournoi)
        liste_joueurs = []
        for row in joueur_par_tournoi:
            deserialise = [
                row["nom_du_tournoi"],
                row["nom"],
                row["prenom"],
                row["naissance"],
                row["sexe"],
                row["classement"],
                row["score"]
            ]
            liste_joueurs.append(deserialise)
        return liste_joueurs

    def recuperer_table_tournoi(self):
        return self.table_tournoi.all()

    def recuperer_nom_tournois(self):
        table_tournoi = self.table_tournoi.all()
        liste_noms = []
        for row in table_tournoi:
            nom = row["Nom du tournoi"], row["Lieu"]
            liste_noms.append(nom)
        return liste_noms

    def recuperer_rounds_tournoi(self, nom_tournoi, lieu_tournoi):
        table_rounds = self.table_rounds_par_tournoi.search(self.user.
                                                            nom_du_tournoi == nom_tournoi + "," + lieu_tournoi)
        liste_rounds = []
        for round in table_rounds:
            deserialise = [
                round["nom_du_tournoi"],
                round["nom_round"],
                round["matchs_du_round"],
                round["date_debut_round"],
                round["heure_debut_round"],
                round["date_fin_round"],
                round["heure_fin_round"]
            ]
            liste_rounds.append(deserialise)
        return liste_rounds

    def recuperer_matchs_tournoi(self, nom_tournoi, lieu_tournoi):
        table_rounds = self.table_rounds_par_tournoi.search(self.user.
                                                            nom_du_tournoi == nom_tournoi + "," + lieu_tournoi)
        liste_rounds = []
        for round in table_rounds:
            deserialise = [
                round["nom_du_tournoi"],
                round["matchs_du_round"],
            ]
            liste_rounds.append(deserialise)
        return liste_rounds

    def classer_par_ordre_alphabetique(self, liste_joueurs, item: int = 0):
        liste_par_alphabet = sorted(liste_joueurs, key=itemgetter(item), reverse=False)
        return liste_par_alphabet

    def classer_par_classement(self, liste_joueurs, item: int = 4):
        liste_par_classement = sorted(liste_joueurs, key=itemgetter(item), reverse=True)
        return liste_par_classement
