def agrupar_elementos(lista):
    diccionario = {}
    for elemento in lista:
        if elemento in diccionario:
            diccionario[elemento].append(elemento)
        else:
            diccionario[elemento] = [elemento]
    matriz_salida = list(diccionario.values())
    return matriz_salida

def obtener_lista_por_consola():
    entrada = input("Ingrese los elementos separados por comas: ")
    lista = [int(x) for x in entrada.split(",")]
    return lista

# Obtener la lista de elementos por consola
lista_de_entrada = obtener_lista_por_consola()

# Obtener la matriz de salida utilizando la función agrupar_elementos
matriz_de_salida = agrupar_elementos(lista_de_entrada)

# Imprimir el resultado
print(matriz_de_salida)
