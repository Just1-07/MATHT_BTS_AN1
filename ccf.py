def AfficheImage(matrice):
    """Affiche l'image sous forme de caractères 'X' et '0'."""
    for ligne in matrice:  # Parcourt chaque ligne
        for pixel in ligne:  # Parcourt chaque pixel de la ligne
            print("X" if pixel == 1 else "0", end=" ")  # Affiche 'X' ou '0'
        print()  # Retour à la ligne après chaque ligne

def VerifSymetrieVert(tab):
    """Vérifie si l'image est symétrique verticalement."""
    for i in range(len(tab)):  # Parcourt les lignes (au lieu de fixer 10)
        for j in range(len(tab[i]) // 2):  # Compare la moitié gauche
            if tab[i][j] != tab[i][-j - 1]:  # Compare avec la moitié droite
                return False  # Si il y a une différence , pas symétrique
    return True  # Si tout correspond, alors  symétrique

def Negative(matrice):
    """Transforme l'image en négatif (inverse les couleurs)."""
    for i in range(len(matrice)):  # Parcourt chaque ligne
        for j in range(len(matrice[i])):  # Parcourt chaque colonne
            matrice[i][j] = 1 - matrice[i][j]  # Inverse 0 en 1 et 1 en 0

# Définition de l'image (10x10)
image = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Affichage de l'image originale
print("Image originale :")
AfficheImage(image)

# Vérification de la symétrie
if VerifSymetrieVert(image):
    print("\nL'image est symétrique verticalement.")
else:
    print("\nL'image n'est PAS symétrique verticalement.")

# Transformation en négatif
Negative(image)

# Affichage de l'image en négatif
print("\nImage en négatif :")
AfficheImage(image)
