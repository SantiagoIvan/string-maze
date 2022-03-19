# Empiezo del 0 0 y me puedo mover en esas direcciones, tengo que llegar a la salida
# seria como el juego del laberinto
# siempre son matrices cuadradas

# la diferencia es que mi laberinto es un string

def get_dimension(maze):
    # si el laberinto tu tuviera solo una fila, no tiene el \n al final, por eso hago el flag 'found'
    i = 0
    found = False
    for char in maze:
        i += 1
        if char == '\n': 
            found = True
            break
    maze_width = i-1 if found else i # cantidad de elementos por fila sin contar al  \n
    
    return maze_width# matriz cuadrada
    
def get_element(maze, row, col, dimension):
    row_is_correct = row>=0 and row < dimension
    col_is_correct = col>=0 and col < dimension
    if (not row_is_correct) or (not col_is_correct): return
    
    start_position = (dimension+1) * row 
    # me muevo segun la cantidad que tenga cada fila para saber la posicion 
    # inicial, tengo que contar el \n, por eso el +1
    
    return maze[start_position + col] if start_position + col < len(maze) else None


def depthfirst_recursive(maze, src, visited, dimension):
    if src in visited: return False
    if src == (dimension-1, dimension - 1):
        return True

    (row, column) = src
    elem = get_element(maze, row, column, dimension)
    if (not elem) or (elem == 'W'): return False
    
    visited.add(src)
    
    if depthfirst_recursive(maze, (row-1, column), visited, dimension): return True
    if depthfirst_recursive(maze, (row, column-1), visited, dimension): return True
    if depthfirst_recursive(maze, (row+1, column), visited, dimension): return True
    if depthfirst_recursive(maze, (row, column+1), visited, dimension): return True
    return False


def breadthfirst(maze, src):
    queue = []
    visited = set([])
    dimension = get_dimension(maze)
    
    queue.append(src)
    
    while len(queue)>0:
        current = queue.pop(0)
        
        if current in visited: continue
        elem = get_element(maze, current[0], current[1], dimension)
        if (not elem) or (elem == 'W'): continue
        visited.add(current)
        
        if current == (dimension-1, dimension - 1):
            return True
        
        queue.append((current[0] + 1, current[1]))
        queue.append((current[0], current[1]+1))
        queue.append((current[0] - 1, current[1]))
        queue.append((current[0], current[1]-1))
        
    return False

def depthfirst_iterative(maze, src):
    dimension = get_dimension(maze)
    stack = []
    visited = set([])
    
    stack.append(src)
    
    while len(stack)>0:
        current = stack.pop()
        
        if current == (dimension-1, dimension-1): return True
        if current in visited: continue
        elem = get_element(maze, current[0], current[1], dimension)
        if (not elem) or (elem == 'W'): continue
        
        visited.add(current)
        stack.append((current[0] + 1, current[1]))
        stack.append((current[0], current[1]+1))
        stack.append((current[0] - 1, current[1]))
        stack.append((current[0], current[1]-1))
    return False


def path_finder(maze):
    dimension = get_dimension(maze)
    print("Dimensiones", dimension, dimension, len(maze))
    
    #return depthfirst_recursive(maze, (0,0), set([]), dimension)
    #return breadthfirst(maze, (0,0))
    return depthfirst_iterative(maze, (0,0))
