'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC) Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona. IMC = PESO / ALTURA^2
'''
print ('Vamos a calcular tu IMC : ')
altura = float(input('Introduce tu altura en m: '))
peso = float(input('Introduce tu peso en kg :'))
IMC = peso / (altura*altura)
print ('Tu IMC es: ', round(IMC,2))