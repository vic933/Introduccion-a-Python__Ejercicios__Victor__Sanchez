'''
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
'''
anio = int(input('Introduce un año: '))
if (anio %4 == 0 and anio %100 != 0) or (anio %400 == 0):
  print(f'El año {anio} es bisiesto')
else: 
  print (f'El año {anio} NO es bisiessto')
