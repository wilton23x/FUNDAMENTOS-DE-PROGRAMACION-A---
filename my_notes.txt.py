# Escritura de Archivo de Texto

# 1. Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w'). Si ya existe, sobreescribe su contenido.
with open('my_notes.txt', 'w') as file:
    # 2. Escribimos tres líneas de notas personales en el archivo
    file.write("Primera nota: Estoy practicando manipulación de archivos en Python.\n")
    file.write("Segunda nota: La escritura en archivos es sencilla con el método write().\n")
    file.write("Tercera nota: Siempre recuerda cerrar los archivos para evitar problemas.\n")
# 3. El archivo se cierra automáticamente al salir del bloque 'with'.

# Lectura de Archivo de Texto

# 1. Abrimos el archivo 'my_notes.txt' en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    # 2. Leemos el archivo línea por línea
    line = file.readline()  # Leemos la primera línea
    while line:  # Mientras haya más líneas, ejecutamos el siguiente bloque
        print(line, end='')  # 3. Mostramos cada línea en la consola (sin agregar saltos extra)
        line = file.readline()  # Leemos la siguiente línea
# 4. El archivo se cierra automáticamente al salir del bloque 'with'.

