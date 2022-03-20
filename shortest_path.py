# aplicando breadthfirst, como busco por niveles ( a distancia n siendo n el nivel), voy a encontrar al mas corto de 1
# si aplicase depthfirst, voy a estar tomando una direccion y yendo hasta el fondo, si esa direccion es erronea, va por otra direccion
# asi hasta encontrar al buscado, pero no va a ser la distancia mas corta ni en pedo
# solo de suerte va a ser la distancia mas corta

def get_dimension(maze):
    count = 0
    found = False
    for char in maze:
        count +=1
        if char == '\n':
            found = True
            break
    # si el laberinto tiene solo 1 fila, no va a tener \n
    dimension = count-1 if found else count # para tener la dimension del laberinto en si 
    return dimension

def get_elem(maze, dimension, src):
    row_is_correct = src[0]>=0 and src[0]<dimension
    col_is_correct = src[1]>=0 and src[1]<dimension
    if (not row_is_correct) or (not col_is_correct): return
    
    start_index = src[0] * (dimension + 1) #ya que cada fila tiene un \n
    return maze[start_index + src[1]] if start_index + src[1] < len(maze) else None

def breadthfirst(maze, src):
    visited = set([])
    queue = []
    dimension = get_dimension(maze)
    results = []
    
    trio = (src[0], src[1], 0) # 0 is distance from start
    queue.append(trio)
    
    while len(queue)>0:
        (row, col, dist) = queue.pop(0)

        if (row, col) in visited: continue
        elem = get_elem(maze, dimension, (row, col))
        if (not elem) or (elem == 'W'): continue
        
        if (row, col) == (dimension-1, dimension-1):
            results.append(dist)
            continue
        
        visited.add((row, col))
        queue.append((row + 1, col, dist + 1))
        queue.append((row, col + 1, dist + 1))
        queue.append((row - 1, col, dist + 1))
        queue.append((row, col - 1, dist + 1))
    return False if len(results) == 0 else min(results)

def path_finder(maze):
    return breadthfirst(maze, (0,0))
