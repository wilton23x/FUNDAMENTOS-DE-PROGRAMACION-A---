# Paso 1: Crear un Diccionario
informacion_personal = {
    "nombre": "Wilton Salazar",
    "edad": 20,
    "ciudad": "Cielo Verde",
    "profesion": "Estudiante Univercitario"
}

# Paso 2: Acceder y Modificar Valores
print("Ciudad original:", informacion_personal["ciudad"])  # Imprimir ciudad original
informacion_personal["ciudad"] = "Quito"  # Modificar ciudad
informacion_personal["profesion"] = "Desarrollador"  # Modificar profesión

# Paso 3: Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # 0952451235

# Paso 4: Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar edad

# Paso 5: Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)
