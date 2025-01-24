# Funcion Simple

def funcion_simple():
    '''Esta función no hace nada.'''
    pass

# Funcion que saluda al mundo

def saluda():
    '''Esta función saluda al mundo.'''
    print ('Hola mundo.')

print ('Antes de llamar a la función.')
funcion_simple()
saluda()
print ('Ya se ha llamado a la función.')

help(saluda)
help(funcion_simple)