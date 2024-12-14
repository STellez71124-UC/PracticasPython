entrada = input ('¡Hola! Introduce tu edad:')
edad = 0

if entrada.isnumeric():
    edad = int(entrada)

else:
    print ('Dato incorrecto. Debes introducir un número.')
    exit()

if edad <= 0:
    print ('Wow. Que joven eres. Pero, lo siento, eso no es posible.')

elif edad >=115:
    print ('Vaya. ¿Cómo le haces para vivir tanto? No te creo. Mejor intenta de nuevo.')

elif edad < 18:
    print ('Eres menor de edad, así que no puedes comprar un cigarro.')

else:
    print ('Eres mayor de edad. Aquí tienes tu cigarro.')