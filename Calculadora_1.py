"""

OBETENER LA TABLA DE MULTIPLICAR (5 AL 15) DE UN NUMERO ESPECIFICADO POR EL USUARIO

"""

numero_tabla = int(input("Dime un número con el que hacer una tabla de multiplicar: "))


for multiplo in range(5, 16):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))


































