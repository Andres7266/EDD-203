lista = [10, 20, 45, 45, 7, 90, 88, 45, 910]
repetidos = [num for num in set(lista)
              if lista.count(num) > 1]
print("Repetidos:", repetidos)