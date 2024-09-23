def calcular_descuento(monto_total, porcentaje_descuento=5):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada a la función con otros precios
compra_1_descuento, compra_1_final = calcular_descuento(150.75)  # 5% de descuento por defecto
compra_2_descuento, compra_2_final = calcular_descuento(980.50, 25)  # 25% de descuento

# Mostrar los resultados
print(f"Compra 1 - Descuento: ${compra_1_descuento:.2f}, Monto final: ${compra_1_final:.2f}")
print(f"Compra 2 - Descuento: ${compra_2_descuento:.2f}, Monto final: ${compra_2_final:.2f}")
