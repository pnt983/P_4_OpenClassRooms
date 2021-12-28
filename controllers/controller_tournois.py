from models import tournoi
from vues.vue_tournoi import VueTournoi
from . import controller_joueurs
from models import tournoi


class ControleurTournoi:

    def __init__(self):
        self.vue_tournoi = VueTournoi()

    def creer_tournoi(self):
        infos = self.vue_tournoi.creer_info_tournoi()
        self.tournoi = tournoi.Tournoi(infos.get("nom"), infos.get("lieu"), infos.get("description"),
                                       tournoi.Tournoi.nb_tours(tournoi.Tournoi, infos.get("nombre_tours")),
                                       tournoi.Tournoi.controle_temps(tournoi.Tournoi, infos.get("controle_temps")))
        return self.tournoi

    def ajouter_joueur_au_tournoi(self, nom, lieu, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueur(VueTournoi)
        if not choix_nombre_joueurs:
            i = 0
            for i in range(nombre_joueur):
                controller_joueurs.ControllerJoueur.ajouter_joueur_au_tournoi(controller_joueurs.ControllerJoueur, nom, lieu)
                i += 1
        else:
            i = 0
            for i in range(choix_nombre_joueurs):
                controller_joueurs.ControllerJoueur.ajouter_joueur_au_tournoi(controller_joueurs.ControllerJoueur, nom, lieu)
                i += 1

def main():
    pass


if __name__ == "__main__":
    main()