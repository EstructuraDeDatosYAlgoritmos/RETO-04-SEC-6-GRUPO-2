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
import csv
import os

from DISClib.ADT import queue

from App.Dev import Const
from App.Model import Add
from App.Model import Structure
from App.Model import Analysis

def initDataBase()->dict:
    return Structure.initDataBase()


def getFiles()->queue:
    files = queue.newQueue()
    for filename in os.listdir(Const.data_dir):
        if filename.endswith('.csv'):
            queue.enqueue(files,Const.data_dir+filename)       
    return files

def loadData(DataBase)->bool:
    files = getFiles()
    dialect = csv.excel()
    dialect.delimiter = ','
    while not(queue.isEmpty(files)):
        with open(queue.dequeue(files), encoding="utf-8") as csvfile:
            buffer = csv.DictReader(csvfile, dialect=dialect)
            cont = 0
            for element in buffer:
                cont += 1
                Add.addTrip(element,DataBase)
                if cont == Const.SIZE:
                    print(cont)
                    return True
        print(cont)

    return True

def analyze(dataBase):
    analysis = {
        'trips' : dataBase['trips'],
        'vertices' : Analysis.numVertices(dataBase),
        'edges' : Analysis.numEdges(dataBase),
        'Clusters' : Analysis.numClusters(dataBase)
    }
    return analysis