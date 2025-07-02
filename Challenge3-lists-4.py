def recherche_element_tous(element, liste):
    
    indices = []
    for i in range(len(liste)):
        if liste[i] == element:
            indices.append(i)
    return indices