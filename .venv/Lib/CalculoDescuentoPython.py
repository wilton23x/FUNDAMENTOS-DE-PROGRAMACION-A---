def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devuelve el monto del descuento
    return descuento

# Llamada 1: Solo proporcionando el monto total
monto_total_1 = 100.0  # Ejemplo de compra
descuento_1 = calcular_descuento(monto_total_1)
print(f"Monto total: ${monto_total_1}, Descuento aplicado: ${descuento_1}, Monto final: ${monto_total_1 - descuento_1}")

# Llamada 2: Proporcionando monto total y porcentaje de descuento
monto_total_2 = 200.0  # Ejemplo de otra compra
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
print(f"Monto total: ${monto_total_2}, Descuento aplicado: ${descuento_2}, Monto final: ${monto_total_2 - descuento_2}")

