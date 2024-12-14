x = 5
while x>0:
    print ('Al infinito y mas allá.')

for i in range (1,101):
    print ('No debo platicar en clase.')

palabracorrecta = 'Dinosaurio'
numerointentos = 0
maxintentos = 3
while numerointentos < maxintentos:
    print ('Hola, se me viene a la mente un animal famoso en el cine.')
    adivina = input ('Adivina la palabra en que estoy pensando: ').title
    numerointentos += 1
    if adivina == palabracorrecta:
        print ('Es correcto.')
    elif numerointentos == 1:
        print ('Una pista. Seguramente lo tuviste como juguete de niño.')
    elif numerointentos == 2:
        print ('Otra pista. Ya no existe en la actualidad')
    elif numerointentos == 3:
        print ('No le atinaste. Quiza en la siguiente ocasión lo adivines correctamente.')
    else:
        print ('Lo siento, no entendí tu respuesta.')