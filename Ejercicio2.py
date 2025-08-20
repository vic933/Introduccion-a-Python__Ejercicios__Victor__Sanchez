'''
Ejercicio 2: Calculadora de Propina Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
'''
cuenta = float(input('Importe de la cuenta: '))
propina = cuenta * 0.15
total = cuenta + propina
print('El total a pagar es de :', total, '€')