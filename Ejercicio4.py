# Definir las listas para almacenar los productos y existencias por grupo
dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]
cleaning_products = []
cleaning_stock = []
grain_products = []
grain_stock = []

def agregar_producto():
    # Solicitar los datos del producto al usuario
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    grupo = input("Ingrese el grupo al que pertenece el producto (dairy, cleaning, grain): ")

    # Verificar el grupo y agregar o actualizar las existencias del producto
    if grupo == "dairy":
        if nombre in dairy_products:
            indice = dairy_products.index(nombre)
            dairy_stock[indice] += cantidad
        else:
            dairy_products.append(nombre)
            dairy_stock.append(cantidad)
    elif grupo == "cleaning":
        if nombre in cleaning_products:
            indice = cleaning_products.index(nombre)
            cleaning_stock[indice] += cantidad
        else:
            cleaning_products.append(nombre)
            cleaning_stock.append(cantidad)
    elif grupo == "grain":
        if nombre in grain_products:
            indice = grain_products.index(nombre)
            grain_stock[indice] += cantidad
        else:
            grain_products.append(nombre)
            grain_stock.append(cantidad)
    else:
        print("Grupo inválido. Por favor, ingrese un grupo válido.")

def visualizar_inventario():
    print("Inventario:")
    print("Dairy:")
    for producto in dairy_products:
        indice = dairy_products.index(producto)
        print(f"{producto} - Existencias: {dairy_stock[indice]}")
    print("Cleaning:")
    for producto in cleaning_products:
        indice = cleaning_products.index(producto)
        print(f"{producto} - Existencias: {cleaning_stock[indice]}")
    print("Grain:")
    for producto in grain_products:
        indice = grain_products.index(producto)
        print(f"{producto} - Existencias: {grain_stock[indice]}")

# Programa principal
while True:
    print("==== Menú ====")
    print("1. Agregar producto")
    print("2. Visualizar inventario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        visualizar_inventario()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
