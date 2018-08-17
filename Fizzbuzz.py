"""
REALIZAR EL FIZZBUZZ PERO CUANDO EL NUMERO SEA DIVISIBLE ENTRE 3 Y 5, QUE EL TEXTO SEA 'BAZINGA'
"""


mi_lista = [2, 3, 12, 35, 21, 13, 45, 70]


for indice in range(len(mi_lista)):
    numero = mi_lista[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        mi_lista[indice] = ""

        if numero % 3 == 0:
            mi_lista[indice] = "fizz"

        if numero % 5 == 0:
            mi_lista[indice] = "buzz"

        if numero % 3 == 0 and numero % 5 ==0:
            mi_lista[indice] = "Bazzinga"

print(mi_lista)






























