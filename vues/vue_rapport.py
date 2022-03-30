from utilitaires.verificateur import Verification


class VueRapport:

    def __init__(self):
        pass

    @classmethod
    @Verification.verifier_alphabetique_ou_classement
    def choisir_alphabetique_ou_classement(cls):
        return int(input("Entrer 1 pour avoir le rapport par ordre alphabetique ou \
entrer 2 pour avoir le rapport par classement: "))

    @classmethod
    @Verification.verifier_nom_dans_db
    def entrer_nom_tournoi(cls):
        return input("Entrer le nom du tournoi dont vous voulez le rapport: ").capitalize()

    @classmethod
    @Verification.verifier_lieu_dans_db
    def entrer_lieu_tournoi(cls):
        return input("Entrer le lieu du tournoi dont vous voulez le rapport: ").capitalize()

    @classmethod
    def montrer_message(cls, message):
        for row in message:
            print(row)

    @classmethod
    def montrer_table_tournoi(cls, liste_tournois):
        for element in liste_tournois:
            print("\n", "Nom:", element[0], "/", "Lieu:", element[1], "/", "Date:", element[2], "/",
                  "Nombre de tours:", element[3], "/", "Controle du temps:", element[4], "/",
                  "Description:", element[5], "/", "Avancée du tournoi:", element[6])

    @classmethod
    def montrer_rapport_match(cls, liste_matchs):
        for row in liste_matchs:
            print("\n", row[0][0], row[0][1], " VS ", row[1][0], row[1][1], ": ")
            Verification.verifier_gagnant(row)

    @classmethod
    def montrer_rapport_tour(cls, liste_matchs):
        for row in liste_matchs:
            if type(row) is tuple:
                print("\n", row[0], "/", "Date et heure du debut:", row[1], "/", "Date et heure de fin:", row[2])
            if type(row) is list:
                print(row[0][0], row[0][1], " VS ", row[1][0], row[1][1])
                Verification.verifier_gagnant(row)

    @classmethod
    def montrer_tournois(cls, liste_tournois):
        for row in liste_tournois:
            for element in row:
                print("\n", "Nom:", element[0], "/", "Lieu:", element[1], "/", "Date:", element[2], "/",
                      "Nombre de tours:", element[3], "/", "Controle du temps:", element[4], "/",
                      "Description:", element[5], "/", "Avancée du tournoi:", element[6])

    @classmethod
    def montrer_joueurs_tournoi(cls, liste_joueurs):
        for element in liste_joueurs:
            print("\n", "Nom:", element[0], "/", "Prenom:", element[1], "/", "Date de naissance:", element[2], "/",
                  "Sexe:", element[3], "/", "Classement:", element[4], "/", "Score:", element[5])

    @classmethod
    def montrer_acteurs(cls, liste_joueurs):
        for element in liste_joueurs:
            print("\n", "Nom:", element[0], "/", "Prenom:", element[1], "/", "Date de naissance:", element[2], "/",
                  "Sexe:", element[3], "/", "Classement:", element[4])

    @classmethod
    def afficher_message_erreur(cls):
        print("Le choix incorrect")
