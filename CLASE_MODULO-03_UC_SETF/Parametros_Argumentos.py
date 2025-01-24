def sumar (parametro1,parametro2):
    '''Función que suma dos parametros y los imprime en pantalla.'''
    print ('Suma:',parametro1+parametro2)

argumento1 = 5
argumento2 = 7

#Invocando la función por medio de parámetro variables.
sumar(argumento1,argumento2)

#Invocando la función por medio de parámetros de valor.
sumar('Mundo!','Hola')
sumar('Hola','Mundo!')

#sumar('Hola')

#Parametros opcionales
def muestra_alumno(nombre,edad = 18, sexo = 'F'):
    '''Función que muestra en pantalla nombre, edad y sexo de un alumno.
    Recibe tres parámetros.
    1.- Nombre.
    2.- Edad.
    3.- Sexo.
    '''
    print (f'Nombre: {nombre}, Edad {edad}, Sexo: {sexo}')

#Ejecución de función con parámetro obligatorio.
muestra_alumno('Maria')

#Ejecución de función utilizando parámetro obligatorio y uno opcional.
muestra_alumno('Maria',22)

#Ejecución de función usando primer y último parámetro.
muestra_alumno('Juan',sexo='M')