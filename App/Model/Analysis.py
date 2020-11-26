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
from DISClib.ADT import graph
from DISClib.ADT import map 
from DISClib.ADT import list 
from DISClib.DataStructures import listiterator 
from DISClib.DataStructures import mapentry
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra 
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