palabracorrecta = ['Dinosaurio', 'dinosaurio', 'DINOSAURIO']
numerointentos = 0
maxintentos = 3
print ('Hola. Acabo de ver un animal increible en el cine.')
while numerointentos < maxintentos:
    adivina = input ('Adivina el animal en que estoy pensando: ')
    numerointentos += 1
    if adivina in palabracorrecta:
        print ('Es correcto. ¿Acaso puedes leer mi mente?')
        break
    elif numerointentos == 1:
        print ('Una pista. Seguramente lo tuviste como juguete de niño.')
    elif numerointentos == 2:
        print ('Te doy otra pista. Ya no existe en la actualidad.')
    else:
        print ('No le atinaste. Quiza en la siguiente ocasión lo adivines correctamente.')