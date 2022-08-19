"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Hacer un programa que le pida una cadena al usuario (usando la función "input") y la imprima a pantalla al revés.

Por ejemplo, para el texto

"Esto es asi"

debería mostrar
da
"isa se otsE"
"""
def InvertirCadena(texto):
    cadenaInvertida = ""
    for caracter in texto:
        cadenaInvertida = caracter + cadenaInvertida
    return (cadenaInvertida)


textoIngresado = input("Ingrese texto: ")
print(InvertirCadena(textoIngresado))

# otra opcion (la más corta) es:
print(textoIngresado[::-1])
