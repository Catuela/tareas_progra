peli1 = int(input('ingresa calificacion (en numeros enteros entre 1 y 10) de una pelicula: '))
if peli1 < 0 or peli1 > 11:
    peli1 = int(input('ingresar calificacion dentro de los numeros dados'))

peli2 = int(input('ingresar calificacion segunda pelicula: '))
if peli2 < 0 or peli2 > 11:
    peli2 = int(input('ingresar calificacion dentro de los numeros dados'))

peli3 = int(input('ingresar calificaion tercera pelicula: '))
if peli3 < 0 or peli3 > 11:
    peli3 = int(input('ingresar calificacion dentro de los numeros dados'))

print('ahora se sacara el promedio de las tres clasificacion ingresadas.')

pro = (peli1 + peli2 + peli3) / 3
print('el promedio es de ', pro) 
