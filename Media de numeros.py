"""

CREA UN PROGRAMA QUE CALCULE LA MEDIA DE LOS ELEMENTOS DE LA LISTA DE NUMEROS INTRODUCIDA POR EL USUARIO (MEDIA = SUMA DE TODOS LOS NUMEROS / NUMERO DE NUMEROS)

"""

numeros_usuario = []

entrada_usuario = ""

while not entrada_usuario == "FIN":
    entrada_usuario = input("Dime un número: ")
    if entrada_usuario.isdigit():
        numeros_usuario.append(entrada_usuario)
        print("Has añadido un número")

print("Esta es tu lista de números: {}".format(numeros_usuario))

numero_de_numeros = len(numeros_usuario)
suma = 0

for numero in numeros_usuario:
    suma += int(numero)

media_numeros = suma / numero_de_numeros

print("La media de todos tus números es: {}".format(media_numeros))