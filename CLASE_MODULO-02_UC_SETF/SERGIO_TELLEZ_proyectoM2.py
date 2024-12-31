print ('Hola. Me gustaria hacer un ejercicio contigo. \nNecesito que escribas seis palabras para formar una lista.')
print ('Tus respuestas deben tener entre cuatro y ocho letras.')
print ('\nA ver, cuentame en que palabra estas pensando ahora.')

text_lista = [] #Lista para almacenar datos ingresados.
text_valid = 0 #Contador de palabras.
while text_valid <6: #Limite para ingresar seis palabras.
    palabra = input(f'Palabra {text_valid+1}: ') #Ingreso de datos que se modifica con cada validación de texto.
    if palabra.isalpha() and len(palabra) < 4: #Verificar si es palabra con menos de 4 letras.
        print ('Hacen falta letras. Solo tiene', len(palabra), 'letras')
    elif palabra.isalpha() and len(palabra) > 8: #Verificar si es palabra con mayor de 8 letras.
        print ('Sobran letras. Tiene', len(palabra), 'letras')
    elif palabra.isalpha() and len(palabra) >= 4 <= 8: #Verificar si es palabra dentro de rango aceptable (4-8 letras).
        print ('Gracias. Ya guarde tu respuesta.')
        text_lista.append(palabra) #Palabra es agregada a lista.
        text_valid +=1 #Suma de valor 1 por cada palabra guardada y reconocida.
    elif palabra.isnumeric(): #Rechazo de números como dato valido para ejecución del programa.
        print ('Solo letras por favor.')
    else:
        print ('Escribe una palabra por favor.')

print ('\nExcelente. Estas fueron las seis respuestas que me compartiste.')
for numero, texto in enumerate(text_lista): #Enumeración de palabras presentes en lista.
    print (f'{numero+1}.- {texto}') #Impresión de lista de palabras ingresadas por el usuario.
print ('\n¿Qué te parece si hacemos otro ejercicio?')
print ('Tu objetivo es ubicar un punto dentro de un plano cartesiano.')

print ('\n¿Qué coordenadas deseas ingresar para el eje horizontal y vertical?')
coordenadas = ['X:','Y:'] #Lista para almacenar valores de eje horizontal y vertical.
num_valid = 0 #Contador para estabilizar operación.
while num_valid <1: #Limite para establecer valores de X y Y.
    try:
        eje_x = int(input('Ingresa el valor de X: '))
        eje_y = int(input('Ingresa el valor de Y: '))
        if eje_x == 0 or eje_y == 0: #Rechazo de valor 0 absoluto como dato valido para ejecución del programa.
            print ('Ingrese un número valido por favor.')
        else:
            coordenadas.insert(1,eje_x)
            coordenadas.insert(3,eje_y)
            num_valid +=1
    except ValueError: #Detección y reinicio de programa al ingresarse datos distinto a número entero.
        print ('Solo se permiten números enteros.')

if coordenadas[1] >=1 and coordenadas[3] >=1: #Cumplimiento de supuesto valor positivo / valor positivo.
    print ('\nEl punto ubicado en',coordenadas, 'se encuentra en el cuadrante I.')
    print ('Tu valor horizontal (X) es positivo y el vertical (Y) es positivo.')
elif coordenadas[1] <=-1 and coordenadas[3] >=1:#Cumplimiento de supuesto valor negativo / valor positivo.
    print ('\nEl punto ubicado en',coordenadas, 'se encuentra en el cuadrante II.')
    print ('Tu valor horizontal (X) es negativo y el vertical (Y) es positivo.')
elif coordenadas[1] <=-1 and coordenadas[3] <=-1: #Cumplimiento de supuesto valor negativo / valor negativo.
    print ('\nEl punto ubicado en',coordenadas, 'se encuentra en el cuadrante III.')
    print ('Tu valor horizontal (X) es negativo y el vertical (Y) es negativo.')
elif coordenadas[1] >=1 and coordenadas[3] <=-1: #Cumplimiento de supuesto valor positivo / valor negativo.
    print ('\nEl punto ubicado en',coordenadas, 'se encuentra en el cuadrante IV')
    print ('Tu valor horizontal (X) es positivo y el vertical (Y) es negativo.')

print ('Gracias por apoyarme con la realización de esta tarea. ¡Hasta luego!')