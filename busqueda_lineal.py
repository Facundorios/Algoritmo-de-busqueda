def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

# Ejemplo de uso:
lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_lineal(lista, objetivo)
print(f'Índice del objetivo en la lista: {resultado}')