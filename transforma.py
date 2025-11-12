import json
import csv
class CSV2JSON(object):
    def __init__(self, attributes):
        self.attributes = attributes  # "nombre", "apellido

    def todict(self, values):
        if len(values) != len(self.attributes):
            return None
        d = {}
        i = 0
        while i < len(values):
            d[self.attributes[i]] = values[i]
            i = i + 1
        return d
    def mostrar_archivo(self, archivo):
        ar = open(archivo, "r")
        ar.readline()
        lineas = ar.readlines()
        ar.close()

        i = 0
        while i < len(lineas):
            datos = lineas[i].strip().split(",")
            dic = self.todict(datos)
            # imprime cada diccionario en formato JSON individual
            print(json.dumps(dic))
            i = i + 1
