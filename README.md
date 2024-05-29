### Investigación Teórica

#### Búsqueda Lineal

La búsqueda lineal, también conocida como búsqueda secuencial, es uno de los algoritmos de búsqueda más simples. Consiste en recorrer cada elemento de una lista o arreglo hasta encontrar el elemento objetivo o llegar al final de la lista sin haberlo encontrado.

- **Funcionamiento**: En cada iteración, se compara el elemento objetivo con el elemento actual de la lista. Si coinciden, se retorna el índice del elemento. Si no, se continúa con el siguiente elemento.
- **Requisitos**: No requiere que la lista esté ordenada.
- **Complejidad**: La complejidad temporal en el peor de los casos es O(n), donde n es el número de elementos en la lista.

#### Búsqueda Binaria

La búsqueda binaria es un algoritmo mucho más eficiente que la búsqueda lineal, pero requiere que la lista esté ordenada previamente. El algoritmo divide repetidamente el rango de búsqueda a la mitad, reduciendo significativamente el número de comparaciones necesarias para encontrar el elemento objetivo.

- **Funcionamiento**: Comienza comparando el elemento objetivo con el elemento del medio de la lista. Si el objetivo es igual al elemento medio, se ha encontrado el elemento. Si el objetivo es menor que el elemento medio, la búsqueda se restringe a la mitad inferior de la lista. Si es mayor, se restringe a la mitad superior. Este proceso se repite hasta encontrar el elemento o hasta que el rango de búsqueda se reduce a cero.
- **Requisitos**: La lista debe estar ordenada.
- **Complejidad**: La complejidad temporal en el peor de los casos es O(log n).

### Análisis de Ejemplos

#### Implementación en Python

**Búsqueda Lineal:**
```python
def busqueda_lineal(lista, objetivo):
    for indice, elemento en enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

# Ejemplo de uso:
lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_lineal(lista, objetivo)
print(f'Índice del objetivo en la lista: {resultado}')
```

**Búsqueda Binaria:**
```python
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

# Ejemplo de uso:
lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_binaria(lista, objetivo)
print(f'Índice del objetivo en la lista: {resultado}')
```

### Prueba y Evaluación

Probamos ambos algoritmos con diferentes conjuntos de datos y valores:

**Pruebas:**
```python
# Pruebas para búsqueda lineal
print(busqueda_lineal([10, 20, 30, 40, 50], 30))  # Salida: 2
print(busqueda_lineal([10, 20, 30, 40, 50], 60))  # Salida: -1

# Pruebas para búsqueda binaria
print(busqueda_binaria([10, 20, 30, 40, 50], 30))  # Salida: 2
print(busqueda_binaria([10, 20, 30, 40, 50], 60))  # Salida: -1
```

### Comparación de Eficiencia

Para comparar la eficiencia, medimos el tiempo de ejecución de ambos algoritmos con listas de diferente tamaño utilizando el módulo `time` en Python.

```python
import time

# Generar una lista grande
lista_grande = list(range(1000000))
objetivo = 999999

# Medir tiempo de búsqueda lineal
inicio = time.time()
busqueda_lineal(lista_grande, objetivo)
fin = time.time()
print(f'Tiempo de búsqueda lineal: {fin - inicio} segundos')

# Medir tiempo de búsqueda binaria
inicio = time.time()
busqueda_binaria(lista_grande, objetivo)
fin = time.time()
print(f'Tiempo de búsqueda binaria: {fin - inicio} segundos')
```

### Resultados

- **Búsqueda Lineal**: Para una lista grande, la búsqueda lineal toma un tiempo proporcional al tamaño de la lista.
- **Búsqueda Binaria**: La búsqueda binaria es significativamente más rápida para listas grandes debido a su complejidad logarítmica.

### Conclusión

La búsqueda binaria es mucho más eficiente que la búsqueda lineal para listas grandes, siempre y cuando la lista esté ordenada. La búsqueda lineal, aunque menos eficiente, es más simple y no requiere una lista ordenada.

### Código en Repositorio

Para subir el código a un repositorio, sigue estos pasos:

1. **Crear un nuevo repositorio en GitHub.**
2. **Clonar el repositorio a tu máquina local:**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```
3. **Agregar los archivos de código al repositorio:**
   ```bash
   cd tu_repositorio
   git add .
   git commit -m "Agregar implementaciones de búsqueda lineal y binaria"
   git push origin main
   ```
4. **Proporcionar el enlace del repositorio en el classroom.**

Con esto, habrás completado la investigación y la implementación de los algoritmos de búsqueda lineal y binaria en Python.