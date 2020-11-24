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
from DISClib.DataStructures import mapentry  
from DISClib.DataStructures import edge 

from App.Model import Structure

"""
"tripduration",
"starttime",
"stoptime",
"start station id",
"start station name",
"start station latitude",
"start station longitude",
"end station id",
"end station name",
"end station latitude",
"end station longitude",
"bikeid",
"usertype",
"birth year",
"gender"
"""

def addTrip(trip:dict, DataBase:dict)->None:
    if trip["end station id"] != trip["start station id"]:
        updateStation(trip, DataBase)
        updateRoute(trip, DataBase)
        DataBase['trips'] += 1

def updateRoute(trip:dict, DataBase:dict)->None:
    startId = int(trip["start station id"])
    endId = int(trip["end station id"])
    tripTime = int(trip["tripduration"])
    
    edgeRoute = graph.getEdge(DataBase['graph'],startId,endId)
    
    if edgeRoute is None:
        weight = Structure.newWeight()
        graph.addEdge(DataBase['graph'],startId,endId,weight)
        edgeRoute = graph.getEdge(DataBase['graph'],startId,endId)
        
        
    weight = edge.weight(edgeRoute)
    weight['time'] = aveTime(weight,tripTime)
    weight['users'] += 1 

def updateStation(trip:dict, DataBase:dict)->None:
    startId = int(trip["start station id"])
    endId = int(trip["end station id"])
    if not(map.contains(DataBase['station'],startId)):
        addStation(0,trip,DataBase)
    if not(map.contains(DataBase['station'],endId)):
        addStation(1,trip,DataBase)
    stationOut = map.get(DataBase['station'],startId)
    stationIn = map.get(DataBase['station'],endId)

    stationOut = mapentry.getValue(stationOut)
    stationIn = mapentry.getValue(stationIn)

    stationOut['tripsOut'] += 1
    stationIn['tripsIn'] += 1

    stationOut['trips'] += 1
    stationIn['trips'] += 1

def addStation(type:int, trip:dict, DataBase:dict)->None:
    types = (
        'start station ',
        'end station '
    )
    station = Structure.newStation()
    id = int(trip[types[type]+'id'])

    station['name'] = trip[types[type]+'name']
    station['latitude'] = trip[types[type]+'latitude']
    station['longitude'] = trip[types[type]+'longitude']

    map.put(DataBase['station'],id,station)
    graph.insertVertex(DataBase['graph'],id)
    

def aveTime(weight:dict, newTime)->float:
    time = weight['time']
    users = weight['users']
    result = ((time*users)+newTime)/(users+1)

    return result

