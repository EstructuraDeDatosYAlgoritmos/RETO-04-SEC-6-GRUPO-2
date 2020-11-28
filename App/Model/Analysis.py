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

from App.Model import Structure
from App.Utils import Calc

from DISClib.ADT import graph
from DISClib.ADT import map 
from DISClib.ADT import list 
from DISClib.ADT import stack
from DISClib.ADT import queue
from DISClib.ADT import orderedmap
from DISClib.DataStructures import listiterator 
from DISClib.DataStructures import edge 
from DISClib.DataStructures import mapentry
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktraRout 
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

def getStation(dataBase:dict,id:int)->dict:
    station = map.get(dataBase['station'],id)
    station = mapentry.getValue(station)
    return station

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
    mergesort.mergesort(topIn,Comparation.tripsVal)
    mergesort.mergesort(topOut,Comparation.tripsVal)
    mergesort.mergesort(topTrips,Comparation.tripsVal)

    return (topIn,topOut,topTrips)

def topTarget(dataBase:dict, target:int)->list:
    targetGraph = dataBase['target'] 

    targetList = list.newList()

    if map.contains(targetGraph, target):
        targetGraph = map.get(targetGraph, target)
        targetGraph = mapentry.getValue(targetGraph)
        targetList = graph.edges(targetGraph)
        mergesort.mergesort(targetList,Comparation.targetVal)
    
    return targetList

def bikeTracking(dataBase, bikeID, date):
    tracking = Structure.newDate()
    if map.contains(dataBase['tracking'],bikeID):
        bike = map.get(dataBase['tracking'],bikeID)
        bike = mapentry.getValue(bike)
        if map.contains(bike, date):
            tracking = map.get(bike, date)
            tracking = mapentry.getValue(tracking)
    return tracking

def traerEstacion(dataBase, idStation):
    if m.contains(dataBase['name_IDstations'], idStation):
        keyValue = m.get(dataBase['name_IDstations'], idStation)
        return (keyValue['value'])
    return None, None

def rutasCirculares(dataBase, tiempoi, tiempof, estacioni):
   
    ltArcos = gr.edges(dataBase['connections'])
    rutas = 0
    ltrutasCirculares = lt.newList(datastructure='ARRAY_LIST')
    
    for i in range(1, lt.size(ltArcos)+1): 
        estacion  = lt.getElement(ltArcos, i)
        if str(estacioni) == estacion['vertexA']:
            estacionf = estacion['vertexB']
            try:
                existe_ar = gr.getEdge(dataBase['connections'], estacionf, estacioni)
                weightestacionf = arcoExiste['weight']
                duracion = estacion['weight'] + weightestacionf
                if duracion+20 >= tiempoi and duracion+20 <= tiempof:
                    rutas += 1
                    estacioni_nom = traerEstacion(dataBase, estacioni)
                    estacionf_nom = traerEstacion(dataBase, estacionf)
                    lt.addLast(ltrutasCirculares, (estacioni_nom, estacionf_nom, duracion))
            except:
                pass   
    
def nearbyStations(database, longitude, latitude):
    aspir = queue.newQueue()
    queue.enqueue(aspir,orderedmap.ceiling(database['position']['latitude'],latitude))
    queue.enqueue(aspir,orderedmap.ceiling(database['position']['longitude'], longitude))
    queue.enqueue(aspir,orderedmap.floor(database['position']['longitude'], longitude))
    queue.enqueue(aspir,orderedmap.floor(database['position']['latitude'],latitude))

    val = None
    wID = None
    
    while not queue.isEmpty(aspir):
        id = queue.dequeue(aspir)
        id = mapentry.getValue(id)
        element = map.get(database['station'],id)
        element = mapentry.getValue(element)
        dist = abs(Calc.distance(element['latitude'],latitude,element['longitude'],longitude))
        if val is None:
            val = dist
            wID = id
        if dist < val:
            val = dist
            wID = id
    return wID

def nearbyRoute(database,id1,id2):
    search = dijsktraRout.Dijkstra(database['graph'],id1)
    path = dijsktraRout.pathTo(search,id2)
    time = dijsktraRout.distTo(search,id2)
    return (path,time)
    print("\nEl número de rutas circulares es " + str(rutas) + " y estos son los datos: ")

    for i in range(1, lt.size(ltrutasCirculares)+1):
        print("\nNombre de estación inicial: " + str(lt.getElement(ltrutasCirculares, i)[0]))
        print("\nNombre de estación final: " + str(lt.getElement(ltrutasCirculares, i)[1]))
        print("\nDuración estimada: " + str(lt.getElement(ltrutasCirculares, i)[2]) + " minutos")

