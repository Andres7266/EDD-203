"""De la siguiente lista de números: 10, 20, 45,45, 7, 90, 88, 45,910. Mostrar cuántas veces se repite el 45 y cuantas veces se repite el 90. Usar for"""
lista = [10, 20, 45, 45, 7, 90, 88, 45, 910]
repetidos = [num for num in set(lista)
              if lista.count(num) > 1]
print("Repetidos:", repetidos)
