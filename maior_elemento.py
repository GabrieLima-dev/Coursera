def maior_elemento(lista):
    max_value = None
    for num in lista:
        if (max_value is None or num > max_value):
            max_value = num
    return max_value
