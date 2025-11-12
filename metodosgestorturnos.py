from transforma import CSV2JSON
class Gestordeturnos(object):
    # mostrar los metodos correspondientes
    def __init__(self,archivoturno,archivoclientes):
        self.archivoturno=archivoturno
        self.archivoclientes=archivoclientes
    def registrarcliente(self,**kwargs):
        ar = open(self.archivoclientes, "a")  # "a" para agregar sin borrar lo anterior
        valores = [str(valor) for valor in kwargs.values()]  # convierte los valores a texto
        linea = ",".join(valores) + "\n"  # une los valores con comas y salto de línea
        ar.write(linea)
        ar.close()
        ar = open(self.archivoclientes, "r")
        lineas = [linea.strip() for linea in ar.readlines()]
        ar.close()
        return lineas

    def solicitarturno(self, **kwargs):
        ar = open(self.archivoturno, "a")
        valores = [str(valor) for valor in kwargs.values()]  # convierte los valores a texto
        linea = ",".join(valores) + "\n"  # une los valores con comas y salto de línea
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
