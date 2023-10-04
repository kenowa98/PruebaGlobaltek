def procesar_lista(lista):
    resultado = []

    for numero in lista:
        # Verificar si el número es mayor que 1000
        if numero > 1000:
            return resultado
        else:
            # Verificar si el número es divisible por cinco y menor o igual a 600
            if numero % 5 == 0 and numero <= 600:
                resultado.append(numero)

    return resultado

# EJEMPLOS
"""
Entrada : [24, 150, 300, 660, 295, 1050, 50]
Salida : [150, 300, 295]
"""
print(procesar_lista([24, 150, 300, 660, 295, 1050, 50]))
"""
Entrada : [110, 720, 307, 555, 1095, 12, 300, 1000]
Salida : [110, 555]
"""
print(procesar_lista([110, 720, 307, 555, 1095, 12, 300, 1000]))