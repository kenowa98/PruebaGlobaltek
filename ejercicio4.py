# Listas para almacenar los grupos de productos y sus existencias
dairy_products = []
dairy_stock = []
cleaning_products = []
cleaning_stock = []
grain_products = []
grain_stock = []

# Función para registrar un producto entrante
def registrar_producto(nombre, cantidad, grupo):
    if grupo == "dairy":
        productos = dairy_products
        existencias = dairy_stock
    elif grupo == "cleaning":
        productos = cleaning_products
        existencias = cleaning_stock
    elif grupo == "grain":
        productos = grain_products
        existencias = grain_stock

    if nombre in productos:
        indice = productos.index(nombre)
        existencias[indice] += cantidad
    else:
        productos.append(nombre)
        existencias.append(cantidad)

# Función para visualizar el inventario completo
def visualizar_inventario():
    spaces = 10
    for grupo, productos, existencias in [("Dairy", dairy_products, dairy_stock), ("Cleaning", cleaning_products, cleaning_stock), ("Grain", grain_products, grain_stock)]:
        if len(productos) > 0:
            print(f"\nGrupo: {grupo}")
            max_name = len(max(productos))
            titulo = "Nombre" + " " * (max_name - 6 + spaces) + "Existencias"
            print(titulo)
            print("-" * (len(titulo)))
            for i in range(len(productos)):
                print(f"{productos[i]}{' ' * (max_name - len(productos[i]) + spaces)}{existencias[i]}")

# Ejecutar Consola
while True:
    print("\nSistema de inventario. Ingrese una opción:")
    print("--------------------------------------------")
    print("1. Agregar producto")
    print("2. Ver reporte de inventario")
    print("3. Salir")
    opcion = input("\nSu opción: ")

    if opcion == "1":
        while True:
            grupoOpt = int(input("Digita el número del grupo al que pertenece (1-dairy, 2-cleaning, 3-grain): "))
            if grupoOpt in [1,2,3]:
                if grupoOpt == 1:
                    grupo = "dairy"
                else:
                    grupo = "cleaning" if grupoOpt == 2 else "grain"
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        registrar_producto(nombre, cantidad, grupo)
    elif opcion == "2":
        visualizar_inventario()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")