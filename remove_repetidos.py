def remove_repetidos(lista):
    lista_vazia = []
    for x in lista:
        if x not in lista_vazia:
            lista_vazia.append(x)
    return sorted(lista_vazia)
