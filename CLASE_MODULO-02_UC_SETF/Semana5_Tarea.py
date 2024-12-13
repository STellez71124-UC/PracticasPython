# Posibles actividades a realizar una vez conluida la jornada laboral.

print ('Hola. ¿Cómo estas? \nMe percate que estas a punto de salir del trabajo. ¿A donde piensas ir ahora?')
print ('1.- Ir directo a la casa. \n2.- Ir por comida. \n3.- Realizar pagos. \n4.- Dar una vuelta. \n5.- Visitar una tienda')
entrada = int(input ('Cuentame que planeas hacer: '))
if entrada == 1:
    print ('Muy bien. Te veo alla cuando enciendas tu computadora de nuevo.')
elif entrada == 2:
    print ('Excelente idea. No olvides comprar algo de llevar para la familia.')
elif entrada == 3:
    print ('Que bueno que te acordaste. Espero que no te cobren recargos')
elif entrada == 4:
    print ('Me parece bien. Sirve que vas a la gasolinera para llenar el tanque.')
elif entrada == 5:
    print ('Ya. Puede que encuentres un nuevo libro en tu recorrido.')
else:
    print ('Disculpa, no entendí tu respuesta.')