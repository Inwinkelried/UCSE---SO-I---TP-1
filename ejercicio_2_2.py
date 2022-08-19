"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Hacer un programa que le pida una cadena al usuario, y arme una triángulo creciente y decreciente con ese texto.

Por ejemplo, para el texto "klop", el resultado sería:

k
kl
klo
klop
klo
kl
k
"""
palabra = (input("Ingrese una palabra: "))
lenght = (len(palabra) )
x = -1
while (x != lenght):
    x += 1
    print (palabra[0:x])
while (x != 0):
    x -=1
    print (palabra[0:x])
   
    
