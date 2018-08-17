"""

CREA UN PROGRAMA QUE SEA CAPAZ DE CONTAR ESPACIOS, PUNTOS Y COMAS DE UNA STRING INTRODUCIDA POR EL USUARIO

"""


entrada_usuario = input("Dime una frase loco: ")

espacio = " "
punto = "."
coma = ","

n_espacios = 0
n_puntos = 0
n_comas = 0

for dato in entrada_usuario:
    if espacio in dato:
        n_espacios += 1

    if punto in dato:
        n_puntos += 1

    if coma in dato:
        n_comas += 1

print("Hay {} espacios".format(n_espacios))
print("Hay {} puntos".format(n_puntos))
print("Hay {} comas".format(n_comas))
