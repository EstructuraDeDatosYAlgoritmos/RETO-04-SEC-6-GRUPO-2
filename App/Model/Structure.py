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
from DISClib.DataStructures import listiterator 
from DISClib.DataStructures import mapentry
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra 


def initDataBase()->dict:
    dataBase = {
        'graph' : graph.newGraph('ADJ_LIST',True,14000,compareId),
        'station' : map.newMap(878756,878777,'CHAINING',1.5,compareId),
        'trips' : 0
    }
    return dataBase


def newStation():
    station = {
        'name' : None,
        'latitude': None,
        'longitude' : None,
        'users' : 0
    }
    return station

def newWeight():
    weight = {
        'time' : 0,
        'users' : 0
    }
    return weight

def compareId(id1, id2):
    id2 = mapentry.getKey(id2)
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1
