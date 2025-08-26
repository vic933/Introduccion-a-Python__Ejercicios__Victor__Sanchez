'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
numero = int(input ('Introduce el número entero que desees: '))
pares = 0
impares = 0
for i in range(numero):
  if numero % 2 ==0:
    pares =+1
  else:
    impares =+1
print(f'Hay un total de {pares} números pares')
print(f'Hay un total de {impares} números impares')