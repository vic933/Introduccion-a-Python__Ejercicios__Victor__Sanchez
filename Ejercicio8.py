'''
Ejercicio 9: Conversor de Divisas 1 Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
'''
print ('Conversor de divisa $/€')
dolar = float(input('¿cuántos dólares quieres convertir?  :'))
euro = dolar * 0.85
print ('Entonces tienes : ', round(euro,2), '', 'euros')