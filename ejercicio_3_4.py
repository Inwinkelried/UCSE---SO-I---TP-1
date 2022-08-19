"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Pedirle un texto al usuario y luego ejecutar una función que muestre el mismo texto pero sin las vocales.

Por ejemplo, para un input de:

"Yo estaba allí"

debería mostrar:

"Y stb ll"

"""

def eliminar_vocales(cadena):
  letras = []
  for caracter in cadena:
    if caracter.lower() not in "aeiou":
      letras.append(caracter)
  return ''.join(letras) 

print (eliminar_vocales(input("Ingrese una cadena de texto: ")))
