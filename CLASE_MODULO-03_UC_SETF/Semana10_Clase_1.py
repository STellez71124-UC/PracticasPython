def historia_colectiva():
    print("Bienvenidos a la gran historia de nuestros alumnos y Python.")
    nombre = input("Dime el nombre del personaje principal: ")

    print(f"{nombre} llegó a la primera clase con mucha curiosidad.")
    print(f'Empezó a experimentar con el uso de Python.')
    print('¿Recuerdas si puso atención en aquella ocasión?')
    atencion = input('Me parece que si (S) / Creo que no (N): ')
    if atencion == 'S' or atencion == 's':
        print ('Estaba muy atento a la clase. Parecia que transcribia cada lección en su código.')
    elif atencion == 'N' or atencion == 'n':
        print ('Le costaba trabajo mantenerse despierto. No podia entender la clase por completo.')


historia_colectiva()