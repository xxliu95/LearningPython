courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)

# Longitud
print(len(courses))

# Indice
print(courses[0])
print(courses[-1]) #imprime el ultimo. Util cuando no sabes la longitud

# Slicing
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# Anadir
courses.append('Art') # Al final
courses.insert(1, 'Chemistry') # En la posicion 1
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Chemistry']
courses.extend(courses_2) # Otra lista
print(courses)

# Eliminar
courses.remove('Math')
popped = courses.pop() # el ultimo

print(popped)

# Ordenar
courses.reverse()
print(courses)

num = [1, 5, 2, 4, 3]
num.sort() # Altera la lista original
print(num)

num.sort(reverse = True)
print(num)

num = [1, 5, 2, 4, 3]
sorted_num = sorted(num) # No altera
print(sorted_num)

# Maximo y minimo
print(min(num))
print(max(num))
print(sum(num))

# Buscar
print(courses.index('History'))
print('History' in courses) # Comprueba si esta o no

# For
for item in courses:
    print(item)

# for index, item in enumerate(courses):
for index, item in enumerate(courses, start = 1):
    print(index, item)

# to String
course_str = ', '.join(courses)
print(course_str)

# String to list
new_list = course_str.split(', ')
print(new_list)

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Inmutable (no se puede reasignar los elementos)
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # Va a dar error

# Sets (no importa el orden y no exite duplicados)
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)
print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty lists
empty_list = []
empty_list = list()

# Empty tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # NO SE PUEDE!
empty_set = set()
