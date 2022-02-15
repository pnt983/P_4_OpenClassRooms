from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_joueurs import ControllerJoueur


class ControleurTournoi:

    def __init__(self, db_table_tournoi, requete_db):
        self.tournoi = None
        self.table_tournoi = db_table_tournoi
        self.user = requete_db

    def creer_tournoi(self):
        self.tournoi = Tournoi(VueTournoi.creer_nom_tournoi(VueTournoi),
                               VueTournoi.creer_lieu_tournoi(VueTournoi),
                               VueTournoi.creer_description_tournoi(VueTournoi),
                               VueTournoi.nombre_tours_tournoi(VueTournoi),
                               VueTournoi.controle_temps(VueTournoi),
                               self.table_tournoi,
                               self.user)
        self.tournoi.enregistrer_tournoi()
        return self.tournoi

    def ajouter_joueur_au_tournoi(self, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueurs(VueTournoi)
        liste_joueurs = []
        if not choix_nombre_joueurs:
            i = 0
            for i in range(nombre_joueur):
                nouveau_joueur = ControllerJoueur.ajouter_joueur(ControllerJoueur)
                self.tournoi.joueur.append(nouveau_joueur)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        else:
            i = 0
            for i in range(int(choix_nombre_joueurs)):
                nouveau_joueur = ControllerJoueur.ajouter_joueur(ControllerJoueur)
                self.tournoi.joueur.append(nouveau_joueur)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        return liste_joueurs

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
        VueTournoi.afficher_message(VueTournoi, liste_tournois_encours)
        return liste_tournois_encours

    def reprendre_tournoi(self):
        self.afficher_tournoi_en_cours()
        nom_tournoi = VueTournoi.rechercher_nom_tournoi(VueTournoi)
        lieu_tournoi = VueTournoi.rechercher_lieu_tournoi(VueTournoi)
        recup_infos = Tournoi.recuperer_infos_tournoi(Tournoi, nom_tournoi, lieu_tournoi)
        print(type(recup_infos), recup_infos.rounds, recup_infos.joueur)


def main():
    pass


if __name__ == "__main__":
    main()
