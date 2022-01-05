

class Verification:
    """"Verification des inputs"""

    def verifier_input_remplit(fonction):
        def wrapper(*args, **kwargs):
            while True:
                resultat = fonction(*args, **kwargs)
                if len(resultat) > 0:
                    return resultat
                else:
                    print("Le champs ne peut pas etre vide.")
        return wrapper

    def verifier_sexe(fonction):
        def wrapper(*args, **kwargs):
            while True:
                resultat = fonction(*args, **kwargs)
                if len(resultat) < 2 and len(resultat) > 0:
                    if resultat == "M" or resultat == "F":
                        return resultat
                else:
                    print("Entrer seulement la lettre 'f' ou 'm'.")
        return wrapper

    def verifier_classement(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    resultat = fonction(*args, **kwargs)
                    if int(resultat) >= 0:
                        return resultat
                    else:
                        print("Le classement ne peut pas etre négatif.")
                except ValueError:
                    ValueError(print("Le champs ne peut pas etre vide."))
        return wrapper

    def verifier_date_naissance(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    resultat = fonction(*args, **kwargs)
                    if len(resultat) == 10:
                        if int(resultat[0:2]) > 0 and int(resultat[0:2]) <= 31:
                            if int(resultat[3:5]) > 0 and int(resultat[3:5]) <= 12:
                                if int(resultat[6:10]) > 1900 and int(resultat[6:10]) < 2022:  # Essayer avec datetime pour l'annee max
                                    return resultat
                    else:
                        print("Veuillez respecter le format jj/mm/aaaa.")
                except ValueError:
                    ValueError(print("Le champs ne peut pas etre vide"))
        return wrapper

    def verifier_nombre_tours(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if len(choix_utilisateur) == 0:
                        return 4
                    else:
                        int(choix_utilisateur)
                        return choix_utilisateur
                except ValueError:
                    print("Entrer seulement un chiffre ou un nombre.")
        return wrapper

    def verifier_controle_temps(fonction):
        def wrapper(*args, **kwargs):
            while True:
                choix = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if choix_utilisateur in choix:
                        return choix[choix_utilisateur]
                    else:
                        print("Choix incorrect.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_qui_gagne(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if choix_utilisateur == 1:
                        return choix_utilisateur
                    elif choix_utilisateur == 2:
                        return choix_utilisateur
                    elif choix_utilisateur == 3:
                        return choix_utilisateur
                    else:
                        print("Choix incorrect.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper
