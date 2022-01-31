from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_joueurs import ControllerJoueur
import database


class ControleurTournoi:

    def __init__(self):
        self.tournoi = None
        self.joueur_du_tournoi = []
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI

    def creer_tournoi(self):
        self.tournoi = Tournoi(VueTournoi.creer_nom_tournoi(VueTournoi),
                               VueTournoi.creer_lieu_tournoi(VueTournoi),
                               VueTournoi.creer_description_tournoi(VueTournoi),
                               VueTournoi.nombre_tours_tournoi(VueTournoi),
                               VueTournoi.controle_temps(VueTournoi))
        self.tournoi.enregistrer_tournoi()
        return self.tournoi

    def ajouter_joueur_au_tournoi(self, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueurs(VueTournoi)
        liste_joueurs = []
        if not choix_nombre_joueurs:
            i = 0
            for i in range(nombre_joueur):
                nouveau_joueur = ControllerJoueur.ajouter_joueur(ControllerJoueur)
                self.joueur_du_tournoi.append(nouveau_joueur)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        else:
            i = 0
            for i in range(int(choix_nombre_joueurs)):
                nouveau_joueur = ControllerJoueur.ajouter_joueur(ControllerJoueur)
                self.joueur_du_tournoi.append(nouveau_joueur)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        return liste_joueurs

    def chercher_tournoi_en_cours(self):
        tous_les_tournois = self.table_tournoi.all()
        for tournoi in tous_les_tournois:
            if tournoi["etat_tournoi"] == "en_cours":
                print(tournoi)
            else:
                pass


def main():
    pass


if __name__ == "__main__":
    main()
