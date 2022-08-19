""""
Alumno: Santiago Inwinkelried
Email: santiagoinwinkelried@gmail.com

Consigna:
Mostrar los números potencia de 2 menores a 10000 de la siguiente manera (respetar formato y salto de línea):

0001
0002
0004
0008
"""

n=0
while 2**n < 10000:
    potencia = str(2**n)
    print (potencia.zfill(4))
    n+=1