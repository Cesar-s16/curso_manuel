# Contar la cantidad de vocales de cada palabra y luedo si esa vocal se encuentra mas de tres veces
# se agrega a la lista y luego se ordena de manera descendente
def palabras_con_vocal(texto, vocal):
    palabras = texto.split()
    palabras_con_vocal = []
    for palabra in palabras: 
        palabra = palabra.rstrip(".,¡!¿?")
        if palabra.count(vocal) >= 3:
            palabras_con_vocal.append(palabra)
                      
    # Implementación del algoritmo de ordenamiento de burbuja
    n = len(palabras_con_vocal)
    for i in range(n):
        for j in range(0, n-i-1):
            if (len(palabras_con_vocal[j]), palabras_con_vocal[j]) < (len(palabras_con_vocal[j+1]), palabras_con_vocal[j+1]):
                palabras_con_vocal[j], palabras_con_vocal[j+1] = palabras_con_vocal[j+1], palabras_con_vocal[j]

    return palabras_con_vocal


# Cambiar palabra por asteriscos
def sustituir_subcadena(cadena, subcadena):
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
    
# programa principal
# Parte A
while True:
    texto = input("Ingrese el texto (terminado en punto): ")
    if not texto.endswith('.'):
        opcion = input("El texto introducido no termina en punto. ¿Desea agregarlo automáticamente (S/N)? ").upper()
        if opcion == 'S':
            texto += '.'
            break
        else:
            continue
    else:
        break

while True:
    vocal = input("Ingrese la vocal a buscar: ")
    if vocal.lower() not in 'aeiou':
        print("Error: Debe ingresar una vocal.")
        continue
    else:
        break

palabras_encontradas = palabras_con_vocal(texto, vocal)
print("Palabras con la vocal '",vocal,"' tres o más veces ordenadas por longitud descendente:")
print(palabras_encontradas)

# Parte B
subcadena = input("Ingrese el texto (terminado en punto): ")
sustituir_subcadena(texto, subcadena)