def Ordenar():
    lista = []
    for i in range(5):
        num = int(input("Ingrese un número: "))
        lista.append(num)
    lista.sort()
    print("Lista ordenada:", lista)
Ordenar()