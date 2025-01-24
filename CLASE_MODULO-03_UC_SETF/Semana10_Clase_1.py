def historia_colectiva():
    print("Bienvenidos a la gran historia de nuestros alumnos y Python.")
    text_valid = 0
    while text_valid < 1:
        nombre = input("Dime el nombre del personaje principal: ")
        if nombre.isalpha() and len(nombre) > 3:
            print(f"\n{nombre} llegó a la primera clase con mucha curiosidad y empezó a experimentar con el uso de Python.")
            text_valid+=1
        else:
            print ('No entendí tu respuesta.')

    print('¿Recuerdas si puso atención en aquella ocasión?')
    while text_valid < 2:
        atencion = input('Me parece que si (S) / Creo que no (N): ')
        if atencion == 'S' or atencion == 's':
            print (f'{nombre} estaba muy atento a la clase. Con pluma, cuaderno y maquina a la mano.')
            print ('Tenia gusto por trabajar y aprender cosas nuevas.')
            text_valid+=1
        elif atencion == 'N' or atencion == 'n':
            print (f'A {nombre} le costaba trabajo mantenerse despierto. Estaba distraido y esperaba con ansias el fin de la clase.')
            text_valid+=1
        else:
            print ('No entendí tu respuesta.')

    print ('\nDespues de un rato, la maestra da instrucciones para hacer un trabajo en clase.')
    print ('Dio veinte minutos para preparar un ejercicio que seria resuelto por otro compañero.')
    print (f'¿Cómo resolvio el problema {nombre}?')
    while text_valid < 3:
        try:
            respuesta = int(input('Por su propia cuenta (1) / Plagio de internet (2) / A la última hora y a ver que sale (3): '))
            if respuesta == 1:
                print (f'{nombre} cumplió la tarea con exito y envió su trabajo al repositorio grupal.')
                text_valid+=1
            elif respuesta == 2:
                print (f'{nombre} solo cambio una que otra oración. Costo poco trabajo, pero al final se envió algo.')
                text_valid+=1
            elif respuesta == 3:
                print (f'{nombre} no sabia bien lo que estaba haciendo. Hizo su esfuerzo pero su trabajo era rebuscado y poco organizado.')
                text_valid+=1
            else:
                print ('No entendí tu respuesta.') 
        except ValueError:
            print ('No entendí tu respuesta.') 



historia_colectiva()