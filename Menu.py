from main import Cliente,Profesionales,Turno
c=Cliente()
t=Turno()
p=Proff()
g=Gestordeturnos("turnos.csv","clientes.csv")
print("----SISTEMA DE TURNOS-----")
print("----MENU----")


continuar = False

while not continuar:
    print("1.Registrar cliente")
    print("2.Solicitar turno")
    print("3.Listar turnos ")
    print("4.Modificar o Eliminar turno")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("Registrar cliente")
        ID = input("Registrar id del cliente: ")
        nombre=input("ingrese el nombre que desea registrar: ")
        apellido=input("ingrese el apellido que desea registrar: ")
        DNI=input("ingrese el dni que desea registrar: ")
        g.registrarcliente(ID=ID,nombre=nombre,apellido=apellido,dni=DNI)
        print("Cliente agregado")
        c.mostrarclientes("clientes.csv")

    elif opcion == "2":
        print("Solicitar turno")
        ID=input("ingrese su id: ")
        fecha=input("ingrese la fecha que desea el turno: ")
        hora=input("ingrese la hora que desea el turno: ")
        servicio=input("ingrese el servicio que desea para el turno: ")
        g.solicitarturno(ID=ID,fecha=fecha,hora=hora,servicio=servicio)
        print("Turno agregado correctamente")
        t.mostrarturnos("turnos.csv")

    elif opcion == "3":
        print("Listando turnos")
        g.listarturnos("turnos.csv")
    
    elif opcion=="4":
        opcion = input("Ingrese una opcion A O B: ")
        if opcion == "A":
            print("modificar turno")
            fecha=input("ingrese fecha: ")
            hora=input("ingrese hora: ")
            servicio=input("ingrese servicio: ")
            ID=input("ingrese id: ")# se modifica atravez del id 
            g.modificarturno(ID=ID,fecha=fecha,hora=hora,servicio=servicio)
            t.mostrarturnos("turnos.csv")
            print("Turno modificado")
        elif opcion == "B":
            print("Eliminar turno")
            ID= input("Ingrese el id del turno a eliminar: ")
            g.eliminarturno("turnos.csv",ID)
        else:
            print("Opcion invalida")

    elif opcion == "5":
        print("Saliendo del sistema")
        continuar = True

    else:
        print("Opción no válida")

print("Programa finalizado...")
