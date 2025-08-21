'''
Ejercicio 11: Calculadora de Edad Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
'''
year_of_birth = int(input('Introduce tu año de nacimiento :'))
from datetime import date
today = date.today()
actual_year = today.year
edad = actual_year - year_of_birth
print ('Tu edad es : ',edad,'', 'años')
