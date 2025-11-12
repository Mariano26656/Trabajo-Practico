from transforma import CSV2JSON
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
