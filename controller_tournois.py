import tournoi
from vue_tournoi import VueTournoi


class ControleurTour:

    def __init__(self):
        self.vue_tournoi = VueTournoi()

    def creer_tournoi(self):
        infos = self.vue_tournoi.creer_info_tournoi()
        self.tournoi = tournoi.Tournoi(infos.get("nom"), infos.get("lieu"), infos.get("description"),
                                       tournoi.Tournoi.nb_tours(tournoi.Tournoi, infos.get("nombre_tours")),
                                       tournoi.Tournoi.controle_temps(tournoi.Tournoi, infos.get("controle_temps")))


def main():
    test = ControleurTour()
    tournoi = test.creer_tournoi()
    print(type(tournoi))
    #tournoi.enregistrer_tournoi()


if __name__ == "__main__":
    main()