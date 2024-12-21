numero = [1,3,7,9,11]
frutas = ['sandia', 'pera', 'manzana', 'aguacate','melon','papaya']
datos = [0, 'Juan', 8.75, 'Ji', True, False]

print (datos[3])
print (numero[-1], frutas[-1], datos [-1])

numero.append (37)
print (numero[-1])
numero.remove (37)
print (numero[-1])

for i in datos:
    print (i)

elevacion = [x**2 for x in range (1,9)]
print (elevacion)

colores = ('Azul', 'Rojo', 'Verde', 'Negro', 'Cafe')
numerostupla = (1,4,9,6,2,5,1,3,6,4,9,8,1)

print (len(colores))
print (len(numerostupla))
print (numerostupla.count(1))


diccionarioalpha = dict([
    ('Altair','Tepic'),
    ('Carlos','Bogota'),
    ('Sergio','Guanajuato'),
    ('Josue','Guadalajara'),
    ('Elker','Monterrey'),
    ('Jose','Mexico'),
    ])
print (diccionarioalpha)

diccionariobeta = {
    'Nombre':'Silvestre',
    'Apellido':'Revueltas',
    'Edad':'45',
    'Profesion':'Compositor',
}
print (diccionariobeta)

#Ejercicio para calmar la ansiedad.
print ('Bienvienido a tu acompañamiento virtual durante este proceso de ansiedad')
print ('¿Que te parece si vamos a enumerar cosas que pueden percibir tus sentidos?')
#Creación de listas para almacenar elementos ingresados.
#5 cosas visibles
#4 cosas que puedas escuchar
#3 cosas que puedas saborear
#2 cosas que puedas oler
#1 cosa que puedas tocar
lista_visual = []
lista_auditiva = []
lista_gusto = []
lista_olfato = []
lista_tacto = []
#Pedir usuario ingreso de datos para cada lista
print ('Piensa en cinco objetos que puedes ver al tu alrededor.')
for i in range (5):
    item = input (f'Elemento {i+1}: ')
    lista_visual.append(item)

print ('Piensa en cuatro cosas que puedes oir en donde estar.')
for i in range (4):
    item = input (f'Elemento {i+1}: ')
    lista_auditiva.append(item)

print ('Piensa en tres cosas que imaginas poder saborear ahora mismo.')
for i in range (3):
    item = input (f'Elemento {i+1}: ')
    lista_gusto.append(item)

print ('Piensa en dos aromas que sentir en tu entorno.')
for i in range (2):
    item = input (f'Elemento {i+1}: ')
    lista_olfato.append(item)

print ('Piensa en un objeto que puedas tocar con tus manos, pies o cuerpo.')
for i in range (1):
    item = input (f'Elemento {i+1}: ')
    lista_tacto.append(item)

print ('Puedes ver:',lista_visual)
print ('Puedes oir:',lista_auditiva)
print ('Puedes saborear:',lista_gusto)
print ('Puedes oler:',lista_olfato)
print ('Puedes tocar:',lista_tacto)