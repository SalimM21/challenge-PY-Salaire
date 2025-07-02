# Liste des notes donnée
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# Calcul de la moyenne
moyenne = sum(notes) / len(notes)

# Extraction des notes supérieures à la moyenne
notes_superieures = []
for note in notes:
    if note > moyenne:
        notes_superieures.append(note)

# Affichage des résultats
print(f"Moyenne : {moyenne:.2f}")
print(f"Notes supérieures à la moyenne : {notes_superieures}")
print(f"Nombre de notes supérieures à la moyenne : {len(notes_superieures)}")
