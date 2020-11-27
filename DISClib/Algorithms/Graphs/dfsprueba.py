import config
from DISClib.DataStructures import adjlist as g
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import map as map
from DISClib.ADT import stack as stk
from DISClib.Utils import error as error
from DISClib.ADT import graph as gr
from DISClib.DataStructures import edge
assert config


def DepthFirstSearch(graph, source):
    
    """
    Genera un recorrido DFS sobre el grafo graph
    Args:
        graph:  El grafo a recorrer
        source: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    try:
        search = {
                  'source': source,
                  'visited': None,
                  }

        search['visited'] = map.newMap(numelements=g.numVertices(graph),
                                       maptype='PROBING',
                                       comparefunction=graph['comparefunction']
                                       )

        map.put(search['visited'], source, {'marked': True, 'edgeTo': None, 'peso': None})
        dfsVertex(search, graph, source)
        return search
    except Exception as exp:
        error.reraise(exp, 'dfs:DFS')


def dfsVertex(search, graph, vertex):
    """
    Funcion auxiliar para calcular un recorrido DFS
    Args:
        search: Estructura para almacenar el recorrido
        vertex: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    try:
        result = False
        adjlst = g.adjacents(graph, vertex)
        adjslstiter = it.newIterator(adjlst)
        while (it.hasNext(adjslstiter)):
            w = it.next(adjslstiter)
            if w == vertex:
                result = True
            visited = map.get(search['visited'], w)
            if visited is None:
                
                map.put(search['visited'],
                        w, {'marked': True, 'edgeTo': vertex, 'peso': edge.weight(gr.getEdge(graph, vertex, w)) })
                dfsVertex(search, graph, w)
        return (search, result)
    except Exception as exp:
        error.reraise(exp, 'dfs:dfsVertex')


def hasPathTo(search, vertex):
    """
    Indica si existe un camino entre el vertice source
    y el vertice vertex
    Args:
        search: Estructura de recorrido DFS
        vertex: Vertice destino
    Returns:
        True si existe un camino entre source y vertex
    Raises:
        Exception
    """
    try:
        element = map.get(search['visited'], vertex)
        if element and element['value']['marked'] is True:
            return True
        return False
    except Exception as exp:
        error.reraise(exp, 'dfs:hasPathto')


def pathTo(search, vertex):
    """
    Retorna el camino entre el vertices source y el
    vertice vertex
    Args:
        search: La estructura con el recorrido
        vertex: Vertice de destingo
    Returns:
        Una pila con el camino entre el vertices source y el
        vertice vertex
    Raises:
        Exception
    """
    try:
        if hasPathTo(search, vertex) is False:
            return None
        path = stk.newStack()
        while vertex != search['source']:
            stk.push(path, vertex)
            vertex = map.get(search['visited'], vertex)['value']['edgeTo']
        stk.push(path, search['source'])
        return path
    except Exception as exp:
        error.reraise(exp, 'dfs:pathto')
