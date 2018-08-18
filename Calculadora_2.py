"""

OBETENER LA TABLA DE MULTIPLICAR (5 AL 15) DE UN NUMERO ESPECIFICADO POR EL USUARIO (Mostrar solo multiplos de 2)

"""

numero_tabla = int(input("Dime un número con el que hacer una tabla de multiplicar: "))


for multiplo in range(5, 16):
    resultado = multiplo * numero_tabla
    if resultado % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, resultado))

