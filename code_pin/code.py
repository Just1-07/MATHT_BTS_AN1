import tkinter as tk
from tkinter import messagebox

# Code PIN correct
Chaine2 = "6931"

def saisie():
    """ Récupère le code saisi et lance la vérification """
    Chaine1 = entry_pin.get()
    verifier4caractere(Chaine1)

def comparer2chaine(chaine1, chaine2):
    """ Compare le PIN saisi avec le PIN correct """
    if chaine1 == chaine2:
        messagebox.showinfo("Succès", "CORRECT")
    else:
        messagebox.showerror("Erreur", "INCORRECT")
        entry_pin.delete(0, tk.END)  # Efface la saisie pour réessayer

def verifier4caractere(Chaine1):
    """ Vérifie si le PIN contient exactement 4 caractères """
    if len(Chaine1) == 4:
        caractèrenumerique(Chaine1)
    else:
        messagebox.showerror("Erreur", "4 caractères SVP")
        entry_pin.delete(0, tk.END)

def caractèrenumerique(Chaine1):
    """ Vérifie si le PIN contient uniquement des chiffres """
    if Chaine1.isnumeric():
        comparer2chaine(Chaine1, Chaine2)
    else:
        messagebox.showerror("Erreur", "Des chiffres SVP")
        entry_pin.delete(0, tk.END)

# Création de l'interface
root = tk.Tk()
root.title("Saisie du PIN")

# Label
label = tk.Label(root, text="Entrez un code PIN à 4 chiffres :")
label.pack(pady=5)

# Champ de saisie
entry_pin = tk.Entry(root, show="*", justify="center")
entry_pin.pack(pady=5)

# Bouton de validation
btn_valider = tk.Button(root, text="Valider", command=saisie)
btn_valider.pack(pady=5)

# Lancement de l'application
root.mainloop()