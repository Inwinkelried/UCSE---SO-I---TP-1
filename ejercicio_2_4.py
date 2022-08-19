"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Escribir un programa que le pregunte un número al usuario.

Si el número es 5, que muestre "Suerte!";
Si el número es mayor a 10, que muestre "Grande!";
Para los otros casos que muestre "Sin suerte, :("

"""

n = int(input("Ingrese un numero: "))
if(n == 5):
    respuesta = "Suerte!"
elif (n>10):
        respuesta = "Grande!"
else:
        respuesta = "Sin suerte, :("

print(respuesta)

