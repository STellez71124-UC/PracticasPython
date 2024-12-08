# ejemplos de la función Print ()

print ('Hola mundo')
print ('Hola mundo', 'otra vez')
print ('Son las', 9, 'de la mañana')
print ('El resultado de 3 * 4 es:', 3*4)

# ejemplos de cadenas formateadas
print ('El numero 15 en sistema decimal es %d, en sistema octal es %o, en el sistena hexadecimal es %x' % (15, 15, 15))

pi = 3.141592
r = 5
print (f'El radio de un circulo es {r} y el área de ése círculo es {pi * r ** 2 : .2f}')

# Impresión de caracteres especiales
print ('La letra beta es \n\t \u0382')

# caracteres de escape
print('Hola mundo', end = ' ')
print('otra vez', end = '\t')
print('y otra vez')