'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
'''
millas = float(input('Introduce la distancia en millas: '))
km = millas * 1.60934
print(f'{millas} millas corresponden a {round(km,2)} kilómetros')