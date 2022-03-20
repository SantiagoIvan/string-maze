# String-maze

- Un laberinto pero hecho con un string, donde el comienzo de cada fila es representado luego de un '\n'
- Los casilleros libres estan representados por puntos ( '.' ) mientras que los casilleros bloqueados estan con una 'W'


## Path finder
- Se comienza en la posicion (0,0) y se debe llegar si es posible hacia la posicion (n-1, n-1)

Algoritmo resuelto utilizando depthfirst recursivo, iterativo y breadthfirst, pero para laberintos de grandes dimensiones, resulta mas performante tener una cola/pila que realizar llamadas recursivas.

## Shortest path
- Se comienza en la posicion (0,0) y se debe retornar la longitud del camino mas corto hacia (n-1,n-1)

Algoritmo resuelto utilizando breadthfirst, ya que este algoritmo busca por niveles, siendo la raiz el nodo inicial. El nivel representa la distancia que hay hasta la raiz, por lo que si el nodo buscado se encuentra en el nivel n, esa distancia sera la minima
