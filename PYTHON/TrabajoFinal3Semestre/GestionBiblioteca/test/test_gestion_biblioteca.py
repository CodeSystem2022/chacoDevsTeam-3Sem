import ui.ui
from service.service_solicitud import SolicitudService
from service.service_autor import service_autor
from service.service_socio import service_socio
from service.service_libro import service_libro
from ui.ui import mostrar_menu_principal, mostrar_menu_solicitud
from config.database_manager import DatabaseManager


def inicio():
    try:
        DatabaseManager.inicializar()
    except Exception as e:
        print(e)


def ejecutar_opcion_abm(opcion):
    if opcion == "1":
        service_socio()
    elif opcion == "2":
        service_autor()
    elif opcion == "3":
        service_libro()
    elif opcion == "4":
        print("Volviendo al menu principal")
    else:
        print("Opción inválida. Por favor, elige una opción válida.")


def ejecutar_opcion_solicitud(opcion1):
    if opcion1 == "1":
        SolicitudService.service_solicitud_alta()
    elif opcion1 == "2":
        SolicitudService.service_devolucion_alta()
    elif opcion1 == "3":
        return
    else:
        print("Opción inválida. Por favor, elige una opción válida.")


def ejecutar_opcion(opcion):
    if opcion == "1":
        ui.ui.mostrar_menu_principal_abm1()
        opcion2 = ""
        while opcion2 != '4':
            opcion2 = input("Elige una opción (1-4): ")
            ejecutar_opcion_abm(opcion2)
            if opcion2 != '4':
                ui.ui.mostrar_menu_principal_abm1()
    elif opcion == "2":
        mostrar_menu_solicitud()
        opcion2 = ""
        while opcion2 != "3":
            opcion2 = input("Elige una opción (1-3): ")
            ejecutar_opcion_solicitud(opcion2)
            mostrar_menu_solicitud()
        else:
            print("Volviendo al menu principal.")


def menu():
    inicio()

    opcion_menu = ""
    while opcion_menu != "3":
        mostrar_menu_principal()
        try:
            opcion_menu = input("Elige una opción (1-3): ")
            ejecutar_opcion(opcion_menu)
            if 0 < int(opcion_menu) < 4:
                if int(opcion_menu) != 3:
                    mostrar_menu_principal()
            else:
                print("Opción inválida. Por favor, elige una opción válida.")
        except Exception as e:
            print(f'Opción inválida. Por favor, elige una opción válida, error: {e} ')
            opcion_menu = ""

menu()
print("Hasta Luego!")