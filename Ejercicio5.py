'''
Ejercicio 5: Suma de Números Pares Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
suma = 0
for numero in range (1,101):
  if numero %2 ==0 :
    suma = suma + numero

print( 'La suma total de los numeros pares del 1 al 100 es ', suma)

numero = int(input ('Introduce un número '))
if numero %2 == 0 :
    print ('El número es par')
else :
    print ('El número es impar')
