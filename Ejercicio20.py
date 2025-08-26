'''
Ejercicio 20: Suma de Números en una Lista Crea un programa que sume todos los números en una lista ingresada por el usuario.
'''
lista_num = input("Introduce una lista de números separados por coma: ")
numeros = [int(x) for x in lista_num.split(",")]
total = sum(numeros)
print(f"La suma total de los números es {total}")
