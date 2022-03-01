from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi


class ControleurTournoi:

    def __init__(self, db_table_tournoi, requete_db):
        self.tournoi = None
        self.table_tournoi = db_table_tournoi
        self.user = requete_db

    def creer_tournoi(self):
        self.tournoi = Tournoi(nom=VueTournoi.creer_nom_tournoi(),
                               lieu=VueTournoi.creer_lieu_tournoi(),
                               description=VueTournoi.creer_description_tournoi(),
                               nb_tour=VueTournoi.nombre_tours_tournoi(),
                               controle_du_temps=VueTournoi.controle_temps(),
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
        self.afficher_tournoi_en_cours()
        nom_tournoi = VueTournoi.rechercher_nom_tournoi()
        lieu_tournoi = VueTournoi.rechercher_lieu_tournoi()
        # revoir la ligne recup_infos car c'est bizarre de passer ces parametres
        recup_infos = Tournoi.recuperer_infos_tournoi(self.table_tournoi, self.user, nom_tournoi, lieu_tournoi)
        return recup_infos

    # def run_tournoi(self):
    #     tournoi = self.controller_tournoi.creer_tournoi()
    #     liste_joueurs = self.controller_joueur.ajouter_joueur(tournoi.nombre_joueur)
    #     tournoi.enregistrer_joueur(liste_joueurs)
    #     tournoi.sauvegarder_tournoi()
    #     input("Appuyer sur 'Entrer' pour commencer le round")
    #     round_1 = self.controller_round.creer_premier_round(tournoi.joueurs)
    #     tournoi.enregistrer_round(round_1)
    #     tournoi.sauvegarder_tournoi()
    #     input("Appuyer sur 'Entrer' pour finir le round")
    #     round_1.ajouter_date_fin_round()
    #     tournoi.sauvegarder_tournoi()
    #     self.controller_round.entrer_resultat_matchs(round_1.match)
    #     round_1.cloturer_round()
    #     tournoi.sauvegarder_tournoi()
    #     for i in range(int(tournoi.nb_tour) - 1):
    #         round_suivant = self.controller_round.creer_les_rounds_suivant(tournoi.joueurs)
    #         tournoi.enregistrer_round(round_suivant)
    #         tournoi.sauvegarder_tournoi()
    #         input("Appuyer sur 'Entrer' pour finir le round")
    #         round_suivant.ajouter_date_fin_round()
    #         tournoi.sauvegarder_tournoi()
    #         self.controller_round.entrer_resultat_matchs(round_suivant.match)
    #         round_suivant.cloturer_round()
    #         i += 1
    #     tournoi.sauvegarder_tournoi()
    #     tournoi.cloturer_tournoi()

def main():
    pass


if __name__ == "__main__":
    main()
