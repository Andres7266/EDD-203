def numerosimPares():
    lista=[1,3,5,7,9,11,13,15,17,19]
    for i in range(len(lista)):
        if lista[i]%2==0:
            print(lista[i],end=" ")
    return lista
resultado=numerosimPares()
print(resultado)
