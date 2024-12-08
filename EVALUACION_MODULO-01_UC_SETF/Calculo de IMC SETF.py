print ('¡Hola! Bienvenido a tu calculadora de Índice de Masa Corporal. \n¿Me permites un poco de tu tiempo para realizar esta operación?')

lista_metricas = [] #Lista donde los datos numericos del sujeto interesado son ingresados para confirmar su entrada

def consentimiento(): #Menu de inicio / reinicio de la calculadora
    while True:
        permisopersona = input('Continuar proceso - S / En otro momento - N: > ') #Decision para empezar con captura de datos o cerrar el programa en Python.
        if permisopersona == 'S' or permisopersona == 's':
            print ('¡Excelente! Antes de continuar, me gustaría saber un poco de ti, o bien, de la persona que deseas evaluar.')
            print ('--------------------------------------------------------------')
            capturadatos_generales () #Procede a avanzar a captura de nombres y valores numericos del sujeto interesado y su cuerpo fisico.
        elif permisopersona == 'N' or permisopersona == 'n':
            print ('Quiza en otra ocasión. ¡Cuidate mucho! ¡Adios!')
            break # Concluye programa desde un primer inicio o en caso de ya haberse completado calculo IMC y no desear capturar datos de otra persona.
        else:
            print ('Por favor ingresa un dato correcto')

def capturadatos_generales():
    while True:
        nombre = input ('Nombre, apellido paterno y apellido materno del interesado: ') #Captura de nombres en forma de oración / string de texto.
        nombrecompleto = nombre.split() #Division de nombres de oración ingresada por usuario a lista de texto generada automaticamente.
        listanombrebool = [] #Verificación de lista de nombres.
        nombrecompleto = nombre.title() #Conversión de nombre mal escrito / puras minusculas a palabra individual que inicia con mayusculas.
        contarnombre = 0 #Conteo de nombres ingresados, mínimo necesario de tres nombres con tres caracteres en adelante.
        for i in nombrecompleto:
            i = i.isalpha() #Comprobación de existencia de solo letras en nombre ingresado.
            listanombrebool.append(1)
        for palabra in nombre.split():
            if len(palabra) >= 3: #Verificación de al menos tres caracteres en cada nombre de la oración inicial.
                contarnombre += 1 #Conteo de palabras individuales ingresadas a partir de nombre proporcionado por el usuario.
        if False in listanombrebool or contarnombre < 3 or len(nombrecompleto)<=9:
            print ('Solo se permiten letras. Gracias.')
        else:
            print (f'<<< Resultado Proceso Captura | Nombre: {nombrecompleto} >>>')
            print ('Nombre y apellidos registrados con éxito.') #Registro de respuesta con formato de texto adecuado.
            print ('--------------------------------------------------------------')
            break

    while True:
        try:
            edadpersona = int(input("Escribe la edad del interesado: ")) #Ingreso de edad del usuario.
            lista_metricas.append(edadpersona) #Se añade a lista de registro y muestra de resultados captura de datos.
            if edadpersona >= 1 and edadpersona < 18: #Condición donde se acredita ser menor de edad y cambian parametros de IMC.
                print (f'<<< Resultado Proceso Captura | Edad: {lista_metricas} >>>')
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            elif edadpersona >= 18 and edadpersona <= 99: #Condición donde se acredita ser mayor de edad y cambian parametros de IMC.
                print (f'<<< Resultado Proceso Captura | Edad: {lista_metricas} >>>') #Se muestra impresión de dato almacenado en el sistema.
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            else:
                print("Por favor, se honesto en tu respuesta.")
        except ValueError: #ingreso de número fictico o dato erroneo
            print("Solo números. Gracias.")

    while True:
        try:
            pesokilos = float(input("Anota su peso en kilogramos (Entre 10kg y 200kg): ")) #Ingreso de peso en kilogramos del usuario de números enteros y/o decimales.
            lista_metricas.append(pesokilos) #Se añade a lista de registro y muestra de resultados captura de datos.
            if pesokilos >= 10 and pesokilos < 250: #Rango de kilogramos contemplados por la calculadora.
                print (f'<<< Resultado Proceso Captura | Peso: {lista_metricas[1]} >>>') #Se muestra impresión de dato almacenado en el sistema.
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            else:
                print("Por favor, se honesto en tu respuesta.")
        except ValueError: #ingreso de número fictico o dato erroneo
            print("Solo escriba números. Gracias.")

    while True:
        try:
            estaturapersona = float(input("Anota su altura en centimetros (Entre 75cm y 210cm): "))/100 #Ingreso de estatura del usuario y su conversion a cifra con dos decimales posibles.
            lista_metricas.append(estaturapersona) #Se añade a lista de registro y muestra de resultados captura de datos.
            if estaturapersona >= 0.75 and estaturapersona < 2.20:
                print (f'<<< Resultado Proceso Captura | Estatura: {lista_metricas[2]} >>>') #Se muestra impresión de dato almacenado en el sistema.
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            else:
                print("Por favor, se honesto en tu respuesta.")
        except ValueError: #ingreso de número fictico o dato erroneo
            print("Solo escriba números. Gracias.")
            

    while True:
        operacion = round(pesokilos/estaturapersona/estaturapersona) #Operación de calculo del IMC a partir de datos almacenados anteriormente.
        imc = operacion #Vinculación entre variables para determinar clasificación del IMC.
        print ('Muchas gracias por tomarte el tiempo para llenar este formulario.')
        print ('Te presento todos datos que ingresaste hasta ahora y su respectivo Índice de Masa Corporal.')
        print ('El Índice de Masa Corporal ofrecido a continuación es solo un marcador matemático simple.')
        print ('Por favor consulta a tu médico de cabecera para revisar a profundidad tu cuerpo y estado de salud.')
        print ('--------------------------------------------------------------') #Total de datos capturados en una misma operación del programa.
        print ('Nombre: ',nombrecompleto,' |  Edad: ',edadpersona,'años\nPeso: ',pesokilos,'kilogramos  |  Estatura: ',estaturapersona,'metros  |  IMC:',operacion,'')
        print ('--------------------------------------------------------------')
        print ('El Índice de Masa Corporal se obtiene con la operación peso(kg)/estatura(m)**2 = IMC.')
        if edadpersona <= 11 and imc < 13.10: #Inicio de posibles resultados y clasificaciones de IMC para menor y mayor de edad.
            print ('El valor del IMC obtenido se puede clasificar como: DESNUTRICIÓN SEVERA.')
        elif edadpersona <= 11 and imc >= 13.10 and imc <= 14.09:
            print ('El valor del IMC obtenido se puede clasificar como: DESNUTRICIÓN MODERADA.')
        elif edadpersona <= 11 and imc >= 14.10 and imc <= 19.29:
            print ('El valor del IMC obtenido se puede clasificar como: PESO NORMAL o SALUDABLE.')
        elif edadpersona <= 11 and imc >= 19.30 and imc <= 22.59:
            print ('El valor del IMC obtenido se puede clasificar como: SOBREPESO.')
        elif edadpersona <= 11 and imc > 22.60:
            print ('El valor del IMC obtenido se puede clasificar como: OBESIDAD.')
        if edadpersona > 11 and edadpersona < 18 and imc < 15.69:
            print ('El valor del IMC obtenido se puede clasificar como: DESNUTRICIÓN SEVERA.')
        elif edadpersona > 11 and edadpersona < 18 and imc >= 15.70 and imc <= 17.29:
            print ('El valor del IMC obtenido se puede clasificar como: DESNUTRICIÓN MODERADA.')
        elif edadpersona > 11 and edadpersona < 18 and imc >= 17.30 and imc <= 24.99:
            print ('El valor del IMC obtenido se puede clasificar como: PESO NORMAL o SALUDABLE.')
        elif edadpersona > 11 and edadpersona < 18 and imc >= 25.00 and imc <= 29.29:
            print ('El valor del IMC obtenido se puede clasificar como: SOBREPESO.')
        elif edadpersona > 11 and edadpersona < 18 and imc > 29.30:
            print ('El valor del IMC obtenido se puede clasificar como: OBESIDAD.')
        elif edadpersona >= 18 and imc < 18.50:
            print ('El valor del IMC obtenido se puede clasificar como: INFERIOR A LA MEDIA o BAJO DE PESO.')
            print ('IMC consistente en posible transtorno alimentario, carencia de nutrientes o disposición genética.')
        elif edadpersona >= 18 and imc >= 18.50 and imc <= 24.99:
            print ('El valor del IMC obtenido se puede clasificar como: PESO NORMAL o SALUDABLE.')
            print ('En teoría, su IMC muestra que esta en buen estado físico y sin sufrir alteraciones.')
        elif edadpersona >= 18 and imc >= 25.00 and imc <= 29.99:
            print ('El valor del IMC obtenido se puede clasificar como: PRE-OBESIDAD o SOBREPESO.')
            print ('Tome precauciones. Quiza deba realizar cambios a habitos alimenticios y actividades cotidianas.')
        elif edadpersona >= 18 and imc >= 30.00 and imc <= 34.99:
            print ('El valor del IMC obtenido se puede clasificar como: OBESIDAD CLASE I.')
            print ('IMC consistente en posible desequilibrio hormonal, exceso de calorias y dieta no balanceada.')
        elif edadpersona >= 18 and imc >= 35.00 and imc <= 39.99:
            print ('El valor del IMC obtenido se puede clasificar como: OBESIDAD CLASE II.')
            print ('IMC consistente en posible dificultad para moverse y respirar, sudoración excesiva y fatiga.')
        elif edadpersona >= 18 and imc >= 40.00:
            print ('El valor del IMC obtenido se puede clasificar como: OBESIDAD MÓRBIDA.')
            print ('IMC consistente en posible hipertensión arterial, dolor articular crónico y caso de diabetes.')
        print ('--------------------------------------------------------------') #fin de lista de posibles resultados y clasificaciones del IMC.
        print ('Seria todo de mi parte. ¿Deseas saber el IMC de otra persona?') #Retorno a menu de la calculadora IMC para reiniciar captura datos o cerrar programa.
        listanombrebool.clear()
        lista_metricas.clear() # Vaciado de listas para ingresar nuevos datos de sujeto interesado en saber IMC
        break

if __name__ == "__main__": #Ejecución de código como Script en Python.
    consentimiento ()