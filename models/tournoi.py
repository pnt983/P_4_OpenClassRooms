import datetime

from .round import Round
from models.joueur import Joueur


class Tournoi():
    """Crée un tournoi"""

    def __init__(self, nom, lieu, description, nb_tour, controle_du_temps, joueurs=[], rounds=[],
                 db_table_tournoi=None, query=None, nombre_joueur: int = 8):
        self.nom = nom
        self.lieu = lieu
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.nb_tour = nb_tour
        self.controle_du_temps = controle_du_temps
        self.description = description
        self.nombre_joueur = nombre_joueur
        self.joueurs = joueurs
        self.rounds = rounds
        self.id = None
        self.table_tournoi = db_table_tournoi
        self.user = query

    def serialiser_tournoi(self):
        serialise = {
            "nom_du_tournoi": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nombre_de_tour": self.nb_tour,
            "controle_du_temps": self.controle_du_temps,
            "description": self.description,
            "etat_tournoi": "en_cours"
        }
        return serialise

    @classmethod
    def deserialiser_tournoi(cls, info_tournoi):
        nom = info_tournoi["nom_du_tournoi"]
        lieu = info_tournoi["lieu"]
        nb_tour = info_tournoi["nombre_de_tour"]
        controle_temps = info_tournoi["controle_du_temps"]
        description = info_tournoi["description"]
        liste_joueurs = [Joueur.deserialiser_joueur(joueur) for joueur in info_tournoi["joueurs"]]
        liste_rounds = [Round.deserialiser_round(round, liste_joueurs) for round in info_tournoi["rounds"]]
        tournoi = Tournoi(nom, lieu, description, nb_tour, controle_temps, liste_joueurs, liste_rounds)
        return tournoi

    def enregistrer_tournoi(self):
        data = self.serialiser_tournoi()
        self.id = self.table_tournoi.insert(data)

    def enregistrer_joueur(self, liste_joueurs):
        """Enregistre la liste des joueurs dans le tournoi"""
        joueurs = self.joueurs.append(liste_joueurs)
        return joueurs

    def enregistrer_round(self, round):
        """Enregistre les rouds dans le tournoi"""
        round = self.rounds.append(round)
        return round

    def sauvegarder_tournoi(self):
        liste_joueurs_serialise = []
        liste_rounds_serialise = []
        for row in self.joueurs:
            for joueur in row:
                joueur_serialise = joueur.serialiser_joueur()
                liste_joueurs_serialise.append(joueur_serialise)
        for round in self.rounds:
            round_serialise = round.serialiser_round()
            liste_rounds_serialise.append(round_serialise)
        serialise = {
            "nom_du_tournoi": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nombre_de_tour": self.nb_tour,
            "controle_du_temps": self.controle_du_temps,
            "description": self.description,
            "etat_tournoi": "en_cours",
            "joueurs": liste_joueurs_serialise,
            "rounds": liste_rounds_serialise
        }
        self.table_tournoi.upsert(serialise, self.user.nom_du_tournoi == self.nom and self.user.lieu == self.lieu)

    @classmethod
    def recuperer_infos_tournoi(cls, table, user, nom_tournoi, lieu_tournoi):
        table_tournoi = table.search(user.nom_du_tournoi == nom_tournoi and user.lieu == lieu_tournoi)
        for row in table_tournoi:
            tournoi = cls.deserialiser_tournoi(row)
            liste_rounds = []
            for round in tournoi.rounds:
                liste_rounds.append(round)
        return tournoi

    # def creer_classement_final(self):
    #     for row in self.joueurs:
    #         liste_par_score = sorted(row, key=lambda joueur: joueur.score, reverse=True)
    #         return liste_par_score

    def cloturer_tournoi(self):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == self.nom and self.user.lieu == self.lieu)
        for row in table_tournoi:
            row["etat_tournoi"]
            self.table_tournoi.update({"etat_tournoi": "Fini"}, self.user.nom_du_tournoi == self.nom and self.user.
                                      lieu == self.lieu)
        for row in self.joueurs:
            liste_par_score = sorted(row, key=lambda joueur: joueur.score, reverse=True)
            return liste_par_score

    def sauvegarder_apres_reprise(self):
        liste_joueurs_serialise = []
        liste_rounds_serialise = []
        for row in self.joueurs:
            for joueur in row:
                for element in joueur.adversaire_deja_rencontrer:
                    if type(element) is not int:
                        joueur.adversaire_deja_rencontrer.pop(-1)
            joueur_serialise = joueur.serialiser_joueur()
            liste_joueurs_serialise.append(joueur_serialise)
        for row in self.rounds:
            round_serialise = row.serialiser_round()
            liste_rounds_serialise.append(round_serialise)
        serialise = {
            "nom_du_tournoi": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nombre_de_tour": self.nb_tour,
            "controle_du_temps": self.controle_du_temps,
            "description": self.description,
            "etat_tournoi": "en_cours",
            "joueurs": liste_joueurs_serialise,
            "rounds": liste_rounds_serialise
        }
        self.table_tournoi.update(serialise, self.user.nom_du_tournoi == self.nom and self.user.lieu == self.lieu)


def main():
    pass


if __name__ == "__main__":
    main()
