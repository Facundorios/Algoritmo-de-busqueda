def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return -1

#Ejemplo de uso
lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_binaria(lista, objetivo)
print(f'Índice del objetivo en la lista: {resultado}')

print(busqueda_binaria([10, 20, 30, 40, 50], 30))  # Salida: 2
print(busqueda_binaria([10, 20, 30, 40, 50], 60))  # Salida: -1
