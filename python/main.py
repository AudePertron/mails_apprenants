from apprenant import Apprenant
from bdd import MySQL_link
from read import Read
import tkinter as tk
from tkinter import filedialog


def main():
    link = MySQL_link()
    
    root = tk.Tk()
    root.withdraw()
    
    emplacement = filedialog.askopenfilename()
    fichier = Read(emplacement).read()

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
    link.close()

main()
