from config import logger_base
from core import core_libro as core_libro
from core import core_autor as core_autor
from domain.libro import Libro as Libro
from ui.ui import mostrar_menu_libro as ui
from ui.ui import mostrar_menu_principal_abm1 as ui_principal


def service_libro():
    opcion = None
    while opcion != 6:
        try:
            ui()
            opcion = int(input('Digite una opcion de menu (1-5):'))
            if opcion == 1:
                print('NUEVO LIBRO: ')
                print('Ingrese los siguientes datos:')
                isbn = input('ISBN: ')
                reg_validar = core_libro.ABMLibro.buscar_libro_por_isbn(isbn)
                if reg_validar is not None:
                    print(f'Ya existe un libro con dicho ISBN: {isbn} id libro: {reg_validar}')
                    print('Debe acceder a la opcion modificar libro, agregar libro existente')
                else:
                    titulo = input('Titulo: ')
                    genero = input('Genero: ')
                    anio_publicacion = int(input('anio de publicacion: '))
                    cantidad = int(input('Cantidad de copias: '))
                    editorial = input('Editorial: ')
                    metodo = int(input("AUTOR\nDebe ingresar un modo de registro\n1: Nombre: \n2: Apellido: \n3: id:"))
                    if metodo == 1:
                        ingreso = input("Nombre de Autor: ")
                        registro = core_autor.ABMAutor.buscar_autor_por_nombre(ingreso)
                        while registro is None:
                            print(f'Ocurrio un error, {ingreso} no se encuentra ese autor')
                            ingreso = input("Ingrese el Nombre nuevamente: ")
                            registro = core_autor.ABMAutor.buscar_autor_por_nombre(ingreso)
                        else:
                            libro1 = Libro(titulo, genero, anio_publicacion, isbn, registro, cantidad, editorial)
                            core_libro.ABMLibro.nuevo_libro(libro1)
                            opcion = None
                    if metodo == 2:
                        ingreso = input("Apellido de Autor: ")
                        registro = core_autor.ABMAutor.buscar_autor_por_apellido(ingreso)
                        while registro is None:
                            print(f'Ocurrio un error, {ingreso} no se encuentra ese autor')
                            ingreso = input("Apellido de Autor: ")
                            registro = core_autor.ABMAutor.buscar_autor_por_apellido(ingreso)
                        else:
                            libro1 = Libro(titulo, genero, anio_publicacion, isbn, registro, cantidad, editorial)
                            core_libro.ABMLibro.nuevo_libro(libro1)
                            opcion = None
                    if metodo == 3:
                        ingreso = int(input('Autor id: '))
                        registro = core_autor.ABMAutor.buscar_autor(ingreso)
                        if registro is not None:
                            libro1 = Libro(titulo, genero, anio_publicacion, isbn, ingreso, cantidad, editorial)
                            core_libro.ABMLibro.nuevo_libro(libro1)
                        else:
                            print(f'Ocurrio un error, no se encuentra ese autor')
                            opcion = None
            elif opcion == 2:
                print('LISTADO DE LIBROS: ')
                core_libro.ABMLibro.listar_libros()
            elif opcion == 3:
                print('BAJA LIBRO:')
                id_libro = int(input('Ingrese el id del libro: '))
                core_libro.ABMLibro.borrar_libro(id_libro)
            elif opcion == 4:
                print('MODIFICAR DATOS DE UN LIBRO: ')
                id_libro = int(input('Ingrese el id del libro: '))
                core_libro.ABMLibro.buscar_libro(id_libro)
                titulo = input('Titulo: ')
                genero = input('Genero: ')
                editorial = input('Editorial: ')
                autor_id = int(input('Autor id: '))
                anio_publicacion = int(input('anio de publicacion: '))
                isbn = input('ISBN: ')
                libro1 = Libro(titulo, genero, anio_publicacion, isbn, autor_id, 0, editorial)
                core_libro.ABMLibro.modificar_libro(libro1, id_libro)
            elif opcion == 5:
                print('NUEVO LIBRO EXISTENTE: ')
                print('Ingrese los siguientes datos:')
                isbn = input('ISBN: ')
                id_lib = core_libro.ABMLibro.buscar_libro_por_isbn(isbn)
                if id_lib is not None:
                    cant_lib = core_libro.ABMLibro.buscar_cantidad_libro_por_isbn(isbn)
                    if cant_lib[0] is None:
                        nuevo_valor = 0
                        nuevos_valores = (nuevo_valor, cant_lib[0])
                        cantidad = int(input('Ingrese la cantidad de libros a agregar a la existencia: '))
                        cantidad_nueva = int(nuevos_valores[0]) + cantidad
                    else:
                        cantidad = int(input('Ingrese la cantidad de libros a agregar a la existencia: '))
                        cantidad_nueva = int(cant_lib[0]) + cantidad
                    core_libro.ABMLibro.agregar_libro_existente(cantidad_nueva, id_lib)
                else:
                    print(f'No se encuentra el ISBN: {isbn}')

        except Exception as e:
            print(f'Ocurrio un error de tipo: {e}')
            opcion = None
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
    else:
        print(f'Volviendo al menu principal...')