nombre = input('¿cómo te llamas? ')
print('Hola ' + nombre)

edad = input('¿Cúantos años tienes? ')
print (type(edad))
print (f'{nombre} tiene {edad} años')

# Programa que pide dos números al usuario y los suma

numero1 = int(input('Introduce un número por favor: '))
numero2 = int(input('Introduce otro número por favor: '))
numero3 = numero1 + numero2

print(f'El resultado de la suma es {numero3}')