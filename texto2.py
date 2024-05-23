def sustituir_subcadena(cadena, subcadena, caracter_reemplazo):
    """
    Esta función sustituye los asteriscos (*) por el caracter de reemplazo
    en todas las palabras donde aparezca la subcadena.
    """
    nueva_cadena = ""
    palabras = cadena.split()
    subcadena_encontrada = False
    for palabra in palabras:
        if subcadena in palabra:
            subcadena_encontrada = True
            nueva_palabra = ""
            temp = ""
            for letra in palabra:
                if letra == ' ' or letra == '.':
                    if temp == subcadena:
                        nueva_palabra += '*' * len(temp) + " "
                    else:
                        nueva_palabra += temp + " "
                    temp = ""
                else:
                    temp += letra
            if temp == subcadena:
                nueva_palabra += '*' * len(temp)
            else:
                nueva_palabra += temp
            nueva_cadena += nueva_palabra + " "
        else:
            nueva_cadena += palabra + " "
    if subcadena_encontrada:
        print("Nueva cadena:", nueva_cadena)
    else:
        print("Subcadena no encontrada")

# Ejemplo de uso:
cadena_original = "Esta es una prueba de sustitución de asteriscos en una subcadena."
subcadena = "prueba"
caracter_reemplazo = '-'
sustituir_subcadena(cadena_original, subcadena)
