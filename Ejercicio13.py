'''
Ejercicio 13: Verificación de Número Primo Escribe un programa que determine si un número ingresado por el usuario es primo o no.
'''
numero = int(input('Introduce el níumero: '))
if numero > 1:
  es_primo = True
  for i in range (2, numero):
    if numero % i == 0:
      es_primo = False
  if es_primo:
      print ('Este número es primo')
  else:
    print ('Este número no es primo')