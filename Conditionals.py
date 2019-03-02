# Operaciones == != > < >= <= is
language = 'Python'

# if statement (No existe switch case)
if language == 'Java':
    print('Language is Java')
elif language == 'Python':
    print('Language is Python')
else:
    print('No match')

# and or not
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
# if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')

# is
a = [1, 2, 3]
b = [1, 2, 3]
# b = a

print(a == b)
print(a is b) # no comparten memoria
print(id(a))
print(id(b))

# Valores para falso
# False
# None
# Cero en cualquier tipo numerico
# Secuencia o diccionarios vacios
condition = {}
if condition:
    print('True')
else:
    print('False')
