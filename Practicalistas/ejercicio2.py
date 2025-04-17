def suma():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))
    if numero1% 2 == 0:
        if numero2 % 2 == 0:
            print("Ambos números son pares")
            suma= numero1 + numero2
            print("La suma de los números es:", suma)
        else:
            print("Ambos números son impares") 
            print("FIN")
suma()
       
    