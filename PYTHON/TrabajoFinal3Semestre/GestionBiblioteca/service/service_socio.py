from config import logger_base
from core import core_socio as core_socio
from domain.socio import Socio as Socio
from utils.date_utils import obtener_fecha_hoy as fecha_hoy
from ui.ui import mostrar_menu_socio as ui


def service_socio():
    opcion = None
    while opcion != 5:
        try:
            ui()
            opcion = int(input('Digite una opcion de menu (1-5):'))

            if opcion == 1:
                print('NUEVO SOCIO: ')
                print('Ingrese los siguientes datos:')
                fecha = fecha_hoy()
                nombre_socio = input('Nombre: ')
                apellido_socio = input('Apellido: ')
                dni_socio = int(input('Dni: '))
                cel_socio = int(input('Celular: '))
                domicilio_socio = input('Domiclio: ')
                email_socio = input('Email:')
                socio1 = Socio(fecha, 0, nombre_socio, apellido_socio, dni_socio, cel_socio, domicilio_socio,
                               email_socio)
                core_socio.ABMSocio.nuevo_socio(socio1)
                print(socio1)
            elif opcion == 2:
                print('LISTADO DE SOCIOS: ')
                core_socio.ABMSocio.listar_socios()
            elif opcion == 3:
                print('BAJA SOCIO:')
                id_socio = int(input('Ingrese el id del socio: '))
                core_socio.ABMSocio.borrar_socio(id_socio)
            elif opcion == 4:
                print('MODIFICAR DATOS DE SOCIO: ')
                fecha = fecha_hoy()
                id_socio = int(input('Ingrese el id del socio: '))
                core_socio.ABMSocio.buscar_socio(id_socio)
                nombre_socio = input('Nombre: ')
                apellido_socio = input('Apellido: ')
                dni_socio = int(input('Dni: '))
                cel_socio = int(input('Celular: '))
                domicilio_socio = input('Domiclio: ')
                email_socio = input('Email:')
                socio1 = Socio(fecha, 0, nombre_socio, apellido_socio, dni_socio, cel_socio, domicilio_socio,
                               email_socio)
                core_socio.ABMSocio.modificar_socio(socio1, id_socio)
        except Exception as e:
            print(f'Ocurrio un error de tipo: {e}')
            opcion = None
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
    else:
        print(f'Volviendo al menu principal...')