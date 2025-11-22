from transforma import CSV2JSON
class Gestordeturnos(Registro):
    # mostrar los metodos correspondientes
    def __init__(self,archivoturno,archivoclientes):
        self.archivoturno=archivoturno
        self.archivoclientes=archivoclientes
    def registrarcliente(self,**kwargs):
        super().registro(self.archivoclientes,**kwargs)

    def solicitarturno(self, **kwargs):
        super().registro(self.archivoturno,**kwargs)

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

    def eliminarturno(self,archivo,valor):
        ar=open(archivo,"r")
        lineas= ar.readlines()
        ar.close()
        i=0
        nueva=[]
        while i<len(lineas):
            linea=lineas[i].strip().split(",")
            if len(linea) > 1 and linea[0] != valor:
                nueva.append(",".join(linea)+"\n")
            i+=1
        ar=open(archivo,"w")
        ar.writelines(nueva)
        ar.close()
