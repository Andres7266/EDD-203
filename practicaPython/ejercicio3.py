
print("\n 1.-Suma\n 2.-Resta\n 3.-Multiplicación\n 4.-División\n 5.-Potencia")    
option=int(input("Elige una opción: "))
if(option==1):
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: ")) 
    print("La suma es: ",numero1+numero2)

elif(option==2):
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: ")) 
    print("La resta es: ",numero1-numero2)
elif(option==3):
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))   
    print("La multiplicación es: ",numero1*numero2)
elif(option==4):
    numero1=float(input("Introduce el primer número: "))
    numero2=float(input("Introduce el segundo número: ")) 
    if numero2==0:
        print("No se puede dividir entre 0")
    else:
        numero1=float(input("Introduce el primer número: "))
        numero2=float(input("Introduce el segundo número: ")) 
        print("La división es: ",numero1/numero2)
elif(option==5):
    numero1=int(input("Introduce la Base "))
    numero2=int(input("Introduce la Potencia ")) 
    print("La potencia es: ",numero1**numero2)
else:
    print("Opción no válida")    