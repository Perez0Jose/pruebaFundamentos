vol1 = float(input("Ingrese el primer voltaje: "))
vol2 = float(input("Ingrese el segundo voltaje: "))
vol3 = float(input("Ingrese el tercer voltaje: "))

promedio = (vol1+vol2+vol3) / 3

if promedio < 115:
    print("Voltaje correcto")
elif promedio > 115 and promedio < 220:
    print("Alto voltaje")
else:
    promedio > 220
    print("Peligro") 