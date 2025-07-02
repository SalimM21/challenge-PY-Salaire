def compter_occurrences(a, L):
    compteur = 0
    for element in L:
        if element == a:
            compteur = compteur + 1
    return compteur