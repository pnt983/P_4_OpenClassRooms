

class Joueur:
    """ Crée les nouveaux joueurs"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement, db_table_joueur, requete, score=0,
                 id=None, adversaire_deja_rencontrer=[]):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_naissance
        self.sexe_joueur = sexe
        self.classement_joueur = classement
        self.score = score
        self.adversaire_deja_rencontrer = adversaire_deja_rencontrer
        self.id = id
        self.table_joueur = db_table_joueur
        self.user = requete

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
            "score": self.score,
            "id": self.id,
            "adversaire_deja_rencontrer": self.adversaire_deja_rencontrer
        }
        return serialise

    @classmethod
    def deserialiser_joueur(cls, info_joueur):
        nom = info_joueur["nom"]
        prenom = info_joueur["prenom"]
        date_naissance = info_joueur["naissance"]
        sexe = info_joueur["sexe"]
        classement = info_joueur["classement"]
        score = info_joueur["score"]
        id = info_joueur["id"]
        adversaire_deja_rencontrer = info_joueur["adversaire_deja_rencontrer"]
        joueur = Joueur(nom=nom, prenom=prenom, date_naissance=date_naissance, sexe=sexe, classement=classement,
                        db_table_joueur=None, requete=None, score=score, id=id,
                        adversaire_deja_rencontrer=adversaire_deja_rencontrer)
        return joueur

    def sauvegarder_joueur_dans_db(self):
        """Ajoute le joueur a 'table_joueur' de la db. Si il y est deja, il met a jour les infos données"""
        data = self.serialiser_joueur()
        self.id = self.table_joueur.upsert(data, self.user.nom == self.nom and self.user.prenom == self.prenom)
        return self.id


def main():
    pass


if __name__ == "__main__":
    main()
