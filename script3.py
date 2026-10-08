# lista_edades = [15,22,17,30,65,45,70,19]
# for edad in lista_edades:
#     if edad >= 18:
#         print(edad)
#     if edad >= 65:
#         break
#################################3
intentos = 0
while intentos <=4:

    try:
        numero = int(input("Dime un numero: "))
        if type(numero) == int:
                print("El numero es valido")
                break
    except Exception:
        print("Error, debes introducir numeros")
        intentos+=1
    
