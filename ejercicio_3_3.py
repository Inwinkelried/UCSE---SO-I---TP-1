"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Hacer una función que reciba un texto y devuelva el mismo texto pero con cada palabra invertida.

Por ejemplo, llamándola con:

"Esto es una prueba"

debe devolver:

"otsE se anu abeurp"

"""

def invertir_texto(cadena):

    palabra = cadena.split()
    palabra_invertida = [x[::-1] for x in palabra]
    textoinv = " ".join(palabra_invertida)
    return(textoinv)

cadena=input("Ingrese una cadena de string")
print (invertir_texto(cadena))