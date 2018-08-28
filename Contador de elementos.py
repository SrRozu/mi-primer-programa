"""

CREA UN PROGRAMA QUE CUENTE LOS ELEMENTOS DE LA LISTA DE NUMEROS INTRODUCIDA POR EL USUARIO. ESTÁ PROHIBIDO UTILIZAR LEN

"""

lista = []

entrada_usuario = ""

while not entrada_usuario == "FIN":
    entrada_usuario = input("Dime cualquier cosa (Poner 'FIN' para terminar la lista': ")
    lista.append(entrada_usuario)


print("Esta es tu lista añadida: {}".format(lista))


numero_datos = 0

for dato in lista:
    numero_datos += 1


print("El largo de tu lista es: {} ".format(numero_datos))





















