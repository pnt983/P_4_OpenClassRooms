import database


class Joueur:
    """Enregistrer les nouveaux joueurs ou charger ceux enregistrés dans la base de donnees"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement, score=0):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_naissance
        self.sexe_joueur = sexe
        self.classement_joueur = classement
        self.score = score
        self.table_joueur = database.TABLE_JOUEUR
        self.table_tournoi = database.TABLE_TOURNOI
        self.user = database.USER
        self.table_joueur_par_tournoi = database.TABLE_JOUEUR_PAR_TOURNOI

    def __repr__(self):
        return repr((self.nom, self.prenom, self.date_de_naissance, self.sexe_joueur, self.
                     classement_joueur, self.score))

    def serialiser_joueur(self):
        serialise = {
            "nom": self.nom,
            "prenom": self.prenom,
            "naissance": self.date_de_naissance,
            "sexe": self.sexe_joueur,
            "classement": self.classement_joueur,
            "score": self.score
        }
        return serialise

    @classmethod
    def deserialise_joueur(cls, info_joueur):
        nom = info_joueur["nom"]
        prenom = info_joueur["prenom"]
        date_naissance = info_joueur["naissance"]
        sexe = info_joueur["sexe"]
        classement = info_joueur["classement"]
        score = info_joueur["score"]
        joueur = Joueur(nom=nom, prenom=prenom, date_naissance=date_naissance, sexe=sexe, classement=classement,
                        score=score)
        return joueur

    def sauvegarder_joueur_dans_db(self):
        """Ajoute le joueur a 'table_joueur' de la db. Si il y est deja, il met a jour les infos données"""
        data = self.serialiser_joueur()
        self.table_joueur.upsert(data, self.user.nom == self.nom and self.user.prenom == self.prenom)


def main():
    pass


if __name__ == "__main__":
    main()
