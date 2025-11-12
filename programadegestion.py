import json
import csv

class CSV2JSON(object):
    def __init__(self, attributes):
        self.attributes = attributes  

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
            print(json.dumps(dic))
            i = i + 1


class Cliente(object):
    def __init__(self, **kwargs):
        self.valores = []
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)
            self.valores.append(valor)
    def mostrarcliente(self,archivo):

        ar = open(archivo, "r")
        primera_linea = ar.readline().strip()
        encabezados = primera_linea.split(",")
        ar.close()
        

        ver = CSV2JSON(encabezados)
        ver.mostrar_archivo(archivo)

class Proff(object):
    def __init__(self, **kwargs):
        self.valores = []
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)
            self.valores.append(valor)
    def mostrarprof(self, archivo):

        ar = open(archivo, "r")
        primera_linea = ar.readline().strip()
        encabezados = primera_linea.split(",")
        ar.close()
        

        ver = CSV2JSON(encabezados)
        ver.mostrar_archivo(archivo)


class Turno(object):
    def __init__(self, **kwargs):
        self.valores = []
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)
            self.valores.append(valor)

    def mostrarturnos(self, archivo):

        ar = open(archivo, "r")
        primera_linea = ar.readline().strip()
        encabezados = primera_linea.split(",")
        ar.close()
        

        ver = CSV2JSON(encabezados)
        ver.mostrar_archivo(archivo)

class Gestordeturnos(object):
    # mostrar los metodos correspondientes
    def __init__(self,archivoturno,archivoclientes):
        self.archivoturno=archivoturno
        self.archivoclientes=archivoclientes
    def registrarcliente(self,**kwargs):
        ar = open(self.archivoclientes, "a") 
        valores = [str(valor) for valor in kwargs.values()] 
        linea = ",".join(valores) + "\n" 
        ar.write(linea)
        ar.close()
        ar = open(self.archivoclientes, "r")
        lineas = [linea.strip() for linea in ar.readlines()]
        ar.close()
        return lineas

    def solicitarturno(self, **kwargs):
        ar = open(self.archivoturno, "a")
        valores = [str(valor) for valor in kwargs.values()]  
        linea = ",".join(valores) + "\n"  
        ar.write(linea)
        ar.close()
        ar=open(self.archivoturno,"r")
        lineas = [linea.strip() for linea in ar.readlines()]
        ar.close()
        return lineas

    def modificarturno(self,**kwargs):
        ar=open(self.archivoturno,"r")
        lineas=ar.readlines()
        ar.close()
        nuevovalor=[]
        i=0
        modificar = list(kwargs.values())
        while i<=len(lineas)-1:
            linea= lineas[i].strip().split(",")
            if linea[0] == modificar[0]:
                nuevovalor.append(",".join(modificar)+"\n")
            else:
                nuevovalor.append(",".join(linea)+"\n")
            i+=1 
        ar=open(self.archivoturno,"w")
        ar.writelines(nuevovalor)
        ar.close()
    def listarturnos(self,archivo):
        ar = open(archivo, "r")
        primera_linea = ar.readline().strip()
        encabezados = primera_linea.split(",")
        ar.close()
        ver = CSV2JSON(encabezados)
        ver.mostrar_archivo(archivo)


c=Cliente()
t=Turno()
p=Proff()
g=Gestordeturnos("tt.csv","cc.csv")
print("----SISTEMA DE TURNOS-----")
print("----MENU----")

continuar = "si"

while continuar == "si":
    print("1.Registrar cliente")
    print("2.Solicitar turno")
    print("3.Listar turnos")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("Registrar cliente")
        nombre=input("ingrese el nombre que desea registrar: ")
        apellido=input("ingrese el apellido que desea registrar: ")
        DNI=input("ingrese el dni que desea registrar: ")
        g.registrarcliente(nombre=nombre,apellido=apellido,DNI=DNI)
        c.mostrarcliente("cc.csv")

    elif opcion == "2":
        print("Solicitar turno")
        ID=input("ingrese su id: ")
        Fecha=input("ingrese la fecha que desea el turno: ")
        Hora=input("ingrese la hora que desea el turno: ")
        Servicio=input("ingrese el servicio que desea para el turno: ")
        g.solicitarturno(ID,Fecha,Hora,Servicio)

    elif opcion == "3":
        print("Listando turnos")
        g.listarturnos("tt.csv")

    elif opcion == "5":
        print("Saliendo del sistema")
        continuar = "no"

    else:
        print("Opción no válida")

print("Programa finalizado...")
