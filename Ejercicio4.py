'''
Ejercicio 4: Contador de Vocales Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
palabra= input('Introduce un palabra :')
vocales = 'aeiouAEIOU'
contador = 0

for letra in palabra:
  if letra in vocales:
    contador +=1
    
print('la palabra ' + palabra + ' '+ 'tiene ' + str(contador) +' ' 'vocal(es)')