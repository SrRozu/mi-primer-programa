que_quieres_hacer = input("¿Que quieres hacer? (multiplicar/ dividir/ sumar/ restar): ")
primer_numero = int(input("Dime un numero range(1, 1000): "))
segundo_numero = int(input("Dime otro numero range(1, 1000): "))
resultado = 0

if que_quieres_hacer == "multiplicar":
    resultado = primer_numero * segundo_numero
    print("Resultado:{}".format(resultado))

if que_quieres_hacer == "dividir":
    resultado = primer_numero / segundo_numero
    print("Resultado:{}".format(resultado))

if que_quieres_hacer == "sumar":
    resultado = primer_numero + segundo_numero
    print("Resultado:{}".format(resultado))

if que_quieres_hacer == "restar":
    resultado = primer_numero - segundo_numero
    print("Resultado:{}".format(resultado))