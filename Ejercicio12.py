'''
Ejercicio 12: Calculadora de Área de un Rectángulo Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
'''
longitud = float(input('Introduce la longitud en cm: '))
ancho = float(input('Introduce el ancho en cm: '))
area = longitud *  ancho
print ('Tu rectángulo tiene un área de :', round(area,4), 'cm2')
