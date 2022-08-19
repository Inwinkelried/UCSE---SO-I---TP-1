"""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Siendo:

a -> "Hola"
b -> "mundo"
c -> 87
d -> 2.33145

Realizar un programa que visualice las siguientes cadenas:

"Hola mundo" (usando a y b)
"-Hola-mundo-" (usando a y b)
"El resultado es: 87" (usando c)
"El resultado es: 87min (5220seg)" (usando c ambas veces)
"La temperatura es: 2.3" (usando d).
"""

a = "Hola"
b = "mundo"
c = 87
d = 2.33145

print(a, b)
print("-"+a+"-"+b+"-")
print("El resultado es:", c)
print("El resultado es:", str(c) + "min",  "(" + str(c*60) + "seg" + ")")
print("la temperatura es:", d.__round__(1))


