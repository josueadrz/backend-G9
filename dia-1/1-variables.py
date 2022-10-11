# Esto es un comentario
edad = 30

nombre = 'Josue'
apellido = "Pereyra"

#No se puede utilizar  los backtips (comillas invertidas) para los string
# saludo = 'hola como estan mi nombre es ${nombre}'
mensaje = '''el dia de hoy empezo el modulo de backend'''

despedida = """El dia de hoy nos despedimos hasta una nueva oportunidad"""

lasname =  "o'neil"

print(nombre)


especialidad = None
print(especialidad)


# type(var) > devolver q tipo de dato es esa variable
print(type(nombre))
print(type(edad))

# tambien se puede declarar varias variables en una misma linea
curso, grupo, mes, dia, nota = 'Codigo', 'Backend', 'Octubre', 10, 15.4

print(grupo)

# id(var) > mostrar la posicion de memoria en la cual se esta alojando la variable, funcion, clase, etc
print(id(curso))

# del > eliminar la variable (libera la memoria), no se puede volver a utilizar esa variable nunca mas
del curso

print(curso)