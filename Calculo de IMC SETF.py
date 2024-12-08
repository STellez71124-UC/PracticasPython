print ('¡Hola! Bienvenido a tu calculadora de Índice de Masa Corporal. \n¿Me permites un poco de tu tiempo para realizar esta operación?')

lista_metricas = []

def consentimiento():
    while True:
        permisopersona = input('Continuar proceso - S / En otro momento - N: > ')
        if permisopersona == 'S' or permisopersona == 's':
            print ('¡Excelente! Antes de continuar, me gustaría saber un poco de ti, o bien, de la persona que deseas evaluar.')
            print ('--------------------------------------------------------------')
            capturadatos_generales ()
        elif permisopersona == 'N' or permisopersona == 'n':
            print ('Quiza en otra ocasión. ¡Cuidate mucho! ¡Adios!')
            break
        else:
            print ('Por favor ingresa un dato correcto')

def capturadatos_generales():
    while True:
        nombre = input ('Nombre, apellido paterno y apellido materno del interesado: ')
        nombrecompleto = nombre.split()
        listanombrebool = []
        nombrecompleto = nombre.title()
        contarnombre = 0
        for i in nombrecompleto:
            i = i.isalpha()
            listanombrebool.append(1)
        for palabra in nombre.split():
            if len(palabra) >= 3:
                contarnombre += 1
        if False in listanombrebool or contarnombre < 3 or len(nombrecompleto)<=9:
            print ('Solo se permiten letras. Gracias.')
        else:
            print (f'<<< Resultado Proceso Captura | Nombre: {nombrecompleto} >>>')
            print ('Nombre y apellidos registrados con éxito.')
            print ('--------------------------------------------------------------')
            break

    while True:
        try:
            edadpersona = int(input("Escribe la edad del interesado: "))
            lista_metricas.append(edadpersona)
            if edadpersona >= 1 and edadpersona < 18:
                print (f'<<< Resultado Proceso Captura | Edad: {lista_metricas} >>>')
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            elif edadpersona >= 18 and edadpersona <= 99:
                print (f'<<< Resultado Proceso Captura | Edad: {lista_metricas} >>>')
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            else:
                print("Por favor, se honesto en tu respuesta.")
        except ValueError:
            print("Solo números. Gracias.")

    while True:
        try:
            pesokilos = float(input("Anota su peso en kilogramos (Entre 10kg y 200kg): "))
            lista_metricas.append(pesokilos)
            if pesokilos >= 10 and pesokilos < 250:
                print (f'<<< Resultado Proceso Captura | Peso: {lista_metricas[1]} >>>')
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            else:
                print("Por favor, se honesto en tu respuesta.")
        except ValueError:
            print("Solo escriba números. Gracias.")

    while True:
        try:
            estaturapersona = float(input("Anota su altura en centimetros (Entre 75cm y 210cm): "))/100
            lista_metricas.append(estaturapersona)
            if estaturapersona >= 0.75 and estaturapersona < 2.20:
                print (f'<<< Resultado Proceso Captura | Estatura: {lista_metricas[2]} >>>')
                print ('Dato guardado con éxito.')
                print ('--------------------------------------------------------------')
                break
            else:
                print("Por favor, se honesto en tu respuesta.")
        except ValueError:
            print("Solo escriba números. Gracias.")
            

    while True:
        operacion = round(pesokilos/estaturapersona/estaturapersona)
        imc = operacion
        print ('Muchas gracias por tomarte el tiempo para llenar este formulario.')
        print ('Te presento todos datos que ingresaste hasta ahora y su respectivo Índice de Masa Corporal.')
        print ('El Índice de Masa Corporal ofrecido a continuación es solo un marcador matemático simple.')
        print ('Por favor consulta a tu médico de cabecera para revisar a profundidad tu cuerpo y estado de salud.')
        print ('--------------------------------------------------------------')
        print ('Nombre: ',nombrecompleto,' |  Edad: ',edadpersona,'años\nPeso: ',pesokilos,'kilogramos  |  Estatura: ',estaturapersona,'metros  |  IMC:',operacion,'')
        print ('--------------------------------------------------------------')
        print ('El Índice de Masa Corporal se obtiene con la operación peso(kg)/estatura(m)**2 = IMC.')
        if edadpersona <= 11 and imc < 13.10:
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
        print ('--------------------------------------------------------------')
        print ('Seria todo de mi parte. ¿Deseas saber el IMC de otra persona?')
        listanombrebool.clear()
        lista_metricas.clear()
        break

if __name__ == "__main__":
    consentimiento ()