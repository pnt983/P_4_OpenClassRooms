from models.joueur import Joueur
from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_joueurs import ControllerJoueur
import database


class ControleurTournoi:

    def __init__(self):
        self.table_tournoi = database.TABLE_TOURNOI
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI

    def creer_tournoi(self):
        tournoi = Tournoi(VueTournoi.creer_nom_tournoi(VueTournoi),
                          VueTournoi.creer_lieu_tournoi(VueTournoi),
                          VueTournoi.creer_description_tournoi(VueTournoi),
                          VueTournoi.nombre_tours_tournoi(VueTournoi),
                          VueTournoi.controle_temps(VueTournoi))
        tournoi.enregistrer_tournoi()
        return tournoi

    def ajouter_joueur_au_tournoi(self, nom_tournoi, lieu_tournoi, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueurs(VueTournoi)
        liste_joueurs = []
        if not choix_nombre_joueurs:
            i = 0
            for i in range(nombre_joueur):
                nouveau_joueur = ControllerJoueur.ajouter_joueur(ControllerJoueur)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        else:
            i = 0
            for i in range(int(choix_nombre_joueurs)):
                nouveau_joueur = ControllerJoueur.ajouter_joueur(ControllerJoueur)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        Tournoi.sauvegarder_joueur_du_tournoi_dans_db(Tournoi, nom_tournoi, lieu_tournoi, liste_joueurs)
        return liste_joueurs



def main():
    pass


if __name__ == "__main__":
    main()
