from vues.vue_joueurs import VueJoueur
from models.joueur import Joueur
from tinydb import TinyDB, Query

db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


class ControllerJoueur:

    def __init__(self):
        pass

    def creer_joueur(self):
        """ Cree un joueur et l'ajoute a la db 'table_joueur' """
        self.joueur = Joueur(VueJoueur.creer_nom_joueur(VueJoueur),
                             VueJoueur.creer_prenom_joueur(VueJoueur),
                             VueJoueur.creer_date_naissance_joueur(VueJoueur),
                             VueJoueur.creer_sexe_joueur(VueJoueur),
                             VueJoueur.creer_classement_joueur(VueJoueur))
        serialise = self.joueur.serialise_joueur(self.joueur)
        Joueur.enregistrer_joueur_dans_db(Joueur, serialise, self.joueur.nom, self.joueur.prenom)
        return serialise

    def ajouter_joueur_au_tournoi(self, nom_tournoi, lieu_tournoi):
        """ Enregistre un nouveau joueur ou recupere dans la base de donnees pour l'ajouter au tournoi"""
        while True:
            choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
            try:
                choix_utilisateur = VueJoueur.choix_ajouter_joueur(VueJoueur)
                if choix_utilisateur in choix:
                    if choix_utilisateur == 1:
                        creer_joueur = self.creer_joueur(ControllerJoueur)
                        Joueur.ajouter_joueur_du_tournoi_a_db(Joueur, nom_tournoi, lieu_tournoi, creer_joueur)
                        return creer_joueur
                    elif choix_utilisateur == 2:
                        choix = VueJoueur.choix_par_id(VueJoueur)
                        joueur_recuperer = Joueur.recuperer_joueur_db(Joueur, choix)
                        Joueur.ajouter_joueur_du_tournoi_a_db(Joueur, nom_tournoi, lieu_tournoi, joueur_recuperer)
                        return joueur_recuperer
                    else:
                        VueJoueur.message_erreur(VueJoueur)
                else:
                    VueJoueur.message_erreur(VueJoueur)
            except ValueError:
                VueJoueur.message_erreur(VueJoueur)

    def modifier_classement_joueur(self) -> str:
        """L'utilisateur peut modifier le classement d'un joueur par son ID"""
        while True:
            try:
                joueur_a_modifier = VueJoueur.modifier_classement(VueJoueur)
                joueur_trouve = table_joueur.get(doc_id=joueur_a_modifier)
                if joueur_trouve is not None:
                    nouveau_classement = VueJoueur.nouveau_classement()
                    table_joueur.update({"classement": nouveau_classement}, doc_ids=[joueur_a_modifier])
                    return joueur_trouve
                else:
                    VueJoueur.message_erreur(VueJoueur)
            except ValueError:
                VueJoueur.message_erreur(VueJoueur)


def main():
    test = ControllerJoueur()
    resultat = test.modifier_classement_joueur()
    print(resultat)
    print(type(resultat))


if __name__ == "__main__":
    main()
