import mysql.connector as mysql

class MySQL_link:
    #Créer une classe link qui pourra être utilisée pour tout import/export de données vers la base
    def __init__(self):
        self.link = mysql.connect(host='localhost', password='root', user='root', database='binomotron')
        self.cursor = self.link.cursor()
    
    def creer_colonne(self):
        self.cursor.execute("ALTER TABLE apprenants ADD mail_apprenant VARCHAR(50) NOT NULL")

    def get_infos(self):
        self.cursor.execute("SELECT id_apprenant, prenom_apprenant, nom_apprenant FROM apprenants")
        return self.cursor.fetchall()

    def insert_mail(self, _id, mail):
        SQL = f"UPDATE apprenants SET mail_apprenant = '{mail}' WHERE id_apprenant = {_id}"
        self.cursor.execute(SQL)
        self.link.commit()
