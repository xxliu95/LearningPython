f = open('test.txt', 'r') # Opciones r to read, w to write, a to append

print(f.name)
print(f.mode)

# Siempre hay que cerrar
f.close()

# Content manager
with open('test.txt', 'r') as f: # Cierra el file automaticamente
    # f_contents = f.read()
    # f_contents = f.readlines() # Devuelve una lista con cada linea
    f_contents = f.readline() # Devuelve una linea y la siguiente vez va a la linea siguiente
    # print(f_contents)
    print(f_contents, end='')

    f_contents = f.readline()
    # print(f_contents)
    print(f_contents, end='')

    # imprime todas las lineas sin escribir todo a la memoria
    # for line in f:
    #    print(line, end='')
    # ir a una linea especifica

with open('test.txt', 'r') as f:
    # recorrer fichiros largos
    size_to_read = 20
    f_contents = f.read(size_to_read) # Lee las 20 primeras letras

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

with open('test.txt', 'r') as f:
    size_to_read = 20

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    print(f.tell())
    # f.seek(0) # Vuelve a la posicion 0 del fichero

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

# with open('text2.txt', 'w') as f:
    # pass # Crearia un fichero vacio
    # f.write('Test')

# Trabajar con multiples ficheros
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Copy picture
with open('lenna.png', 'rb') as rf:
    with open('lenna_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
