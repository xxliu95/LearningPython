# Comilla simple y doble no hay diferencia
message = 'Hello World'
print(message)

# Length
print(len(message))

# Imprime el caracter con indice 0
print(message[0])

# Imprime una substring inclusive:exclusive
print(message[0:5])
print(message[:5])
print(message[6:])

# Minusculas y mayusculas
print(message.lower())
print(message.upper())

# Contar
print(message.count('l'))  # l sale 3 veces

# Indice return -1 si no encuentra
print(message.find('World'))
print(message.find('Universe'))

# Reemplazar
new_message = message.replace('World', 'Universe')
print(new_message)

# Concatenacion
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!' # Solo versiones recientes
print(message)

# dir() funciones disponibles
# print(dir(name))
# print(help(str))
# print(help(str.lower))
