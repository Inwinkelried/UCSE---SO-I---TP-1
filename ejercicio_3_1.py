"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:

Hacer una función que recibe un número y contesta "par" o "impar" en función de si el número es par o no.

"""

def par_impar(numero):
    if numero % 2 ==0:
        return ("par")
    else:
        return ("impar")

n = int(input("Ingrese un número: "))
print(par_impar(n))