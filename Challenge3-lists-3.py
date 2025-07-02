# Liste initiale
stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]

# 1. Afficher la liste initiale
print("1. Liste initiale :")
print(f"   stock = {stock}")

# 2. Créer deux nouvelles listes
print("2. Séparation en deux listes :")


chaines = [] # Liste des chaînes de caractères
nombres = [] # Liste des valeurs numériques

# Parcourir la liste et séparer selon le type
for element in stock:
    if isinstance(element, str):
        chaines.append(element)
    elif isinstance(element, (int, float)):
        nombres.append(element)

print(f"   Liste des chaînes : {chaines}")
print(f"   Liste des nombres : {nombres}")
print()

# 3. Trier les listes
print("3. Tri des listes :")

# Trier les chaînes en ordre croissant (alphabétique)
chaines_triees = sorted(chaines)
print(f"   Chaînes triées (ordre croissant) : {chaines_triees}")

# Trier les nombres en ordre décroissant
nombres_tries = sorted(nombres, reverse=True)
print(f"   Nombres triés (ordre décroissant) : {nombres_tries}")
print()

# 4. Affichage final des deux listes triées
print("4. Résultats finaux :")
print(f"   Liste des chaînes triées : {chaines_triees}")
print(f"   Liste des nombres triés : {nombres_tries}")