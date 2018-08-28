"""

CREA UN PROGRAMA QUE ENCUENTRE EL NUMERO MAS PEQUEÑO DE UNA SERIE DE NUMEROS INTRODUCIDOS POR EL USUARIO

"""

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")

numero_pequeño = numeros_usuario[0]

for dato in numeros_usuario:
    if dato < numero_pequeño:
        numero_pequeño = dato

print("El numero mas pequeño es {} ".format(numero_pequeño))
























