from controllers import controller_tournois
import time


class Tournoi:

    def __init__(self, nom, lieu, description, nb_tour, controle_du_temps, nombre_joueur: int = 8):
        self.nom = nom
        self.lieu = lieu
        self.date = time.strftime("%d-%m-%Y")
        self.nb_tour = nb_tour
        self.controle_du_temps = controle_du_temps
        self.description = description

    def enregistrer_tournoi(self, info_tournoi):
        infos = info_tournoi
        serialise = {
            "Nom du tournoi": infos.nom,
            "Lieu": infos.lieu,
            "Nombre de tour": infos.nb_tour,
            "Controle du temps": infos.controle_du_temps,
            "Description": infos.description
        }
        controller_tournois.ControleurTournoi().table_tournoi.insert(serialise)

    def ajouter_joueur_du_tournoi_a_db(self, nom_tournoi, lieu_tournoi, joueur_recuperer):
        """Ajoute le joueur a la table 'table_joueur_par_tournoi' de la db"""
        info_joueur = joueur_recuperer
        serialise_joueur = {
            "nom_du_tournoi": nom_tournoi + "," + lieu_tournoi,
            "nom": info_joueur["nom"],
            "prenom": info_joueur["prenom"],
            "naissance": info_joueur["naissance"],
            "sexe": info_joueur["sexe"],
            "classement": info_joueur["classement"],
            "score": 0
        }
        controller_tournois.ControleurTournoi().table_joueur_par_tournoi.insert(serialise_joueur)
        return serialise_joueur


def main():
    pass


if __name__ == "__main__":
    main()
