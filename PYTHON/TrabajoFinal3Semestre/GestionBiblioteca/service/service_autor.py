from core import core_autor
from domain.autor import Autor
from ui.ui import mostrar_menu_autor as ui
import config.logger_base as logger_base


def service_autor():
    opcion = None
    while opcion != 5:
        try:
            ui()
            opcion = int(input('Digite una opcion de menu (1-5):'))

            if opcion == 1:
                print('NUEVO AUTOR: ')
                print('Ingrese los siguientes datos:')
                nombre_autor = input('Nombre: ')
                apellido_autor = input('Apellido: ')
                libros_publicados = int(input('Ingrese cantidad de libros publicados: '))
                libro_escrito = input('ingrese los libros escrito: ')
                autor1 = Autor(nombre_autor, apellido_autor, libros_publicados, libro_escrito)
                core_autor.ABMAutor.nuevo_autor(autor1)
                print(autor1)
            elif opcion == 2:
                print('LISTADO DE AUTORES: ')
                core_autor.ABMAutor.listar_autor()
            elif opcion == 3:
                print('BAJA AUTOR:')
                id_autor = int(input('Ingrese el id del autor: '))
                core_autor.ABMAutor.borrar_autor(id_autor)
            elif opcion == 4:
                print('MODIFICAR DATOS DE AUTOR: ')
                id_autor = int(input('Ingrese el id del autor: '))
                core_autor.ABMAutor.buscar_autor(id_autor)
                nombre_autor = input('Nombre: ')
                apellido_autor = input('Apellido: ')
                libros_publicados = int(input('Ingrese cantidad de libros publicados: '))
                libro_escrito = input('ingrese los libros escrito: ')
                autor1 = Autor(nombre_autor, apellido_autor, libros_publicados, libro_escrito)
                core_autor.ABMAutor.modificar_autor(autor1, id_autor)
        except Exception as e:
            print(f'Ocurrio un error de tipo: {e}')
            opcion = None
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
    else:
        print(f'Volviendo al menu principal...')
