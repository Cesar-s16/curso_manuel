def digitos(num,cont):
    if num < 0:
        num *= -1
    if num==0:
        return cont
    else:
        return digitos(num//10,cont+1)

num = int(input("ingrese el numero a verificar, por favor:\n"))
print("Numero de digitos es: ", digitos(num,0))