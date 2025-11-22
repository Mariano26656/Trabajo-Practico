from transforma import CSV2JSON
###
class Registrobase(object):
    def __init__(self,**kwargs):
        self.valores=[]
        for clave,valor in kwargs.items():
            setattr(self,clave,valor)
            self.valores.append(valor)

    def mostrarvalores(self,archivo):
        ar = open(archivo,"r")
        linea=ar.readline().strip() 
        encabezados = linea.split(",")
        ar.close()
        ver = CSV2JSON(encabezados)
        ver.mostrar_archivo(archivo)
