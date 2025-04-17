def Mayor():
    lista = [1, 6, 4, 4, 5]
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    print("El mayor es:", mayor)
Mayor()