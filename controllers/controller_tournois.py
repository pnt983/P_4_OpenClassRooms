from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_joueurs import ControllerJoueur
from . import controller_app


class ControleurTournoi:

    def __init__(self):
        self.table_tournoi = controller_app.ControllerApp().table_tournoi
        self.table_joueur_par_tournoi = controller_app.ControllerApp().table_joueur_par_tournoi
        self.table_joueur = controller_app.ControllerApp().table_joueur
        self.query = controller_app.ControllerApp().user

    def creer_tournoi(self):
        self.tournoi = Tournoi(VueTournoi.creer_nom_tournoi(VueTournoi),
                               VueTournoi.creer_lieu_tournoi(VueTournoi),
                               VueTournoi.creer_description_tournoi(VueTournoi),
                               VueTournoi.nombre_tours_tournoi(VueTournoi),
                               VueTournoi.controle_temps(VueTournoi))
        Tournoi.enregistrer_tournoi(Tournoi, self.tournoi)
        return self.tournoi

    def ajouter_joueur_au_tournoi(self, nom, lieu, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueurs(VueTournoi)
        liste_joueurs = []
        if not choix_nombre_joueurs:
            i = 0
            for i in range(nombre_joueur):
                nouveau_joueur = self.ajouter_joueur(nom, lieu)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        else:
            i = 0
            for i in range(int(choix_nombre_joueurs)):
                nouveau_joueur = self.ajouter_joueur(nom, lieu)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        return liste_joueurs

    def ajouter_joueur(self, nom_tournoi, lieu_tournoi):
        """ Enregistre un nouveau joueur ou recupere dans la base de donnees pour l'ajouter au tournoi"""
        while True:
            choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
            try:
                choix_utilisateur = VueTournoi.choix_ajouter_joueur(VueTournoi)
                if choix_utilisateur in choix:
                    if choix_utilisateur == 1:
                        creer_joueur = ControllerJoueur.creer_joueur(ControllerJoueur)
                        Tournoi.ajouter_joueur_du_tournoi_a_db(Tournoi, nom_tournoi, lieu_tournoi, creer_joueur)
                        return creer_joueur
                    elif choix_utilisateur == 2:
                        choix = VueTournoi.choix_par_id(VueTournoi)
                        joueur_recuperer = self.recuperer_joueur_db(choix)
                        Tournoi.ajouter_joueur_du_tournoi_a_db(Tournoi, nom_tournoi, lieu_tournoi, joueur_recuperer)
                        return joueur_recuperer
                    else:
                        VueTournoi.message_erreur(VueTournoi)
                else:
                    VueTournoi.message_erreur(VueTournoi)
            except ValueError:
                VueTournoi.message_erreur(VueTournoi)

    def recuperer_joueur_db(self, choix):
        """ Recupere le joueur dans la base de donnees par son 'id' """
        chercher_id = self.table_joueur.get(doc_id=choix)
        if chercher_id != []:
            print(chercher_id)
            return chercher_id
        else:
            VueTournoi.message_erreur(VueTournoi)


def main():
    test = ControleurTournoi()
    result = test.creer_tournoi()
    print(type(result))


if __name__ == "__main__":
    main()
