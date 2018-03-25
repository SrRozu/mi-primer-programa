

apetece_helado_input = input("¿te apetece un helado? (si/no): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no")
    apetece_helado = False

tienes_dinero_input = input("¿tienes dinero para un helado? (si/no):").upper()
esta_tu_tia_cerca_input = input("¿estas con tu tia? (si/no):").upper()
esta_el_senor_helados_input = input("¿esta el señor de los helados? (si/no):").upper()



apetece_helado = apetece_helado_input == "SI"
puedes_permitirtelo = tienes_dinero_input == "si" or esta_tu_tia_cerca_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"


if apetece_helado and puedes_permitirtelo and esta_el_senor_helados:
    print("comete un helado")
else:
    print("pues no te lo comas")

    







































