import os
from datetime import datetime

# Current directory
print(os.getcwd())

# ls
print(os.listdir())

# mkdir
os.mkdir('prueba')
os.makedirs('prueba1/prueba2')

# rmdir
os.rmdir('prueba')
os.removedirs('prueba1/prueba2')

# remane
# os.rename('a.txt', 'b.txt')

# stats
print(os.stat('os_module.py'))
print(os.stat('os_module.py').st_size)
time = os.stat('os_module.py').st_mtime # timestamp ultima moduficacion
print(datetime.fromtimestamp(time))

# walk
for dirpath, dirnames, filenames in os.walk('D:/Dropbox/Python'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

# environ
print(os.environ.get('HOMEPATH'))

# join paths
file_path = os.path.join(os.environ.get('HOMEPATH'), 'a.txt')
print(file_path)

# otros
print(os.path.basename('/tmp/text.txt')) # Nombre del fichero
print(os.path.dirname('/tmp/text.txt')) # Nombre del directorio
print(os.path.split('/tmp/text.txt')) # Ambos anteriores
print(os.path.exists('/tmp/text.txt')) # Mira si existe
print(os.path.isdir('/tmp/text.txt')) # Mira si es directorio
print(os.path.isfile('/tmp/text.txt')) # Mira si es fichero
print(os.path.splitext('/tmp/text.txt')) # Separa la extension del fichero

# Change directory
# os.chdir('D:/Escritorio')
# print(os.getcwd())
