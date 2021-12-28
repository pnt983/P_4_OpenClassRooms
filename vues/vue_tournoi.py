
class VueTournoi:
    def __init__(self):
        pass

    def creer_info_tournoi(self) -> dict:
        nom_tournoi = input("Entree le nom de votre tournoi: ").capitalize()
        lieu_tournoi = input("Entree lieu du tournoi: ").capitalize()
        description = input("Mot du directeur: ").capitalize()
        nombre_tours = input("Entree le nombre de tours voulu. Si vous voulez 4 tours, appuyer \
directement sur entree: ")
        controle_temps = int(input("Taper 1 pour choisir Bullet, 2 pour choisir Blitz ou \
3 pour choisir Coup rapide: "))
        dictionnaire = {
            "nom": nom_tournoi,
            "lieu": lieu_tournoi,
            "description": description,
            "nombre_tours": nombre_tours,
            "controle_temps": controle_temps
        }
        return dictionnaire

    def choisir_nombre_joueur(self):
        return input("Entrer le nombre de joueurs a ajouter au tournoi: ")


def main():
    pass


if __name__ == "__main__":
    main()
