'''
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
'''
frase = input('Introduce una frase: ')
#Ahora separo la frase en palabras
palabras = frase.split()
cantidad_palabras = len(palabras)
print(f'Tu frase tiene un número de {cantidad_palabras} palabras')

#segun chat GPT también se puede hacer con un bucle
oracion = input("Introduce una oración: ")

contador = 1  # empezamos en 1, porque al menos hay una palabra

for caracter in oracion:
    if caracter == " ":   # cada vez que encontramos un espacio, hay una nueva palabra
        contador += 1

print(f"La oración tiene {contador} palabra(s).")
