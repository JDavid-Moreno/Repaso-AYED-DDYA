# Análisis de complejidad y notación Big O

El análisis de complejidad busca medir cómo crece el costo de un algoritmo al aumentar el tamaño de la entrada, denotado como `n`. Este costo se mide generalmente en tiempo de ejecución o memoria utilizada. No nos interesa conocer la duración exacta en segundos, ya que depende del hardware disponible, sino entender cómo escala el algoritmo conforme el problema crece en magnitud.

Por ejemplo, si duplicar el tamaño de los datos implica duplicar también el trabajo, nos referimos a un crecimiento lineal. Si duplicar los datos cuadruplica el trabajo, hablamos de crecimiento cuadrático.

Por esta razón se creó la notación Big O, que nos permite clasificar la complejidad de un algoritmo. Para determinarla, analizamos la estructura del código e identificamos su orden de complejidad.

**NOTA:** Cada categoría de complejidad incluye ejemplos completos con explicaciones detalladas que justifican por qué esos algoritmos pertenecen a dicha categoría. El código y los informes asociados se encuentran en la carpeta `Algoritmos`.

---

## Tipos de complejidades

### Constante $O(1)$

Un algoritmo de complejidad constante realiza siempre la misma cantidad de operaciones, independientemente del tamaño de la entrada. En otras palabras, el tiempo de ejecución no cambia si el arreglo contiene 10 o 10 millones de elementos; siempre se realiza una única operación.

Ejemplo:

```
array = [1, 2, 3, ..., 1000000]
print(array[0])
```

Aunque el arreglo contenga miles o millones de elementos, el tiempo de ejecución será siempre el mismo.

---

### Logarítmica $O(log(n))$

El algoritmo reduce significativamente el tamaño del problema en cada iteración. El ejemplo más común es eliminar la mitad de los elementos restantes, de modo que cada iteración trabaja con una versión mucho más pequeña del problema.

Por eso el número de pasos crece muy lentamente.

Ejemplo:

```
while n > 1:
    n = n // 2
```

---

### Lineal $O(n)$

En un recorrido lineal, cada iteración procesa un elemento más. Es decir, si hay 10 elementos se realizarán 10 iteraciones; si hay 100 elementos, se realizarán 100 iteraciones, y así sucesivamente.

Ejemplo:

```
array = [1, 2, 3]

for num in array:
    print(num)
```

---

**NOTA:** Generalmente, se asume que los ciclos `for` tienen complejidad O(n) y los ciclos `while` tienen complejidad O(log n). Sin embargo, esto no es necesariamente cierto. Por ejemplo, los ciclos `while` pueden ser O(n):

```
n = 10
i = 0
while i < n:
    print(i)
    i += 1
```

Este ciclo se iteran veces, por lo que su complejidad es O(n). Para determinar la complejidad de un ciclo `while`, es necesario revisar cuál es la condición y cuántas veces se ejecuta: n veces, log(n) veces, etc.

Por otro lado, los ciclos `for` en Python prácticamente siempre son O(n), debido a que Python itera sobre una secuencia completa y fija. Las únicas excepciones son aquellas que utilizan una cantidad log(n) de elementos, como:

```
import math
for i in range(int(math.log2(n)) + 1):
    print(2**i)  # 1, 2, 4, 8...
```

---

### $O(n log(n))$

El algoritmo divide repetidamente el problema en partes más pequeñas y, además, en cada nivel de división debe procesar todos los elementos. Un ejemplo muy conocido es `Merge Sort`, ya que cada división genera aproximadamente `log(n)` niveles y en cada nivel se procesan `n` elementos.

---

### Cuadrática $O(n²)$

El algoritmo compara o procesa cada elemento con todos los demás, de modo que cada recorrido externo provoca otro recorrido completo interno.

Ejemplo:

```
array = [1, 2, 3]

for i in array:
    for j in array:
        print(i, j)
```

Aquí se recorre la lista de dos formas anidadas: los 3 elementos se recorren 2 veces cada uno: 3 × 3 = 9, es decir, 3².

---

### Cúbica $O(n³)$

El algoritmo realiza tres recorridos anidados, generando un crecimiento cúbico en el número de operaciones.

Ejemplo:

```
array = [1, 2, 3]

for i in array:
    for j in array:
        for k in array:
            print(i, j, k)
```

---

### Exponencial $O(2^n)$

Cada solución genera múltiples subproblemas nuevos, haciendo que el número de operaciones se duplique repetidamente.

Un ejemplo clásico es el problema de Fibonacci utilizando recursión, el cual se abordará en su propio informe.

---

### Factorial $O(n!)$

Significa que el algoritmo prueba todas las posibles formas de ordenar o acomodar los elementos.

Por ejemplo, si tenemos:

```
array = [1, 2, 3]
```

Las posibles permutaciones serán:

```
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```

Es decir, 3! = 3 × 2 × 1 = 6.

Con una cantidad muy pequeña de elementos esto no es tan grave, pero crece demasiado rápido. Por ejemplo, si realizamos lo mismo con 10 elementos, hay más de 3 millones de posibilidades.

https://github.com/user-attachments/assets/86e07d6c-f8b6-4e54-aebe-06204b05321e

---

## Como calcular la complejidad de un algoritmo

Para calcular la complejidad de un algoritmo, debemos analizar **cada línea de código** y determinar cuánto "trabajo" realiza. Luego, sumamos todas las complejidades y **nos quedamos con el término más grande** (el término dominante).

**Regla fundamental:** En Big O, solo importa el término que crece más rápido.

Por ejemplo:
- O(n² + n) = O(n²) (porque n² crece mucho más que n)
- O(n + 100) = O(n) (porque la constante 100 no importa)
- O(2n + n log n) = O(n log n) (porque n log n crece más que 2n)

Un par de ejemplos para que se vea que sucede:

### Ejemplo 1

```
def suma_numeros(array):
    total = 0                       # O(1)
    for i in range(len(array)):     # O(n) iteraciones
        total += array[i]           # O(1) por iteración
    return total                    # O(1)
```
Todo dentro de un for que sea constante seguirá siendo O(n), ya que todo dentro de un arreglo se multiplica por a complejidad de dicho ciclo, por lo que si solo hay constantes la complejidad se queda en O(n)

Por lo que queda: O(1) + O(n) + O(1) = O(n)

---

### Ejemplo 2

```
def comparar_elementos(array):
    count = 0                        # O(1)
    for i in range(len(array)):      # O(n) iteraciones
        for j in range(len(array)):  # O(n) iteraciones
            if array[i] > array[j]:  # O(1) por iteración
                count += 1           # O(1) por iteración
    return count                     # O(1)
```

Al haber un ciclo dentro de otro estos al momento de multiplicarse da O(n²), en caso de haber otro ciclo anidado seria O(n³) y asi sucesivamente.

Por lo que queda: O(1) + O(n²) + O(1) = O(n²)

---

### Ejemplo 3: 

```
def buscar_y_contar(array, target):
    encontrado = False               # O(1)
    for i in range(len(array)):      # O(n) iteraciones
        if array[i] == target:       # O(1) por iteración
            encontrado = True
            break
    
    if encontrado:                   # O(1)
        count = 0
        for i in range(len(array)):  # O(n) iteraciones
            count += 1               # O(1) por iteración
    
    return encontrado                # O(1)
```
En caso de existir dos ciclos separados o no anidados, o sea en forma de secuencia (uno y después el otro), estos al igual que cualquier análisis de líneas, estos se suman y como O(n) + O(n) = O(2n), y como las constantes se ignoran esto sigue siendo de complejidad O(n)

Por lo que queda: O(1) + O(n) + O(1) + O(n) + O(1) = O(n) + O(n) = O(n)

---

## Análisis de Recursión

La recursión es más compleja de analizar porque implica llamadas múltiples a la misma función. Para calcular la complejidad, debemos entender cuántas veces se llama a la función y cuánto trabajo hace cada llamada.

Ejemplos:

### Ejemplo 1: Factorial - O(n)

```
def factorial(n):
    if n <= 1:                   # O(1) - comparación
        return 1                 # O(1) - retorno
    
    return n * factorial(n - 1)  # O(1) + llamada recursiva
```

Hay `n` llamadas en total (una para cada número de n a 1), y cada una realiza `O(1)` de trabajo.

Por lo que su complejidad sería de n × O(1) = O(n)

---

### Ejemplo 2: Fibonacci Recursivo - O(2ⁿ)

```
def fibonacci(n):
    if n <= 1:                                  # O(1)
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)  # Línea 2: dos llamadas recursivas
```
Cada llamada a su vez realiza dos llamadas, esto hasta 1, lo que hace que el trabajo se multiplique exponencialmente, ya que se realiza la misma función varias veces, por ejemplo si se hace fibo(5), se realiza fibo(3) 2 veces, fibo(2) 3 veces y asi, lo que vuelve muy complejo el algoritmo.

---

## Análisis de Complejidad de los Algoritmos de Ordenamiento

### $O(n²)$ - Complejidad Cuadrática

### Bubble Sort

```
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
```

**¿Por qué es O(n²)?**

Bubble Sort tiene dos bucles anidados que recorren el arreglo:

1. El bucle externo (`for i in range(n)`) itera `n` veces.
2. El bucle interno (`for j in range(0, n-i-1)`) también itera aproximadamente `n` veces en cada iteración del bucle externo, aunque este reduce la cantidad que itera cada vez, no llega a ser un bajón significativo lo que no la hace O(nlog n).

### Insertion Sort

```
def insertion(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i
        while j > 0 and array[j - 1] > key:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key
    return array
```

**¿Por qué es O(n²)?**

Aunque este algoritmo usa un `while` en lugar de un `for` anidado, sigue siendo O(n²):

1. El bucle externo (`for i in range(1, n)`) itera `n-1` veces.
2. El bucle interno (`while j > 0 and array[j - 1] > key`) puede iterar hasta `i` veces en el peor caso.

---

### Selection Sort

```
def selection(array):
    n = len(array)
    for i in range(n):
        minium = i
        for j in range(i+1, n):
            if array[j] < array[minium]:
                minium = j
        if minium != i:
            array[i], array[minium] = array[minium], array[i]
    return array
```

**¿Por qué es O(n²)?**

Selection Sort también tiene dos bucles anidados:

1. El bucle externo (`for i in range(n)`) itera `n` veces.
2. El bucle interno (`for j in range(i+1, n)`) itera `n-i-1` veces en cada iteración del bucle externo.

---

## $O(n log n)$ 

### Merge Sort

```
def merge(array):
    if len(array) == 1:
        return array
    half = len(array) // 2
    left = array[:half]
    right = array[half:]
    sorted_left = merge(left)
    sorted_right = merge(right)
    return merge_sort(sorted_left, sorted_right)

def merge_sort(left, right):
    array_sort = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            array_sort.append(right[0])
            right.pop(0)
        else:
            array_sort.append(left[0])
            left.pop(0)
    while len(left) > 0:
        array_sort.append(left[0])
        left.pop(0)
    while len(right) > 0:
        array_sort.append(right[0])
        right.pop(0)
    return array_sort
```

**¿Por qué es O(n log n)?**

Merge Sort divide el problema de manera recursiva y luego combina los resultados:

1. El arreglo se divide por la mitad repetidamente hasta obtener sub arreglos de un elemento. Esto ocurre `log(n)` veces:

2. En cada nivel, todos los elementos deben compararse y combinarse. Esta operación toma `O(n)` tiempo en total para cada nivel.

---

### Quick Sort

```
def quick_sort(array, low, high):
    if low < high:
        part = partition(array, low, high)
        quick_sort(array, low, part - 1)
        quick_sort(array, part + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
```

**¿Por qué es O(nlog n)?**

Quick Sort también divide recursivamente el problema y procesa elementos en cada división:

1. La función `partition()` selecciona un pivote y divide el arreglo en dos partes: elementos menores o iguales al pivote y elementos mayores. Esta operación procesa todos los `n` elementos una sola vez: `O(n)`.

2. En el caso promedio, el pivote divide el arreglo aproximadamente por la mitad, por lo que vuelve a dividirse `O(log n)` veces.

**NOTA:** QuickSort en su caso promedio y su mejor caso es `O(nlog n)`, pero en caso de que el pivote sea malo, o sea que sea su peor caso este será de complejidad `O(n²)`

---

## Material adicional

[![Notacion Big O](https://img.youtube.com/vi/MyAiCtuhiqQ/0.jpg)](https://www.youtube.com/watch?v=MyAiCtuhiqQ&t=60s)

[![Notacion Big O](https://img.youtube.com/vi/dqFS-CXCEVQ/0.jpg)](https://www.youtube.com/watch?v=dqFS-CXCEVQ)

[![Notacion Big O](https://img.youtube.com/vi/8biQkAh-LpQ/0.jpg)](https://www.youtube.com/watch?v=8biQkAh-LpQ&t=81s)
