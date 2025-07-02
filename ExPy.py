import math

print("bonjour")

# Challenge 1 : Présentation personnalisée
nom = input("Quel est votre prénom ? ")
age = int(input("Quel est votre âge ? "))

print(f"\nBonjour {nom}, vous avez {age} ans!")

# Challenge  2 : Calcul de salaire avec heures supplémentaires
nom = input("Entrez votre nom : ")
salaire_horaire = float(input("Entrez votre salaire horaire (dh) : "))
heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))

if heures_travaillees > 40:
    heures_supp = heures_travaillees - 40
    salaire_total = (40 * salaire_horaire) + (heures_supp * salaire_horaire * 1.5)
    
else:
    salaire_total = heures_travaillees * salaire_horaire
    

print("\nRésultat :----------------")
print(f"Nom : {nom}")
print(f"Salaire total : {salaire_total:.2f} dh")

# # Challenge 3 :  Gestion des erreurs utilisateur

print("Calcul de salaire avec heures supplémentaires\n")

try:
    # Saisie des données
    nom = input("Votre nom : ")
    salaire = float(input("Salaire horaire (dh) : "))
    heures = float(input("Heures travaillées : "))
    
    # Vérification des valeurs
    if salaire <=0 or heures <0:
        print("Erreur : valeurs doivent être positives")
    else:
        if heures >40:
            salaire_total = 40*salaire + (heures-40)*salaire*1.5
        else:
            salaire_total = heures*salaire

        print(f"\n{nom}, votre salaire total est : {salaire_total:.2f}dh")

except ValueError:
    print("Erreur : entrez des nombres valides")

# Challenge 4 : Remplacement de Mots dans des Textes

n1 = float(input("Entrez le premier nombre (n1) : "))
n2 = float(input("Entrez le deuxième nombre (n2) : "))

produit = n1 * n2

if produit > 0:
    print(f"\nLe produit {produit} est positif")
elif produit < 0:
    print(f"\nLe produit {produit} est négatif")
else:
    print("\nLe produit est nul")

# Challenge 5 : Somme d’entiers

N = int(input("Entrez un entier positif N : "))
somme = 0
i = 1  # Compteur

while i <= N:
    somme += i
    i += 1

print(f"La somme des entiers de 1 à {N} est : {somme}")

# Challenge 6 : Inverser une chaîne 

chaine = input("Entrez une chaîne de caractères : ")

# Initialisation
indice = len(chaine) - 1  # Commence par le dernier caractère
chaine_inverse = ""

# Inversion avec while
while indice >= 0:
    chaine_inverse += chaine[indice]
    indice -= 1  # Décrémente pour aller vers le début

# Affichage du résultat
print(f"Chaîne inversée : {chaine_inverse}")

# Challenge 6 : Calcul de distance entre deux points

print("Calcul de la distance entre deux points (x1,y1) et (x2,y2)")

# Saisie des coordonnées avec conversion en float
x1 = float(input("Entrez x1 : "))
y1 = float(input("Entrez y1 : "))
x2 = float(input("Entrez x2 : "))
y2 = float(input("Entrez y2 : "))

delta_x = x2 - x1
delta_y = y2 - y1

# Application de la formule euclidienne
distance = math.sqrt(delta_x**2 + delta_y**2)

print(f"\nLa distance entre ({x1},{y1}) et ({x2},{y2}) est : {distance:.2f}")