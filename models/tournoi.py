import database
import datetime
from controllers.controller_round import ControllerRound


class Tournoi:

    def __init__(self, nom, lieu, description, nb_tour, controle_du_temps, nombre_joueur: int = 8):
        self.nom = nom
        self.lieu = lieu
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.nb_tour = nb_tour
        self.controle_du_temps = controle_du_temps
        self.description = description
        self.joueur = []
        self.rounds = []
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI
        self.user = database.USER

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
        tournoi = Tournoi(nom, lieu, description, nb_tour, controle_temps)
        return tournoi

    def enregistrer_tournoi(self):
        data = self.serialiser_tournoi()
        self.table_tournoi.insert(data)

    def sauvegarder_tournoi(self):
        liste_joueurs_serialise = []
        liste_rounds_serialise = []
        for joueur in self.joueur:
            joueur_serialise = joueur.serialiser_joueur()
            liste_joueurs_serialise.append(joueur_serialise)
        for round in self.rounds:
            round_serialise = round[1].serialiser_round()
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

    def recuperer_infos_tournoi(self, nom_tournoi, lieu_tournoi):
        table_tournoi = database.TABLE_TOURNOI.search(database.USER.nom_du_tournoi == nom_tournoi and database.USER.
                                                      lieu == lieu_tournoi)
        for row in table_tournoi:
            tournoi = self.deserialiser_tournoi(row)
        return tournoi

    def creer_premier_round(self):      # Lever cette forte dependance
        round = ControllerRound.creer_premier_round(ControllerRound, self.joueur)
        self.rounds.append(round)
        return round

    def creer_rounds_suivant(self):    # Lever cette forte dependance
        round = ControllerRound.creer_les_rounds_suivant(ControllerRound, self.joueur)
        self.rounds.append(round)
        return round

    def cloturer_tournoi(self):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == self.nom and self.user.lieu == self.lieu)
        for row in table_tournoi:
            row["etat_tournoi"]
            self.table_tournoi.update({"etat_tournoi": "Fini"}, self.user.nom_du_tournoi == self.nom and self.user.
                                      lieu == self.lieu)


def main():
    pass


if __name__ == "__main__":
    main()
