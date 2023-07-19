def suma_serie():
    numero = int(input("Ingrese el número: "))
    terminos = int(input("Ingrese el número de términos: "))
    
    resultado = 0
    multiplicador = 1
    numero_repetido = 0

    for i in range(terminos):
        numero_repetido = numero_repetido * 10 + numero
        resultado += numero_repetido
        multiplicador += 1

    return resultado

# Ejemplo de uso
print(suma_serie())