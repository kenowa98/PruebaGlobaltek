def suma_serie_repetida(x, n):
    suma = 0
    for i in range(1, n+1):
        num = int(str(x) * i) # resultado de concatenar el mismo número n veces
        suma += num
    return suma

# EJEMPLOS
"""
Entrada : numero=3, terminos=5
Salida : 37035 #(3 + 33 + 333 + 3333 + 33333)
"""
print(suma_serie_repetida(3, 5))
"""
Entrada : numero=5, terminos=3
Salida : 615 #(5 + 55 + 555)
"""
print(suma_serie_repetida(5, 3))