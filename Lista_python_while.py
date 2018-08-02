
mi_lista = ["Patata", "huevo", "leche", "havena", "fruta"]

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("esta es la lista de la compra")