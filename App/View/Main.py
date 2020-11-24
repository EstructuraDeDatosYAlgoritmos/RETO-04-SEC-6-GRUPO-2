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
import config
import sys

from App.View import Init
from App.View import Menu


def main()->None:
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    dataReady = False #vigila el estado de la informacion
    dataBase = None

    while True:
        Menu.mainMenu() #imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n') #leer opción ingresada
        
        if len(inputs)>0 and (dataReady or int(inputs[0])<=2) and (dataBase is not None or int(inputs[0])<=2):
            if int(inputs[0]) == 1:  #opcion 1
                dataBase = Init.ejecutarInitDataBase()

            elif int(inputs[0]) == 2:  #opcion 2
                dataReady = Init.ejecutarLoadData(dataBase)
            
            elif int(inputs[0]) == 3:  #opcion 3
               Init.ejecutarClustersViajes(dataBase)
                
            elif int(inputs[0]) == 5:  #opcion 5
               Init.ejecutarEstacionesCriticas(dataBase)
                
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
        else:
            print("Porfavor, cargue datos")

if __name__ == "__main__":
    main()