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

from App.Controller import DataBase
from App.Controller import Funtions

def ejecutarInitDataBase()->dict:
    result = DataBase.initDataBase()
    print('Base de datos creada')
    return result


def ejecutarLoadData(dataBase)->bool:
    result = DataBase.loadData(dataBase)
    analysis = DataBase.analyze(dataBase)
    print(f"Datos actualizados:\
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
    while listiterator.hasNext(topIn):
        element = listiterator.next(topIn)
        print(f'\t{element["station"]} con: {element["value"]} viajes')
    print('\n Estaciones de salida Top')
    while listiterator.hasNext(topOut):
        element = listiterator.next(topOut)
        print(f'\t{element["station"]} con: {element["value"]} viajes')
    print('\n Estaciones menos usadas')
    while listiterator.hasNext(bot):
        element = listiterator.next(bot)
        print(f'\t{element["station"]} con: {element["value"]} viajes')
