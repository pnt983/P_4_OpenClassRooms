from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_round import ControllerRound
from .controller_joueurs import ControllerJoueur
from tinydb import TinyDB, Query


DB = TinyDB("db.json")
USER = Query()
TABLE_JOUEUR = DB.table("Joueur")
TABLE_TOURNOI = DB.table("Tournoi")


class ControleurTournoi:

    def __init__(self, db_table_tournoi, requete_db):
        self.tournoi = None
        self.table_tournoi = db_table_tournoi
        self.user = requete_db
        self.controller_round = ControllerRound()
        self.controller_joueur = ControllerJoueur(TABLE_JOUEUR, USER)

    def creer_tournoi(self):
        self.tournoi = Tournoi(nom=VueTournoi.creer_nom_tournoi(),
                               lieu=VueTournoi.creer_lieu_tournoi(),
                               description=VueTournoi.creer_description_tournoi(),
                               nb_tour=VueTournoi.choisir_nombre_tours_tournoi(),
                               controle_du_temps=VueTournoi.choisir_controle_temps(),
                               db_table_tournoi=self.table_tournoi,
                               query=self.user,
                               nombre_joueur=VueTournoi.choisir_nombre_joueurs())
        self.tournoi.enregistrer_tournoi()
        return self.tournoi

    def afficher_tournoi_en_cours(self):
        tous_les_tournois = self.table_tournoi.all()
        liste_tournois_encours = []
        for tournoi in tous_les_tournois:
            if tournoi["etat_tournoi"] == "en_cours":
                infos_tournoi = [tournoi["nom_du_tournoi"], tournoi["lieu"], tournoi["date"],
                                 tournoi["nombre_de_tour"], tournoi["controle_du_temps"], tournoi["description"],
                                 tournoi["etat_tournoi"]]
                liste_tournois_encours.append([infos_tournoi])
            else:
                pass
        VueTournoi.afficher_message(liste_tournois_encours)
        return liste_tournois_encours

    def reprendre_tournoi(self):
        liste_tournois_encours = self.afficher_tournoi_en_cours()
        if len(liste_tournois_encours) == 0:
            return 0
        else:
            nom_tournoi = VueTournoi.rechercher_nom_tournoi()
            lieu_tournoi = VueTournoi.rechercher_lieu_tournoi()
            recup_infos = Tournoi.recuperer_infos_tournoi(self.table_tournoi, self.user, nom_tournoi, lieu_tournoi)
            return recup_infos

    def commencer_tournoi(self):
        """ Début du tournoi dans le menu principal"""
        tournoi = self.creer_tournoi()
        liste_joueurs = self.controller_joueur.ajouter_joueur(tournoi.nombre_joueur)
        tournoi.enregistrer_joueur(liste_joueurs)
        tournoi.sauvegarder_tournoi()
        input("Appuyer sur 'Entrer' pour commencer le round")
        round_1 = self.controller_round.creer_premier_round(tournoi.joueurs)
        tournoi.enregistrer_round(round_1)
        tournoi.sauvegarder_tournoi()
        VueTournoi.valider_fin_round()
        round_1.ajouter_date_fin_round()
        tournoi.sauvegarder_tournoi()
        self.controller_round.entrer_resultat_matchs(round_1.matchs)
        round_1.cloturer_round()
        tournoi.sauvegarder_tournoi()
        for i in range(int(tournoi.nb_tour) - 1):
            round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
            tournoi.enregistrer_round(round_suivant)
            tournoi.sauvegarder_tournoi()
            VueTournoi.valider_fin_round()
            round_suivant.ajouter_date_fin_round()
            tournoi.sauvegarder_tournoi()
            self.controller_round.entrer_resultat_matchs(round_suivant.matchs)
            round_suivant.cloturer_round()
            i += 1
        tournoi.sauvegarder_tournoi()
        tournoi.cloturer_tournoi()

    def reprise_tournoi(self):
        """Reprend un tournoi enregistré dans le menu principal"""
        tournoi = self.reprendre_tournoi()
        if tournoi == 0:
            message = print("Aucun tournoi en cours")
            return message
        else:
            tournoi.table_tournoi = self.table_tournoi
            tournoi.user = self.user
            liste_rounds = []
            for round in tournoi.rounds:
                liste_rounds.append(round)
            if liste_rounds[-1].etat_round == "En_cours":
                round = liste_rounds[-1]
                print(f"Vous reprenez le tournoi {tournoi.nom}-{tournoi.lieu} au tour n°{len(liste_rounds)}")
                tournoi.joueurs = [tournoi.joueurs]
                round.ajouter_date_fin_round()
                self.controller_round.entrer_resultat_matchs(round.matchs)
                for match in round.matchs:
                    match.ajouter_joueur_deja_rencontre()
                round.cloturer_round()
                tournoi.sauvegarder_apres_reprise()
                for i in range(int(tournoi.nb_tour) - len(liste_rounds)):
                    round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
                    tournoi.enregistrer_round(round_suivant)
                    VueTournoi.valider_fin_round()
                    round_suivant.ajouter_date_fin_round()
                    self.controller_round.entrer_resultat_matchs(round_suivant.matchs)
                    round_suivant.cloturer_round()
                    i += 1
                tournoi.sauvegarder_apres_reprise()
                tournoi.cloturer_tournoi()
            else:
                round = liste_rounds[-1]
                print(f"Vous reprenez le tournoi {tournoi.nom}-{tournoi.lieu}. Le tour précédent etait \
    le tour n°{len(liste_rounds)}")
                tournoi.joueurs = [tournoi.joueurs]
                for i in range(int(tournoi.nb_tour) - len(liste_rounds)):
                    round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
                    tournoi.enregistrer_round(round_suivant)
                    VueTournoi.valider_fin_round()
                    round_suivant.ajouter_date_fin_round()
                    self.controller_round.entrer_resultat_matchs(round_suivant.matchs)
                    round_suivant.cloturer_round()
                    i += 1
                tournoi.sauvegarder_apres_reprise()
                tournoi.cloturer_tournoi()


def main():
    pass


if __name__ == "__main__":
    main()
