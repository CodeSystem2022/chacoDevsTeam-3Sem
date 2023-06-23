from config import logger_base
from core import core_libro as core_libro
from core import core_socio as core_socio
from core import core_solicitud as core_solicitud
from domain.solicitud import Solicitud
from utils.date_utils import obtener_fecha_hoy
from enums import estados_libros


class SolicitudService:

    @classmethod
    def service_solicitud_alta(cls):
        opcion = ""
        while opcion != "3":
            opcion = input("1. Registrar una solicitud de un libro:\n2. Listar Solicitudes:\n3. Volver \n")
            if opcion == "1":
                try:
                    print('**********************************\n\t\t SOLICITUD DE LIBRO \n**********************************')
                    registro_libro = cls.buscar_libro()
                    if registro_libro is not None:
                        cantidad = core_libro.ABMLibro.buscar_cantidad_libro_por_id(registro_libro)
                        if cantidad[0] is not None:
                            if cantidad[0] > 0:
                                registro_socio = cls.buscar_socio()
                                if registro_libro is not None and registro_socio is not None:
                                    solicitud = Solicitud(registro_libro, registro_socio, obtener_fecha_hoy(),
                                                          estados_libros.EstadoLibro.NO_DEVUELTO.value)
                                    core_solicitud.ABMSolicitud.nueva_solicitud(solicitud)
                                    cant_lib = core_libro.ABMLibro.buscar_cantidad_libro_por_id(registro_libro)
                                    cantidad_nueva = int(cant_lib[0]) + -1
                                    core_libro.ABMLibro.agregar_libro_existente(cantidad_nueva, registro_libro)
                            else:
                                print(f'No hay existencia disponible para el libro: ')
                                core_libro.ABMLibro.buscar_libro(registro_libro)
                        else:
                            print(f'La existencia del libro {registro_libro} esta vacia')
                    else:
                        print(f'Ocurrio un error al registrar la solicitud')

                except Exception as e:
                    print(f'Ocurrio un error de tipo: {e}')
                    logger_base.log.error(f'OCURRIO UN ERROR {e}')
            elif opcion == "2":
                opcion2 = None
                while opcion2 != "3":
                    opcion2 = input("1. Listar por socio:\n2. Listar general:\n3. Volver \n")
                    if opcion2 == "1":
                        print("HISTORIAL SOLICITUDES SOCIO: ")
                        registro_socio = cls.buscar_socio()
                        core_solicitud.ABMSolicitud.listar_solicitud_socio(registro_socio)
                    elif opcion2 == "2":
                        print("HISTORIAL SOLICITUDES GENERAL")
                        core_solicitud.ABMSolicitud.listar_solicitudes()
                else:
                    print(f'Volviendo...')
        else:
            print(f'Volviendo al menu principal...')

    @classmethod
    def service_devolucion_alta(cls):
        opcion = input("1. Registrar una devolucion de un libro:\n2. Listar devoluciones:\n3. Volver ")
        try:
            if opcion == "1":
                print('DEVOLUCIÓN DE LIBRO: ')
                registro_socio = cls.buscar_socio()
                registro_libro = cls.buscar_libro()

                core_solicitud.ABMSolicitud.listar_solicitudes_por_id(registro_socio, registro_libro)

                if registro_libro is not None and registro_socio is not None:
                    solicitud = Solicitud(registro_libro, registro_socio, obtener_fecha_hoy(),
                                          estados_libros.EstadoLibro.DEVUELTO.value)
                    core_solicitud.ABMSolicitud.nueva_solicitud(solicitud)
                    cant_lib = core_libro.ABMLibro.buscar_cantidad_libro_por_id(registro_libro)
                    cantidad_nueva = int(cant_lib[0]) + 1
                    core_libro.ABMLibro.agregar_libro_existente(cantidad_nueva, registro_libro)

            elif opcion == "2":
                opcion2 = None
                while opcion2 != "3":
                    opcion2 = input("1. Listar por socio:\n2. Listar general:\n3. Volver ")
                    if opcion2 == "1":
                        print("HISTORIAL DEVOLUCIONES SOCIO: ")
                        registro_socio = cls.buscar_socio()
                        core_solicitud.ABMSolicitud.listar_devolucion_socio(registro_socio)
                    elif opcion2 == "2":
                        print("HISTORIAL DEVOLUCIONES GENERAL")
                        core_solicitud.ABMSolicitud.listar_devolucion()
                else:
                    print(f'Volviendo...')

        except Exception as e:
            print(f'Ocurrio un error de tipo: {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_socio(cls):
        print('Ingrese los siguientes datos:')
        socio = int(input("SOCIO:\nIngrese un modo de busqueda de SOCIO\n1: Nombre: \n2: Apellido: \n3: id: "))
        if socio == 1:
            ingreso = input("NOMBRE: ")
            registro_socio = core_socio.ABMSocio.buscar_socio_por_nombre(ingreso)
            while registro_socio is None:
                print(f'Ocurrio un error, NOMBRE: {ingreso} no se encuentra ese socio')
                ingreso = input("Ingrese el Nombre nuevamente: ")
                registro_socio = core_socio.ABMSocio.buscar_socio_por_nombre(ingreso)
        elif socio == 2:
            ingreso = input("APELLIDO: ")
            registro_socio = core_socio.ABMSocio.buscar_socio_por_apellido(ingreso)
            while registro_socio is None:
                print(f'Ocurrio un error, APELLIDO: {ingreso} no se encuentra ese socio')
                ingreso = input("ISBN: ")
                registro_socio = core_socio.ABMSocio.buscar_socio_por_apellido(ingreso)
        elif socio == 3:
            ingreso = int(input('SOCIO ID: '))
            registro_socio = core_socio.ABMSocio.buscar_socio_por_id(ingreso)
            while registro_socio is None:
                print(f'Ocurrio un error, ID: {ingreso} no se encuentra ese socio')
                ingreso = input("Libro id: ")
                registro_socio = core_socio.ABMSocio.buscar_socio_por_id(ingreso)

        core_socio.ABMSocio.buscar_socio(registro_socio)
        return registro_socio

    @classmethod
    def buscar_libro(cls):
        libro = int(input("\t\t\t\tLIBRO\nDebe ingresar un modo de registro\n1: Titulo: \n2: ISBN: \n3: id: \n**********************************\n"))
        if libro == 1:
            ingreso = input("Titulo: ")
            registro_libro = core_libro.ABMLibro.buscar_libro_por_titulo(ingreso)
            while registro_libro is None:
                print(f'Ocurrio un error, TITULO: {ingreso} no se encuentra ese libro')
                ingreso = input("Ingrese el Nombre nuevamente: ")
                registro_libro = core_libro.ABMLibro.buscar_libro_por_titulo(ingreso)
        elif libro == 2:
            ingreso = input("ISBN: ")
            registro_libro = core_libro.ABMLibro.buscar_libro_por_isbn(ingreso)
            while registro_libro is None:
                print(f'Ocurrio un error, ISBN: {ingreso} no se encuentra ese libro')
                ingreso = input("ISBN: ")
                registro_libro = core_libro.ABMLibro.buscar_libro_por_isbn(ingreso)
        elif libro == 3:
            ingreso = int(input('Libro id: '))
            registro_libro = core_libro.ABMLibro.buscar_id_libro_por_id(ingreso)
            while registro_libro is None:
                print(f'Ocurrio un error, ID: {ingreso} no se encuentra ese libro')
                ingreso = input("Libro id: ")
                registro_libro = core_libro.ABMLibro.buscar_id_libro_por_id(ingreso)
        return registro_libro