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


from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator

from App.View import Menu
from App.Controller import DataBase
from App.Controller import Funtions
from App.Model import Analysis

def ejecutarInitDataBase()->dict:
    result = DataBase.initDataBase()
    print('\nBase de datos creada')
    return result

def ejecutarInitTracking(dataBase):
    DataBase.initTracking(dataBase)
    print('\nIniciando Carga')

def ejecutarLoadTracking(dataBase):
    DataBase.loadTracking(dataBase)
    print('IDs cargados: ',dataBase['bikes'])

def ejecutarLoadData(dataBase)->bool:
    print('\nIniciando Carga')
    result = DataBase.loadData(dataBase)
    analysis = DataBase.analyze(dataBase)
    print(f"\nDatos actualizados:\
            \n\tViajes: {analysis['trips']}\
            \n\tVértices: {analysis['vertices']}\
            \n\tArcos: {analysis['edges']}\
            \n\tClústers: {analysis['Clusters']}")
    return result

def ejecutarClustersViajes(dataBase)->None:
    id1 = int(input('Ingrese la primera id: '))
    id2 = int(input('Ingrese la segunda id: '))
    analysis = Funtions.ClustersViajes(dataBase,id1,id2)
    print(f"\n\tSe han encontrado {analysis['clusters']} Clústers")
    if analysis['conected']:
        print(f'\n\tlas estaciones {id1} y {id2} estan conectadas')
    else:
        print(f'\n\tlas estaciones {id1} y {id2} no estan conectadas')

def ejecutarEstacionesCriticas(dataBase)->None:
    analysis = Funtions.estacionesCriticas(dataBase)
    topIn = listiterator.newIterator(analysis[0]) 
    topOut = listiterator.newIterator(analysis[1]) 
    bot = listiterator.newIterator(analysis[2]) 

    print('\n Estaciones de llegada Top')
    cont = 1
    while listiterator.hasNext(topIn):
        element = listiterator.next(topIn)
        print(f'\t{cont}. {element["station"]} con: {element["value"]} viajes')
        cont += 1
    print('\n Estaciones de salida Top')
    cont = 1
    while listiterator.hasNext(topOut):
        element = listiterator.next(topOut)
        print(f'\t{cont}. {element["station"]} con: {element["value"]} viajes')
        cont += 1
    print('\n Estaciones menos usadas')
    while listiterator.hasNext(bot):
        element = listiterator.next(bot)
        print(f'\t#. {element["station"]} con: {element["value"]} viajes')

def ejecutarEstacionesParaPublicidad(dataBase):
    Menu.targetMenu()
    target = int(input('Seleccionado: '))
    analysis = Funtions.EstacionesParaPublicidad(dataBase,target)
    analysis = listiterator.newIterator(analysis)
    if listiterator.hasNext(analysis):
        print('\nLas siguientes estaciones cumplen las condiciones:')
        while listiterator.hasNext(analysis):
            element = listiterator.next(analysis)
            print(f"\n\tSalida: {element['vertexA']}")
            print(f"\tLlegada: {element['vertexB']}")
            print(f"\tUsuarios: {element['weight']}")
    else:
        print('\nNo se encontraron estaciones que cumplan las condiciones')

def ejecutarIdentificarBicicletas(dataBase):
    bikeID = int(input('\nID de la bicicleta: '))
    date = input("Ingrese la fecha (YYYY-MM-DD): ")

    analysis = Funtions.IdentificarBicicletas(dataBase,bikeID,date)
    stations = listiterator.newIterator(analysis['stations'])

    print(f'\nTiempo de uso: {analysis["useTime"]}')
    print(f"Timpo estacionada: {analysis['stopTime']}")
    print('Estaciones Usadas:')
    while listiterator.hasNext(stations):
        print('\t',listiterator.next(stations))

def ejecutarRutasCirculares(database)->None:
    tiempoi = int(input('Ingrese el primero tiempo del rango que desea: '))
    tiempof = int(input('Ingrese el segundo tiempo del rango que desea: '))
    station1 = input('Ingrese la estacion inicial: ')
    analysis = Analysis.rutasCirculares(database, tiempoi, tiempof, station1)
    print(f'\n\tSe han encontrado {analysis[0]} rutas circulares las cuales son: {analysis[1]}')