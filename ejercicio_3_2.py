"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Hacer una función que recibe dos números y devuelve "mayor" (si el primer número es mayor que el segundo), "menor", o "iguales".

"""

def mayor_menor(uno, dos):
    if uno > dos:
        return "mayor"
    elif uno == dos:
        return "iguales"
    else:
        return "menor"

n1 = int(input("Ingrese un número:"))
n2 = int(input("Ingrese otro número:"))
print(mayor_menor(n1,n2))