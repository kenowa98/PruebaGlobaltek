def agrupar_elementos_similares(lista):
    grupos = {}  # Usaremos un diccionario para realizar el agrupamiento
    
    for elemento in lista:
        if elemento in grupos:
            grupos[elemento].append(elemento)
        else:
            grupos[elemento] = [elemento]
    
    #Creo una lista con cada uno de los valores del diccionario
    resultado = list(grupos.values()) 
    return resultado

# EJEMPLOS
"""
Entrada : list = [12, 25, 1, 1, 7, 25] 
Salida : [[12], [7], [25, 25], [1, 1]]
"""
print(agrupar_elementos_similares([12, 25, 1, 1, 7, 25]))
"""
Entrada : list = [6, 7, 8, 9] 
Salida : [[6], [7], [8], [9]]
"""
print(agrupar_elementos_similares([6, 7, 8, 9]))