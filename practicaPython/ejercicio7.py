"""Generar la tabla de multiplicación utilizando el for:"""
numero = int(input("Introduce el primer número: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")
