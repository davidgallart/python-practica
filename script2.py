contraseña = "mimamamemima"
longitud_minima  = 8
longitud_maxima = 20
texto = "La longitud de la contraseña es"
if len(contraseña) < longitud_minima:
    print(f"{texto} MUY CORTA debe ser como minimo {longitud_minima}")
elif len(contraseña) > longitud_maxima:
    print(f"{texto} DEMASIADO LARGA debe ser maximo {longitud_maxima}")
else:
    print("La longitud de la contraseña es VÁLIDA. Contraseña acceptada")

########################
colores = ["rojo", "verde", "azul", "amarillo"]
for color in colores:
    print(color)

########
contador = 7
while contador <=11:
    print(contador)
    contador+=1
######
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Sofia"))
####################
def cuentaCaracteres(texto) -> int:
    if type(texto) != str:
        return "Debo ser ejecutada con un string"
    return len(texto)

print(cuentaCaracteres("HOla buenas tardes"))
print(cuentaCaracteres(22))
#######################
func = lambda txt: txt[0]
print(func("Hola"))

