# Definir una funcion en blanco
def hello_func():
    pass

# Ejecutar una funcion
hello_func()

print(hello_func) # Indica que es una funcion
print(hello_func()) # Imprime el valor de return de la funcion

def hello_func():
    print('Hello Function!')

hello_func()

# return
def hello_func():
    return 'Hello Function!'

print(hello_func())

# Puedes tratar la funcion como el tipo de variable que devuelve
print(hello_func().upper())

# Parametros
def hello_func(greeting, name = 'You'):
    # return '{} Function! '.format(greeting)
    return f'{greeting}, {name}!'

print(hello_func('Hi'))
print(hello_func('Hi', 'Michael'))

# Punteros
def student_info(*args, **kwargs):
    print(args) # anade una secuencia
    print(kwargs) # anade un diccionario

student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

# Ejemplo
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    # La siguiente linea se llama Docstring y sirve para documentar
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2020, 2))
