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
            print("*" * 50)
            print('SOLICITUD DE LIBRO'.center(50, ' '))
            print("*" * 50)
            print("1. Registrar una solicitud de un libro:\n2. Listar Solicitudes:\n3. Volver ")
            print("*" * 50)
            opcion = input('Elige una opción (1-3): ')
            if opcion == "1":
                try:
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
                    print("*" * 50)
                    print('LISTADOS DE SOLICITUDES '.center(50, ' '))
                    print("*" * 50)
                    print("1. Listar por socio:\n2. Listar general:\n3. Volver ")
                    print("*" * 50)
                    opcion2 = input('Elige una opcion (1-3): ')
                    if opcion2 == "1":
                        registro_socio = cls.buscar_socio()
                        print("*" * 50)
                        if registro_socio is not None:
                            print(f'HISTORIAL SOCIO: {registro_socio[0]}'.center(50))
                            print("*" * 50)
                            core_solicitud.ABMSolicitud.listar_solicitud_socio(registro_socio)
                            print("*" * 50)
                    elif opcion2 == "2":
                        print("*" * 50)
                        print('HISTORIAL SOLICITUDES GENERAL'.center(50, ' '))
                        print("*" * 50)
                        core_solicitud.ABMSolicitud.listar_solicitudes()
                        print("*" * 50)
                    elif int(opcion2) < 1 or int(opcion2)>3:
                        print("Opción inválida. Por favor, elige una opción válida.")
                else:
                    print(f'Volviendo...')
            elif int(opcion) > 3 or int(opcion) < 1:
                print("Opción inválida. Por favor, elige una opción válida.")
        else:
            print(f'Volviendo...')

    @classmethod
    def service_devolucion_alta(cls):
        print("*" * 50)
        print('DEVOLUCION DE LIBRO'.center(50, ' '))
        print("*" * 50)
        print("1. Registrar una devolucion de un libro:\n2. Listar devoluciones:\n3. Volver ")
        print("*" * 50)
        opcion = input('Elige una opcion (1-3): ')
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
                    print("*" * 50)
                    print('DEVOLUCION DE LIBRO'.center(50))
                    print("*" * 50)
                    print("1. Listar por socio:\n2. Listar general:\n3. Volver ")
                    print("*" * 50)
                    opcion2 = input('Elige una opcion (1-3): ')
                    if opcion2 == "1":
                        registro_socio = cls.buscar_socio()
                        print("*" * 50)
                        if registro_socio is not None:
                            print(f'HISTORIAL SOCIO: {registro_socio[0]}'.center(50))
                            print("*" * 50)
                            core_solicitud.ABMSolicitud.listar_devolucion_socio(registro_socio)
                    elif opcion2 == "2":
                        print("*" * 50)
                        print("HISTORIAL DEVOLUCIONES GENERAL".center(50))
                        print("*" * 50)
                        core_solicitud.ABMSolicitud.listar_devolucion()
                        print("*" * 50)
                    elif int(opcion) > 3 or int(opcion) < 1:
                         print("Opción inválida. Por favor, elige una opción válida.");
                else:
                    print(f'Volviendo...')

        except Exception as e:
            print(f'Ocurrio un error de tipo: {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_socio(cls):
        print("*" * 50)
        print('SOCIO'.center(50))
        print("*" * 50)
        print("Ingrese un modo de busqueda de SOCIO\n1: Nombre: \n2: Apellido: \n3: id: ")
        print("*" * 50)
        registro_socio = None
        socio = int(input('Elige una opcion (1-3): '))
        if socio == 1:
            ingreso = input("NOMBRE: ")
            registro_socio = core_socio.ABMSocio.buscar_socio_por_nombre(ingreso)
            while registro_socio is None and ingreso != "0":
                print(f'Ocurrio un error, NOMBRE: {ingreso} no se encuentra ese socio')
                ingreso = input("Ingrese el Nombre nuevamente o ingrese 0 para volver:: ")
                if ingreso != "0":
                    registro_socio = core_socio.ABMSocio.buscar_socio_por_nombre(ingreso)
        elif socio == 2:
            ingreso = input("APELLIDO: ")
            registro_socio = core_socio.ABMSocio.buscar_socio_por_apellido(ingreso)
            while registro_socio is None and ingreso != "0":
                print(f'Ocurrio un error, APELLIDO: {ingreso} no se encuentra ese socio')
                ingreso = input("Ingrese el numero de ISBN ingrese 0 para volver:: ")
                if ingreso != "0":
                    registro_socio = core_socio.ABMSocio.buscar_socio_por_apellido(ingreso)
        elif socio == 3:
            ingreso = int(input('SOCIO ID: '))
            registro_socio = core_socio.ABMSocio.buscar_socio_por_id(ingreso)
            while registro_socio is None and ingreso != "0":
                print(f'Ocurrio un error, ID: {ingreso} no se encuentra ese socio')
                ingreso = input("Ingrese el Libro id o ingrese 0 para volver: ")
                if ingreso != "0":
                    registro_socio = core_socio.ABMSocio.buscar_socio_por_id(ingreso)
        elif socio < 0 or socio > 3:
            print("Opción inválida. Por favor, elige una opción válida.")

        if registro_socio is not None:
            core_socio.ABMSocio.buscar_socio(registro_socio)
            return registro_socio

    @classmethod
    def buscar_libro(cls):
        print("*" * 50)
        print("LIBRO".center(50))
        print("*" * 50)
        print("Debe ingresar un modo de registro\n1: Titulo: \n2: ISBN: \n3: id: ")
        print("*" * 50)
        libro = int(input('Elige una opcion (1-3): '))
        if libro == 1:
            ingreso = input("Titulo: ")
            registro_libro = core_libro.ABMLibro.buscar_libro_por_titulo(ingreso)
            while registro_libro is None and ingreso != 0:
                print(f'Ocurrio un error, TITULO: {ingreso} no se encuentra ese libro')
                ingreso = input("Ingrese el Nombre nuevamente o ingrese 0 para volver: ")
                if ingreso != "0":
                    registro_libro = core_libro.ABMLibro.buscar_libro_por_titulo(ingreso)
        elif libro == 2:
            ingreso = input("ISBN: ")
            registro_libro = core_libro.ABMLibro.buscar_libro_por_isbn(ingreso)
            while registro_libro is None and ingreso != 0:
                print(f'Ocurrio un error, ISBN: {ingreso} no se encuentra ese libro')
                ingreso = input("Ingrese nuevamente el ISBN o ingrese 0 para volver: ")
                if ingreso != "0":
                    registro_libro = core_libro.ABMLibro.buscar_libro_por_isbn(ingreso)
        elif libro == 3:
            ingreso = int(input('Libro id: '))
            registro_libro = core_libro.ABMLibro.buscar_id_libro_por_id(ingreso)
            while registro_libro is None and ingreso != 0:
                print(f'Ocurrio un error, ID: {ingreso} no se encuentra ese libro')
                ingreso = int(input("Ingrese el Libro id  o ingrese 0 para volver: "))
                if ingreso != 0:
                    registro_libro = core_libro.ABMLibro.buscar_id_libro_por_id(ingreso)

        return registro_libro
