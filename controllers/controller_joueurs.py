from vues.vue_joueurs import VueJoueur
from models.joueur import Joueur
import utilitaires.menu as menu


class ControllerJoueur:

    def __init__(self, db_table_joueur, requete):
        self.table = db_table_joueur
        self.user = requete

    def creer_joueur(self):
        """ Cree un joueur et l'ajoute a la db 'table_joueur' """
        joueur = Joueur(VueJoueur.creer_nom_joueur(),
                        VueJoueur.creer_prenom_joueur(),
                        VueJoueur.creer_date_naissance_joueur(),
                        VueJoueur.creer_sexe_joueur(),
                        VueJoueur.creer_classement_joueur(),
                        self.table, self.user)
        id_joueur = joueur.sauvegarder_joueur_dans_db()
        joueur.id = id_joueur
        return joueur

    def ajouter_joueur(self, nombre_joueurs):
        """ Cree un nouveau joueur ou recupere dans la base de donnees. Retourne la listes des joueurs ajoutés"""
        liste_joueurs = []
        while True:
            for i in range(nombre_joueurs):
                choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
                try:
                    choix_utilisateur = VueJoueur.choisir_ajouter_joueur()
                    if choix_utilisateur in choix:
                        if choix_utilisateur == 1:
                            joueur = self.creer_joueur()
                            liste_joueurs.append(joueur)
                            i += 1
                        elif choix_utilisateur == 2:
                            choix = VueJoueur.choisir_par_id(self.table)
                            joueur_recuperer = self.recuperer_joueur_db(choix)
                            joueur = Joueur.deserialiser_joueur(joueur_recuperer)
                            joueur.id = choix
                            liste_joueurs.append(joueur)
                            i += 1
                        else:
                            VueJoueur.afficher_message_erreur()
                    else:
                        VueJoueur.afficher_message_erreur()
                except ValueError:
                    VueJoueur.afficher_message_erreur()
            return liste_joueurs

    def recuperer_joueur_db(self, choix):
        """ Recupere le joueur dans la base de donnees par son 'id' """
        id = self.table.get(doc_id=choix)
        if id != []:
            VueJoueur.afficher_message(id)
            return id
        else:
            VueJoueur.afficher_message_erreur()

    def modifier_classement_joueur(self) -> str:
        """ L'utilisateur peut modifier le classement d'un joueur par son ID"""
        while True:
            try:
                joueur_a_modifier = VueJoueur.modifier_classement(self.table)
                joueur_trouve = self.table.get(doc_id=joueur_a_modifier)
                if joueur_trouve is not None:
                    nouveau_classement = VueJoueur.entrer_nouveau_classement()
                    self.table.update({"classement": nouveau_classement}, doc_ids=[joueur_a_modifier])
                    return joueur_trouve
                else:
                    VueJoueur.afficher_message_erreur()
            except ValueError:
                VueJoueur.afficher_message_erreur()

    def gerer_joueurs(self):
        """ Gére la gestion des joueurs dans le menu principal"""
        while True:
            menu_joueur = menu.Menu("Menu joueur", menu.option_joueur)
            choix_joueur = menu_joueur.afficher()
            if choix_joueur == "1":
                self.creer_joueur()
            elif choix_joueur == "2":
                self.modifier_classement_joueur()
            elif choix_joueur == "3":
                print("Retour en arriere")
                break
            else:
                print("Choix invalide !")


def main():
    pass


if __name__ == "__main__":
    main()
