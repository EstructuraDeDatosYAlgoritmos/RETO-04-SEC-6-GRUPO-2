"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
"""

from DISClib.ADT import graph
from DISClib.ADT import map 
from DISClib.ADT import list 
from DISClib.ADT import stack
from DISClib.DataStructures import listiterator 
from DISClib.DataStructures import edge 
from DISClib.DataStructures import mapentry
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra 
from DISClib.Algorithms.Graphs import dfsprueba 
from DISClib.Algorithms.Sorting import mergesort

from App.Model import Comparation

def numClusters(dataBase):
    clusters = scc.KosarajuSCC(dataBase['graph'])
    return scc.connectedComponents(clusters)

def sameCluster(dataBase, station1, station2):
    clusters = scc.KosarajuSCC(dataBase['graph'])
    return scc.stronglyConnected(clusters, station1, station2)

def numVertices(dataBase):
    return graph.numVertices(dataBase['graph'])

def numEdges(dataBase):
    return graph.numEdges(dataBase['graph'])

def topViajes(dataBase)->tuple:
    stations = dataBase['station']
    topIn = list.newList()
    topOut = list.newList()
    topTrips = list.newList()
    keys = map.keySet(stations)
    keys = listiterator.newIterator(keys)
    while listiterator.hasNext(keys):
        key =listiterator.next(keys)
        station = map.get(stations,key)
        station = mapentry.getValue(station)
        list.addFirst(topIn,{'station':station['name'], 'value':station['tripsIn']})
        list.addFirst(topOut,{'station':station['name'], 'value':station['tripsOut']})
        list.addFirst(topTrips,{'station':station['name'], 'value':station['trips']})
    mergesort.mergesort(topIn,Comparation.upVal)
    mergesort.mergesort(topOut,Comparation.upVal)
    mergesort.mergesort(topTrips,Comparation.upVal)

    return (topIn,topOut,topTrips)

def rutasCirculares(database,tiempoi, tiempof, station1)-> tuple:
    lista = []
    numeroRutas= 0
    listaDic = []
    search = dfsprueba.DepthFirstSearch(database, station1)
    while dfsprueba.dfsVertex(search,database, station1)[1] == True:
        estaciones = dfsprueba.pathTo(search, station1)
        for  a in range(1, stack.size(estaciones)):
            lista.append(stack.getElement(estaciones, a))
        
        for i in range(len(lista)):
            for b in range(i+1, len(lista)):
                arcos = graph.getEdge(lista[b], lista[a])
                peso = edge.weight(arcos)
                tiempo = peso['time']
                tiempo_arcos+= int(tiempo)

        tiempo_total = tiempo_arcos +(20 * stack.size(estaciones))
        if tiempo_total>tiempoi and tiempo_total<tiempof:
            numeroRutas+=1
            dic = {'estacion inicial': lista[-1], 'estacion final': lista[0], 'Tiempo': tiempo_total}
            listaDic.append(dic)
    
    respuesta = (numeroRutas, listaDic)
    return respuesta
    




