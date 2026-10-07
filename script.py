tipo = "Coche"
peso = 1500
if tipo == "Camión" and peso > 5000:
    print("Vehículo pesado")
elif tipo == "Coche" and peso > 2000:
    print("Vehículo pesadito")
elif tipo == "Coche" and (peso <= 2000 and peso >= 1000):
    print("Vehículo mediano")
else:
    print("Vehículo ligero")