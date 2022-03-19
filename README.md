# String-maze

- Un laberinto pero hecho con un string, donde el comienzo de cada fila es representado luego de un '\n'
- Se comienza en la posicion (0,0) y se debe llegar si es posible hacia la posicion (n-1, n-1)
- Los casilleros libres estan representados por puntos ( '.' ) mientras que los casilleros bloqueados estan con una 'W'

Algoritmo resuelto utilizando depthfirst recursivo, iterativo y breadthfirst, pero para laberintos de grandes dimensiones, resulta mas performante tener una cola/pila que realizar llamadas recursivas.
