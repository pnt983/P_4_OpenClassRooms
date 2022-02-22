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


def main():
    pass


if __name__ == "__main__":
    main()
