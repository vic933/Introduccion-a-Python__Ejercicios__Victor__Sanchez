'''
Ejercicio 14: Calculadora de Descuento Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
'''
precio = float(input('Introduce el precio original en €: '))
descuento = precio * 0.2
precio_rebajado = precio - descuento
print ('El precio rebajado son: ', round (precio_rebajado,2) , '€')
respuesta = input ('¿Quieres conocer el importe del descuento? (si/no): ')
if respuesta == 'si' :
  print ('El descuento es : ', round(descuento,2) , '€')
else:
  print ('Gracias por usarme')
