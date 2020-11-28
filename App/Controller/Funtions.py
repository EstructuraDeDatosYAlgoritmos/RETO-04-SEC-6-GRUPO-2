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
from DISClib.ADT import list
from DISClib.DataStructures import listiterator
from datetime import datetime
from App.Model import Analysis

def ClustersViajes(dataBase,id1,id2)->dict:
    respuesta = {
        'clusters' : Analysis.numClusters(dataBase),
        'conected' : Analysis.sameCluster(dataBase,id1,id2)
    }
    return respuesta

def rutasCirculares(dataBase, tiempoi, tiempof, estacioni):
    analisis = Analysis.rutasCirculares(dataBase, tiempoi, tiempof, estacioni)
    return analisis
    
def estacionesCriticas(dataBase)->dict:
    top3In = list.newList()
    top3Out = list.newList()
    bot3 = list.newList()

    analysis = Analysis.topViajes(dataBase)

    i = 0
    while i < 3:
        list.addLast(top3In,list.removeFirst(analysis[0]))
        list.addLast(top3Out,list.removeFirst(analysis[1]))
        list.addFirst(bot3, list.removeLast(analysis[2]))
        i += 1
    del analysis

    return (top3In,top3Out,bot3)

def EstacionesParaPublicidad(dataBase,target):
    analysis = Analysis.topTarget(dataBase,target)
    analysis = listiterator.newIterator(analysis)

    topList = list.newList()

    maxVal = 0
    switch = True
    element = None
    if listiterator.hasNext(analysis):
        element = listiterator.next(analysis)
        maxVal = element['weight']
    while switch and listiterator.hasNext(analysis):
        element['vertexA'] = Analysis.getStation(dataBase,element['vertexA'])['name']
        element['vertexB'] = Analysis.getStation(dataBase,element['vertexB'])['name']
        list.addLast(topList,element)
        element = listiterator.next(analysis)
        switch = maxVal == element['weight']
        
    return topList

def IdentificarBicicletas(dataBase, bikeID, date):
    date = datetime.strptime(date,'%Y-%m-%d')
    tracking = Analysis.bikeTracking(dataBase,bikeID,date.date())

    tracking['stopTime'] = secondsToTime(tracking['stopTime'])
    tracking['useTime'] = secondsToTime(tracking['useTime'])

    return tracking
    
def rutaTuristica(dataBase,lon1,lat1,lon2,lat2):
    startStation = Analysis.nearbyStations(dataBase,lon1,lat1)
    endStation = Analysis.nearbyStations(dataBase,lon2,lat2)
    route = Analysis.nearbyRoute(dataBase,startStation,endStation)
    return {
        'start': Analysis.getStation(dataBase,startStation)['name'],
        'end': Analysis.getStation(dataBase,endStation)['name'],
        'route': route[0],
        'time': secondsToTime(route[1])
    }

def secondsToTime(seconds:int)->datetime:
    h = (seconds // 60) // 60
    m = (seconds // 60) % 60
    s = seconds % 60

    time = f'{h}:{m}:{s}'

    return time