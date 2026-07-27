# Estructuras Lineales

---

Antes de abordar las estructuras lineales debemos entender primero que son las estructuras de datos, las estructuras de datos son una forma de organizar y almacenar datos, los cuales pueden ser utilizados de manera eficiente. Gracias a estas, podemos realizar distintas operaciones como buscar, insertar o eliminar elementos, que nos ayudan a manejar los datos que tenemos de manera más sencilla.

Existen dos tipos de estructuras de datos, que son lineales y NO lineales. Las estructuras lineales organizan sus datos de manera secuencial, donde cada elemento tiene un unico predecesor y un unico sucesor. Mientras que las estructuras no lineales organizan la información de forma jerárquica o interconectada, permitiendo que un elemento tenga uno o varios predecesores, y uno o varios sucesores.

---

Los únicos tipos de estructuras no lineales son Árboles y grafos, los cuales se les abordara en su propio repositorio, por ende, ahora solo nos vamos a enfocar en los distintos tipos de estructuras lineales.

Como ya se dijo antes, estas organizan sus elementos de manera secuencial, como puede ser una fila de personas o los vagones de un tren, por lo que son las más sencillas de entender. Se caracterizan por ser faciles de implementar y son las mejores para ordenar elementos.

Entre los distintos tipos de estructuras lineales, los principales tipos son: 

- Arreglos
- Listas enlazadas
- Pilas
- Colas

A continuación, vamos a abordar cada tipo de manera más detallada con ejemplos prácticos.

---

## Arreglos

Es la estructura más conocida y básica de todas, consiste en almacenar elementos del mismo tipo de manera secuencial, asi mismo, a cada elemento se le asigna una posición fija que es su índice, este índice puede variar de $0$ a $n - 1 $ (siendo $n$ la longitud del arreglo), gracias a esto, se puede acceder a cualquier elemento con facilidad si se conoce su índice.

De igual manera esta se crea con un tamaño fijo, por lo que al momento de crearse se debe definir el tamaño, ya que este no cambia dinámicamente, en caso de llenarse y se necesita más espacio, debemos crear un nuevo arreglo más grande y copiar los datos.

Esta estructura es sencilla para buscar elementos, ya que todos al tener un índice predeterminado, es fácil de encontrar dichos elementos.

```
list = [1,2,3,4,5]
print(list[2])       # devuelve el elemento en el indice 2 osea 3 
```

Sin embargo, a la hora de ingresar o eliminar elementos es bastante lenta, ya que al hacerlos tengo que mover los elementos posteriores al elemento hacia atras o adelante, dependiendo el caso.

```
list = [1,2,3,4,5]
list.append(0)  # al hacer esto todos los elementos se mueven
```

Sus ejemplos más conocidos de uso no los vamos a abordar aca, ya que estos se realizaron con anterioridad que son [Búsqueda Binaria](https://github.com/JDavid-Moreno/Dividir-y-conquistar/blob/main/Algoritmos/BinarySearch.py) o los [Algoritmos de ordenamiento de arreglos](https://github.com/JDavid-Moreno/Algoritmos-de-ordenamiento), los cuales rápidamente tratan sobre encontrar el índice de un elemento conociendo el valor de dicho elemento y los algoritmos de ordenamiento, como dice su nombre, consisten en distintas maneras de ordenar un arreglo de elementos enteros.

---

## Pilas

Es una estructura lineal que utiliza el principio LIFO (Last In, First Out), el cual consiste en que el último elemento que ingreso es el primer elemento es sacar o eliminar, por eso su nombre, ya que es como una pila de cosas donde el elemento de más arriba que fue el último en ponerse, es el primero que se quita. Un ejemplo sencillo para imaginar una pila será una lata de pringles, ya que la última papa que se ingresó a la lata, posteriormente será la primera papa que se saque.

A diferencia de una arreglo en donde se puede ingresar un elemento en cualquier posición, en una pila para ingresar elementos, únicamente se puede hacer en un unico punto que es el tope, por lo que todas sus operaciones sé hacer en el tope que son:

- Apilar: Al agregar un nuevo elemento ese elemento se apila y se pone en el tope.
- Desa pilar: Al eliminar el elemento, este se quita de la pila y el elemento anterior se vuelve el nuevo tope.
- Mirar: se puede mirar únicamente el elemento tope de la pila-

```
stack = []
stack.append(10)    # unico elemento, sera el tope
stack.append(20)    # ultimo elemento en entrar, ese es el nuevo tope
stack.pop()         # sale el tope osea el 20, por lo que el 10 es el nuevo tope
stack[-1]           # se ve que elemento es el tope
```

### Cuando se usa

Generalmente, se usa cuando se necesita volver atrás, por ejemplos el atajo de teclado Ctrl + z es en realidad una pila por ejemplo, asi mismo, se utilizan pilas cuando hay estructuras anidadas o si algo que se abre se tiene que cerrar después como pueden ser las claves de HTML.

### Ejemplos 

### Paréntesis balanceados

Este problema es de los más conocidos sobre pilas, consiste en que dado una serie de paréntesis, ya sea (), { } o [ ], verificar que todos los paréntesis que se abran se cierren, si no que también, estén bien cerrados o balanceados, es decir, que no se puede cerrar un paréntesis en medio de otro.

Ejemplos:

`({[]})` Bien balanceado

`([)]` Mal balanceado

Implementación:

```
def balanced_brackets(sequence):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}
    for bracket in sequence:
        if bracket in brackets.values():
            stack.append(bracket)
        elif bracket in brackets:
            if len(stack) == 0:
                return False
            if stack[-1] != brackets[bracket]:
                return False
            stack.pop()
    return len(stack) == 0
```
 
Para abordar este problema, lo más recomendable es usar un diccionario, el cual asociamos a los paréntesis con sus compañeras. Una vez hecho esto, recorremos la secuencia, si encontramos un paréntesis que abre (o sea un "(", "{" o "[") lo guardamos en la pila

Por otro lado, en caso de encontrar uno paréntesis que cierra (o sea un ")", "}"), primero verificamos que la pila no este vacía, ya que si lo está automáticamente está desbalanceado. Posteriormente, verificamos si el tope es igual al compañero del elemento del tope, es decir, si tengo el ")", tengo que revisar que el tope de la pila este su compañero "(".

Si la comparación es verdadera entonces podemos desa pilar ese elemento, y asi sucesivamente hasta finalizar, en donde la pila debe quedar vacía para ser balanceada, de otro modo, esta desbalanceada.

https://github.com/user-attachments/assets/0faa28e1-1ce4-4a25-9bbd-3b9a53566cd8

### Validación HTML / XML

Este ejemplo es un poco más "real" en el sentido que sería más util en la vida real, usa el mismo principio de los paréntesis balanceados, en XML o HTML todas las etiquetas que se abren se deben cerrar, o sea tipo:

```
<html>
    <body>
        <h1>Título</h1> 
    </body>
</html>
```

Sin embargo, en HTML existen etiquetas que nunca se cierran, y para evitar complicaciones el código está enfocado únicamente en archivos XML.

```
import re

def validate_xml(filename):
    stack = []
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    tags = re.findall(r"</?[a-zA-Z0-9]+>", content)
    for tag in tags:
        if tag.startswith("</"):
            name = tag[2:-1]
            if not stack:
                return False
            if stack.pop() != name:
                return False
        else:
            name = tag[1:-1]
            stack.append(name)
    return len(stack) == 0
```

Para este ejemplo se importó `re` (Regular Expressions) para simplificar las búsquedas, sin embargo, se puede hacer de igual manera sin este, el caso es que este busca cadenas dada cierto parámetro, para este caso primero creamos la pila y posteriormente abrimos el archivo en modo lectura ("r"), asi mismo, se lee todo el archivo y se guarda en una variable, es decir:

```
content =
<book>
    <title>Python</title>
    <author>Juan</author>
</book>
```
Posteriormente, se extrae o filtramos las cadenas que empiezan en < y terminen en >, sin importar que haya adentro (es por eso que se ponen que se pone `</?[a-zA-Z0-9]+>`, que significa toda letra del abecedario mayúscula o minúscula y todo número es válido siempre u cuando empiece y termine en <>).

Una vez se realizan las verificaciones, para saber si está bien balanceado, donde se mira si las etiquetas de cierre tienen su compañero en el tope de la pila, para saber si avanza o ya está mal.

---

## Colas

Las colas a diferencia de las pilas usan el principio FIFO (First In, First Out), es decir el primer elemento que entra es el primero que sale, el ejemplo más sencillo es una fila de cualquier tipo, la primera persona que llego es la primera que atienden. 

Es muy parecido a un arreglo, sin embargo, este cuenta con diferencias clave en sus operaciones, ya que solo se puede eliminar el primer elemento que entro y cada que ingresa un elemento este solo se puede añadir al final de la lista.

### Cuando se usa

Las colas se usan habitualmente en varios sistemas como impresoras, donde las hojas se van imprimiendo en orden, atención al cliente, que va desde el primero que llego al último e incluso para eventos en videojuegos.

### Subtipo: Colas de prioridad 

Para este caso, lo más importante no es quien llego primero, sino que elemento tiene una prioridad mayor, el elemento con mayor prioridad será el primero en salir y en caso de que todos los elementos tengan la misma prioridad, entonces se trabajará como si fuera una cola normal.

### Ejemplos

### Cola de prioridad para hospital 

Este es un ejemplo clásico, consite en decir cuál paciente debe ser atendido primero dependiendo su prioridad que en este caso sería que tan grave esta o que tan urgente es que lo atiendan.

Para este caso baso a manejar la prioridad de la siguiente manera:

```
1 -> Emergencia crítica
2 -> Grave
3 -> Normal
4 -> Leve
```

Por lo que mientras más pequeño el número, más rapido se debe atender, por otro lado, en caso de que 2 pacientes tengan la misma prioridad se atenderá al que llego primero, asi mismo, suponemos que la estructura será `(int(Prioridad), String(Nombre))`.

```
def attend_patient(hospital):
    if len(hospital) == 0:
        return None
    priority = 0
    for i in range(1, len(hospital)):
        if hospital[i][0] < hospital[priority][0]:
            priority = i
    return hospital.pop(priority)
```

Aquí lo que hacemos es primero verificar que hay pacientes, en ese caso revisamos la lista de pacientes de modo que comparamos si la prioridad un paciente es mayor a la de los demás, y se retorna el paciente de mayor prioridad (que a la vez se elimina de la lista, ya que es el que se va a atender), en caso se quiera ver el orden de atencion de los clientes se puede realizar de varias maneras, en este caso, se crea otra función:

```
def service_order(hospital):
    order = []
    while hospital:
        order.append(attend_patient(hospital))
    return order
```

**NOTA:** Hay más ejemplos tanto para pilas como colas relacionadas con algoritmos de búsqueda (A*, DFS, BFS, etc), el caso es que varios de estos se desarrollan sobre estructuras no lineales como Árboles binarios o grafos, por lo que dichos ejemplos se abordaran en los respectivos repos de esos temas.

---

## Listas Enlazadas

Es una estructura lineal donde a diferencia de las estructuras anteriores que guarda los elementos uno al lado del otro, si no que los elementos almacenados en la memoria están enlazados entre sí a través de apuntadores, cada elemento tiene un apuntador que señala al siguiente elemento en la lista, estos elementos los llamamos **nodos**.

De esta manera, la listas enlazadas tienen ventajas sobre los arreglos normales, por ejemplo, es muy sencillo agregar nuevos elementos, ya que estas crecen dinámicamente, es decir, unicameral toca crear el elemento en la memoria y el respectivo apuntador hacia el elemento, a diferencia de un arreglo normal, que este al tener tamaño fijo, debe crear otro arreglo más grande, clonar los elementos e insertar el nuevo elemento.

De igual manera, para eliminar elementos es igual muy sencillo, únicamente se debe cambiar el apuntador del elemento anterior al que queremos eliminar, y redireccionarlo al elemento siguiente, de esta manera al no haber nada que lo apunte, elemento técnicamente se eliminó de la lista.

Sin embargo, asi como tiene ventajas, tiene desventajas, por ejemplo, al no contar con índices como los arreglos normales, para ver el elemento en una posición x, debemos recorrer toda la lista para ver el valor de dicho elemento, a diferencia de un arreglo convencional, que con solo saber su índice podemos conocer su valor sin recorrer la lista.

### Tipos

Existen 3 tipos de listas enlazadas:

1. **Lista enlazada**: la base y la que ya se explicó, cada nodo apunta al siguiente.
![ListaEnlazada.jpeg](Recursos/Listas%20Enlazadas/ListaEnlazada.jpeg)
2. **Lista doblemente enlazada**: Cada nodo apunta al siguiente elemento y al anterior elemento, por lo que permite recorrer en ambas direcciones.
![Lista-DoblementeEnlazada.jpeg](Recursos/Listas%20Enlazadas/Lista-DoblementeEnlazada.jpeg)
3. **Lista circular**: es igual a una lista enlazada con la diferencia que el último elemento apunta al primer elemento, lo que lo hace cíclico al recorrer la lista
![ListaCircular.jpeg](Recursos/Listas%20Enlazadas/ListaCircular.jpeg)

### Como se crea

A diferencia de las listas convencionales, las listas enlazadas se crean de manera distinta, ya que debemos definir la estructura de los nodos, y la mejor forma de hacerlo es con una clase. Ya que cada nodo debe guardar 2 cosas: Un valor o dato y un puntero al siguiente nodo.

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```
Esto nos permite guardar el valor y apuntar al siguiente (que todavía no apunta a nadie). Ahora para la lista enlazada necesitamos otra clase la cual guardaremos su funcionamiento y operaciones, por lo que vamos paso por paso empezando por su creación y "constructor".

```
class LinkedList:
    def __init__(self):
        self.head = None
```
En este caso, `self.head` representa al primer nodo de la lista, si este es **None**, significa que la lista está vacía. Por lo que con el molde, podemos crear sus operaciones.

**AGREGAR**

```
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = node
```
Para agregar un nuevo elemento, primero creamos un nuevo nodo con el valor dado, y verificamos si la lista está vacía, en ese caso, ese elemento se vuelve la cabeza. Por otro lado, si no, recorre la lista hasta llegar al último nodo y conecta ese nodo al nuevo nodo.

**BUSCAR**

```
    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next
        return False
```
Recorre nodo por nodo comparando el valor de ese nodo con el valor a buscar, si lo encuentra devuelve `True` de que si está el elemento en la lista, y en caso de que no lo encuentre devuelve `False`.

**ELIMINAR**

```
    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
```
Antes de recorrer la lista verificamos si el elemento que queremos eliminar está en la cabeza, en ese caso, únicamente movemos él `self.head` al siguiente nodo. Por otro lado, si no es la cabeza, recorremos la lista buscando el nodo anterior al que se quiere eliminar, ahi lo que hacemos es redireccionar el apuntador al elemento siguiente al que queremos eliminar, o sea el siguiente del siguiente.

Finalmente, si queremos mostrar o imprimir la lista podemos crear otro método:

```
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")
```
Para este únicamente se recorre la lista imprimiendo el valor de cada nodo hasta llegar al final o sea hasta `None`.

### Operaciones adicionales 

Se pueden crear operaciones adicionales para que sea parecida a como funcionan los arreglos.

**AGREGAR UN VALOR EN CUALQUIER POSICIÓN**

```
    def append_position(self, data, position):
        node = Node(data)
        if position == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head
        cont = 0
        while cont < position - 1 and current:
            current = current.next
            cont += 1
        if current is None:
            return

        node.next = current.next
        current.next = node
``` 

Aquí lo que hacemos es que además de pedir el valor, pedimos en que posición se desea poner ese valor o nodo, para este caso la posición será como el índice en los arreglos, de igual manera, las posiciones se manejaran igual que los índices, es decir, desde $0$ hasta $n - 1$.

**OBTENER TAMAÑO**

``` 
    def size(self):
        cont = 0
        current = self.head

        while current:
            cont += 1
            current = current.next
        return cont
```
En este caso, utilizamos un contador donde si podemos avanzar a un siguiente nodo vamos sumando de a 1, asi hasta que el siguiente nodo sea `None`, es decir, hasta ahi llega la lista.

**OBTENER ELEMENTO POR POSICIÓN**

``` 
    def get(self, position):
        cont = 0
        current = self.head

        while current:
            if cont == position:
                return current.data
            current = current.next
            cont += 1

        return None
```

Para este, de igual manera necesitamos un contador para ir contando en que posición vamos, una vez en dicha posición únicamente extraemos el valor del nodo. 

**OBTENER EL VALOR DEL ÚLTIMO ELEMENTO**

```
    def last(self):
        if self.head is None:
            return None
        current = self.head

        while current.next:
            current = current.next
        return current.data
```

Muy parecido al anterior, sin embargo, como queremos obtener el último elemento, no necesitamos de un contador para saber en qué posición vamos.

**ACTUALIZAR UN VALOR**

```
    def update(self, old, new):
        current = self.head

        while current:
            if current.data == old:
                current.data = new
                return
            current = current.next
```

Este se puede realizar de dos maneras, dando el valor anterior o dando la posición del nodo al que le queremos dar el nuevo valor, en este caso se hizo dando el valor anterior, donde se va recorriendo la lista hasta encontrar dicho valor y sustituirlo.

**CONTAR CUANTAS VECES APARECE UN VALOR**

```
    def count(self, value):
        total = 0
        current = self.head

        while current:
            if current.data == value:
                total += 1
            current = current.next
        return total
```

Para este, vamos recorriendo la lista y cada vez que encontremos el valor vamos sumando uno en un contador, asi sucesivamente hasta haber recorrido todo el arreglo.


**ENCONTRAR EL VALOR MAXIMO Y MINIMO**

```
    def max(self):
        maximum = 0
        current = self.head

        while current:
            if maximum < current.data:
                maximum = current.data
            current = current.next
        return maximum

    def min(self):
        current = self.head
        minimum = current.data

        while current:
            if minimum > current.data:
                minimum = current.data
            current = current.next
        return minimum
```

Ambos funcionan de la misma manera, definimos su variable y vamos recorriendo la lista, comparando cada valor de los nodos para encontrar si es más pequeño o grande dependiendo de que necesitemos.

**LIMPIAR LA LISTA**

```
    def clear(self):
        self.head = None
```
Este es muy importante y a la vez sumamente facil, unicamente debemos volver la cabeza nula, de esta manera se eliminan todos los nodos siguientes.

### Invertir una lista enlazada

Este es un ejercicio clásico, como dice su nombre, consiste en invertir una lista enlazada, a diferencia de un arreglo normal que se hace con mucha facilidad, aquí al no poseer índices, debemos invertir los apuntadores.

```
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
```

Aquí necesitaremos de 3 variables para ir guardando los cambios, primero guardamos cuál es el siguiente nodo normal, es decir, el que sigue en el recorrido antes de invertir, después ese siguiente nodo lo volvemos el anterior y el anterior se volverá el nodo actual. Asi podemos ir invirtiendo la lista sin perder ningún valor.

### Ordenar una lista enlazada

Al igual que un arreglo normal, una lista enlazada se puede ordenar usando los mismos algoritmos de ordenamiento como: merge sort, bubble sort, selection sort, etc. Obviamente adaptado para listas ordenadas; sin embargo, se matiene la misma idea, por lo que para no repetir lo mismo que se dijo en el repo sobre [Algoritmos de ordenamiento](https://github.com/JDavid-Moreno/Algoritmos-de-ordenamiento), unicamente haremos Bubble Sort que es de los más sencillos de realizar a pesar de no ser el más eficiente, por otro lado, el mejor algoritmo para listas enlazadas es **Merge Sort**.

```
    def sort(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next
```

Para resumir, bubble sort consiste en ir comparando elementos de vecinos y llevando el más grande a la derecha, asi sucesivamente hasta llevar al elemento más grande a la última posicion, y asi sucesivamente con todos los elementos hasta ordenar la lista, para una explicación más detallada se puede encontrar [Aquí](https://github.com/JDavid-Moreno/Algoritmos-de-ordenamiento).


---

### Lista doblemente enlazada

Esta cambia un poco como funciona las listas enlazadas, su principal cambio es que ahora como se apunta tanto al elemento previo como al elemento siguiente, se necesitan ahora de dos apuntadores.

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

Ahora creamos el apuntador `prev` para guardar el anterior, y con la base de la lista que queda de igual manera, podemos crear las operaciones de las listas.

**Agregar**

```
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = node
        node.prev = current
```

Este se hace igual al de una lista enlazada normal, con el cambio de que al final guardamos el nodo anterior para que el apuntador nuevo sepa cuál es su predecesor.

**Mostrar la lista en ambas direcciones**

```
    def display_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data)
            current = current.prev
        print(None)
```

Para la función `display_forward` es exactamente igual a la que se usó previamente en la lista enlazada normal, por otro lado, `display_backward` lo que hace es que primero recorre la lista, y una vez llega al final, comienza a reotrnar la lista "al reves", mientras va avanzando con los apuntadores `prev`.

Para las demás funciones no cambia en nada sustancial.

---

### Lista Circular

Esta es muy parecida, ya que en el papel únicamente al último elemento se le debe agregar un apuntador hacia el primer elemento. Por lo que, la clase `Node` se queda tal como esta, sin embargo, para la clase `CircularLinkedList` cambian algunas funciones respecto a sus operaciones básicas.

**Agregar**

```
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        current = self.head

        while current.next != self.head:
            current = current.next
        current.next = node
        node.next = self.head
```

Para este caso, cuando agregamos el primer elemento, hacemos que este se apunte a sí mismo. Por otro lado, cuando agregamos otro nodo, este se hará igual que en una lista enlazada normal, con la diferencia de que el ciclo pare si llega a la cabeza nuevamente o si no estara en un loop infinito, asi como al definir el nuevo nodo, actualizamos el apuntador de la cabeza para que el último elemento sea el que lo apunte.

**Buscar**

```
    def search(self, value):
        current = self.head

        while True:
            if current.data == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False
```

Este también cambia su ciclo, ya que como nunca tendremos un nodo que apunte a nada, o sea `None`, el loop se vuelve infinito. Por lo que debemos modificarlo de tal manera que ahora verifique si volvimos a la cabeza de la lista nuevamente, en ese caso acabamos el lopp para decir que no lo encontramos.

Asi mismo, usamos esta misma idea para la operación de **Mostrar**:

```
    def display(self):
        current = self.head
        while True:
            print(current.data)
            current = cursrent.next
            if current == self.head:
                break
        print("head")
```

---

## Material adicional

[![Estructuras lineales](https://img.youtube.com/vi/Df-sgxGzyTg/0.jpg)](https://www.youtube.com/watch?v=Df-sgxGzyTg&t=2s)

[![Arreglos](https://img.youtube.com/vi/oMoaJ_kX63A/0.jpg)](https://www.youtube.com/watch?v=oMoaJ_kX63A&t=18s)

[![Pilas y colas](https://img.youtube.com/vi/x8pLMgtRXY0/0.jpg)](https://www.youtube.com/watch?v=x8pLMgtRXY0)

[![Listas enlazadas](https://img.youtube.com/vi/qk67wS7WYxo/0.jpg)](https://www.youtube.com/watch?v=qk67wS7WYxo&list=PLfBtpqIBIz7rftekZzTw1DF8gIWetK8pH&index=3)

### Más material que aborda otras estructuras no lineales que posteriormente se van a abordar.

[![Estructuras de datos](https://img.youtube.com/vi/cwRQHcaef5c/0.jpg)](https://www.youtube.com/watch?v=cwRQHcaef5c)

[![Estructuras de datos](https://img.youtube.com/vi/9ifwAPFxpu0/0.jpg)](https://www.youtube.com/watch?v=9ifwAPFxpu0)


