from tinydb import TinyDB, Query


DB = TinyDB("db.json")
USER = Query()
TABLE_JOUEUR = DB.table("Joueur")
TABLE_TOURNOI = DB.table("Tournoi")
TABLE_JOUEUR_PAR_TOURNOI = DB.table("Joueur_du_tournoi")
TABLE_ROUND_PAR_TOURNOI = DB.table("Rounds")
