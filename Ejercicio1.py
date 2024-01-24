#Desarollar un programa que permita ingresar 5 voltajes

vol1 = float(input("Ingrese el primer voltaje: "))
vol2 = float(input("Ingrese el segundo voltaje: "))
vol3 = float(input("Ingrese el tercer voltaje: "))
vol4 = float(input("Ingrese el cuarto voltaje: "))
vol5 = float(input("Ingrese el quinto voltaje: "))

promedio = vol1+vol2+vol3+vol4+vol5 / 5

if promedio > 220:
    print("Alto voltaje")
else :
    promedio < 220
    print("Voltaje correcto")    
 


