def filtrar_numeros():
    lista = input("Ingrese los números separados por espacios: ").split()
    salida = []
    for numero in lista:
        numero = int(numero)
        if numero % 5 == 0:
            if numero > 1000:
                return salida
            elif numero <= 600:
                salida.append(numero)
    return salida

# Ejemplo de uso
salida = filtrar_numeros()
print(salida)
