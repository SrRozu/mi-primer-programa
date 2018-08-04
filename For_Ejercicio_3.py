
" CREA UN PROGRAMA QUE CAMBIA LAS VOCALES POR SU NUMERO DE APARICIÓN. 'AURORA VOREAL' SE CONVERTIRÍA EN '12R3R4 B5R67L' "



entrada_usuario = input("Dime cualquier cosa: ")


if entrada_usuario.find("a" or "A"):
    entrada_usuario = entrada_usuario.replace("a" or "A", entrada_usuario.index("a"))


print(entrada_usuario)


















