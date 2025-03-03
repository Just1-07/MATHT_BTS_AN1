# Fonction qui calcule la moyenne pondérée
def moyenne_ponderee(notes, coefficients):
    somme_notes = 0
    somme_coefficients = 0
    for i in range(len(notes)):
        somme_notes += notes[i] * coefficients[i]  # Multiplie chaque note par son coefficient
        somme_coefficients += coefficients[i]      # Ajoute les coefficients
    return somme_notes / somme_coefficients       # Calcule la moyenne pondérée

# Fonction pour saisir les notes d'une matière
def saisir_notes(matiere):
    notes = []
    print(f"Saisir les notes pour {matiere} (tapez -1 pour finir) :")
    while True:
        try:
            note = float(input())  # Demande à l'utilisateur d'entrer une note
            if note == -1:         # Si l'utilisateur tape -1, il a fini d'entrer des notes
                break
            elif 0 <= note <= 20:  # Vérifie que la note est entre 0 et 20
                notes.append(note) # Ajoute la note à la liste des notes
            else:
                print("La note doit être entre 0 et 20. Essayez encore.")  # Si la note est invalide
        except ValueError:
            print("Entrée incorrecte. Veuillez entrer un nombre.")  # Si l'utilisateur ne saisit pas un nombre
    return notes

# Liste des matières et leurs coefficients respectifs
matieres = ["Mathématiques", "SISR", "Technologie"]
coefficients = [12, 12, 6]
notes_finales = []

# On entre les notes pour chaque matière
for i in range(len(matieres)):
    notes = saisir_notes(matieres[i])  # Demander les notes pour chaque matière
    for note in notes:
        notes_finales.append((note, coefficients[i]))  # Ajouter chaque note avec son coefficient

# Calcul et affichage de la moyenne pondérée
notes, coefficients = zip(*notes_finales)  # Sépare les notes et les coefficients dans deux listes
moyenne = moyenne_ponderee(notes, coefficients)  # Calcule la moyenne pondérée
print(f"La moyenne pondérée est : {moyenne:.2f}")  # Affiche la moyenne avec 2 chiffres après la virgule
