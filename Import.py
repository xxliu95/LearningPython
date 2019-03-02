import my_module
import random
import datetime
import calendar
import math
import os
import sys
# import antigravity
# Asignar funcion
# import my_module as mm
# from my_module import find_index as mm
# from my_module import find_index, test
# from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

# Usar funciones
index = my_module.find_index(courses, 'Math')
print(index)

# directorios que python busca modulos
print(sys.path) # en orden de busqueda
# Anadir path para buscar modulos:
# sys.path.append(dir)

# random por ejemplo
random_course = random.choice(courses)
print(random_course)

# math
rads = math.radians(90)
print(math.sin(rads))

# datetime y calendar
today = datetime.date.today()
print(today)

print(calendar.isleap(2019))

# os
print(os.getcwd())
print(os.__file__)
