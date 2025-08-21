'''
Ejercicio 7: Calculadora Simple Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
'''
print ('Operaciones disponibles +, -, *, /')

numero1 = float(input('Introduce el primer numero: '))
numero2 = float(input('Introduce el segundo numero: ')) 
operacion = input ('¿Qué operación deseas hacer: ')
if operacion == '+':
  resultado = numero1 + numero2
  print ('El resultado es: ', resultado)
elif operacion == '-':
  resultado = numero1 - numero2
  print ('El resultado es: ', resultado)
elif operacion == '*':
  resultado = numero1 * numero2
  print ('El resultado es: ', resultado)
elif operacion == '/':
  resultado = numero1 / numero2
  print ('El resultado es: ', resultado)
else :
  print ('Operación no permtida')
  