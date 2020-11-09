from apprenant import Apprenant
from bdd import MySQL_link
from read import Read


def main():
    link = MySQL_link()
    fichier = Read(r"C:\Users\Work\Google Drive\Projets\Mails\apprenantmail.txt").read()

    try:
        link.creer_colonne()
    except:
        print("La colonne existe déjà")

    membres = link.get_infos()
    apprenants = []

    for membre in membres :
        apprenant = Apprenant(*membre)
        apprenants.append(apprenant)

    for apprenant in apprenants:
        for mail in fichier:
            if apprenant.prenom and apprenant.nom in mail:
                apprenant.mail = mail.replace('\n', '')
                link.insert_mail(apprenant.id, apprenant.mail)
    print("Mails insérés!")


main()
