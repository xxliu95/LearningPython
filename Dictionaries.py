student = {'name': 'Juan', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['courses'])

# getter
print(student.get('name'))
# print(student['phone']) # Da error
print(student.get('phone')) # Getter si no hay devuelve None
print(student.get('phone', 'Not Found'))

# Setter
student['phone'] = '555-5555'
student['name'] = 'Jose'
print(student)
# O tambien
student.update({'name': 'Carlos', 'age': 26})
print(student)

# Eliminar
del student['age']
print(student)

phone = student.pop('phone')
print(phone)

# KV
student = {'name': 'Juan', 'age': 25, 'courses': ['Math', 'CompSci']}

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# for loop
for key, value in student.items():
    print(key, value)
