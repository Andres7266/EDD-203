
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
IndiceM = peso / (altura ** 2)
print(f"\nTu Índice de Masa Corporal (IMC) es: {IndiceM:.2f}")
if IndiceM < 18.5:
    print("Bajo peso")
elif 18.5 <= IndiceM < 25:
    print(" Peso normal")
elif 25 <= IndiceM < 30:
    print("Sobrepeso")
else:
    print("Obesidad")