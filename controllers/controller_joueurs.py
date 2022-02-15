from vues.vue_joueurs import VueJoueur
from models.joueur import Joueur


class ControllerJoueur:

    def __init__(self, db_table_joueur, requete):
        self.joueur = None
        self.table = db_table_joueur
        self.user = requete

    def creer_joueur(self):
        """ Cree un joueur et l'ajoute a la db 'table_joueur' """
        self.joueur = Joueur(VueJoueur.creer_nom_joueur(VueJoueur),
                             VueJoueur.creer_prenom_joueur(VueJoueur),
                             VueJoueur.creer_date_naissance_joueur(VueJoueur),
                             VueJoueur.creer_sexe_joueur(VueJoueur),
                             VueJoueur.creer_classement_joueur(VueJoueur),
                             self.table,
                             self.user)
        self.joueur.sauvegarder_joueur_dans_db()
        return self.joueur

    def ajouter_joueur(self):
        """Cree un nouveau joueur ou recupere dans la base de donnees pour l'envoyer au tournoi"""
        while True:
            choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
            try:
                choix_utilisateur = VueJoueur.choix_ajouter_joueur(VueJoueur)
                if choix_utilisateur in choix:
                    if choix_utilisateur == 1:
                        joueur = self.creer_joueur(ControllerJoueur)
                        return joueur
                    elif choix_utilisateur == 2:
                        choix = VueJoueur.choix_par_id(VueJoueur)
                        objet = ControllerJoueur()
                        joueur_recuperer = objet.recuperer_joueur_db(choix)
                        joueur = Joueur.deserialise_joueur(joueur_recuperer)
                        return joueur
                    else:
                        VueJoueur.message_erreur(VueJoueur)
                else:
                    VueJoueur.message_erreur(VueJoueur)
            except ValueError:
                VueJoueur.message_erreur(VueJoueur)

    def recuperer_joueur_db(self, choix):
        """ Recupere le joueur dans la base de donnees par son 'id' """
        id = self.table.get(doc_id=choix)
        if id != []:
            VueJoueur.afficher_message(VueJoueur, id)
            return id
        else:
            VueJoueur.message_erreur(VueJoueur)

    def modifier_classement_joueur(self) -> str:
        """L'utilisateur peut modifier le classement d'un joueur par son ID"""
        while True:
            try:
                joueur_a_modifier = VueJoueur.modifier_classement(VueJoueur, self.table)
                joueur_trouve = self.table.get(doc_id=joueur_a_modifier)
                if joueur_trouve is not None:
                    nouveau_classement = VueJoueur.nouveau_classement(VueJoueur)
                    self.table.update({"classement": nouveau_classement}, doc_ids=[joueur_a_modifier])
                    return joueur_trouve
                else:
                    VueJoueur.message_erreur(VueJoueur)
            except ValueError:
                VueJoueur.message_erreur(VueJoueur)


def main():
    pass


if __name__ == "__main__":
    main()
