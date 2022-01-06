from controllers import controller_joueurs


class Joueur:
    """Enregistrer les nouveaux joueurs ou charger ceux enregistrés dans la base de donnees"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_naissance
        self.sexe_joueur = sexe
        self.classement_joueur = classement

    def serialise_joueur(self, joueur):
        joueur_info = joueur
        serialise = {
            "nom": joueur_info.nom,
            "prenom": joueur_info.prenom,
            "naissance": joueur_info.date_de_naissance,
            "sexe": joueur_info.sexe_joueur,
            "classement": joueur_info.classement_joueur
        }
        return serialise

    def enregistrer_joueur_dans_db(self, serialise, nom_joueur, prenom_joueur):
        """Ajoute le joueur a 'table_joueur' de la db. Si il y est deja, il met a jour les infos données"""
        controller_joueurs.ControllerJoueur().db.upsert(serialise,
                                                        controller_joueurs.ControllerJoueur().
                                                        query.nom == nom_joueur and controller_joueurs.
                                                        ControllerJoueur().query.prenom == prenom_joueur)


def main():
    pass


if __name__ == "__main__":
    main()
