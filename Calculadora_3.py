"""

CREA UN PROGRAMA QUE MUESTRE LA TABLA DE MULTIPLICAR DE UN NUMERO INTRODUCIDO POR EL USUARIO, PERO INVERTIDA, COMENZANDO POR EL 10

"""


numero_tabla = int(input("Dime un número con el que hacer una tabla de multiplicar: "))

tabla = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)


for multiplo in tabla:
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))