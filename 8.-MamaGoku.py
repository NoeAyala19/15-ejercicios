respuesta = "GINE"
Intentos = 0
while True:
    variable = input("¿Cual es el nombre de la mama de Goku?: ")
    variable = variable.upper()
    if variable == respuesta:
        print("Asi es Gine es su nombre")
        break
    else:
        Intentos = Intentos + 1
        if Intentos == 1:
            print("Incorrecto intenta de nuevo (pista \"G\")")
        if Intentos == 2:
            print("Incorrecto intenta de nuevo (pista \"i\")")
        if Intentos == 3:
            print("Incorrecto intenta de nuevo (pista \"n\")")
        if Intentos == 4:
            print("Incorrecto intenta de nuevo (pista \"e\")")
        if Intentos > 4:
            print("Ya atinale wey ya te di todas")
