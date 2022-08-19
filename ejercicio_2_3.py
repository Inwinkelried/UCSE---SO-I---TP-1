"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Si listamos todos los números naturales menores a 10 que son multiplos de 3 o 5, tenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Encontrar y mostrar la suma de todos los multiplos de 3 o 5 menores a 1000.
"""

n=0
suma=0
while (n<1000):
    if(n % 3 ==0):
        suma = suma + n
    elif (n % 5 ==0):
        suma = suma + n

    n= n+1 

print ("La suma de los multiplos de 3 o 5, menores de 1000 son: ", suma)