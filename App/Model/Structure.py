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

from App.Model import Comparation

def initDataBase()->dict:
    dataBase = {
        'graph' : graph.newGraph('ADJ_LIST',True,14000,Comparation.compareId),
        'station' : map.newMap(878756,878777,'CHAINING',1.5,Comparation.compareId),
        'target' : map.newMap(7,7,'CHAINING',1.5,Comparation.compareId),
        'trips' : 0
    }
    return dataBase

def newStation():
    station = {
        'name' : None,
        'latitude': None,
        'longitude' : None,
        'tripsIn' : 0,
        'tripsOut' : 0,
        'trips' : 0
    }
    return station

def newWeight():
    weight = {
        'time' : 0,
        'users' : 0
    }
    return weight

def newTargetGraph():
    return graph.newGraph('ADJ_LIST',True,14000,Comparation.compareId)