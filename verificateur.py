

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
