from core import core_autor
from domain.autor import Autor
from ui.ui import mostrar_menu_autor as ui_autor
import config.logger_base as logger_base


def service_autor():
    opcion = None
    while opcion != 5:
        try:
            ui_autor()
            opcion = int(input('Digite una opcion de menu (1-5):'))

            if opcion == 1:
                print("*" * 50)
                print('NUEVO AUTOR'.center(50))
                print("*" * 50)
                print('Ingrese los siguientes datos:')
                nombre_autor = input('Nombre: ')
                apellido_autor = input('Apellido: ')
                anio_nacimiento = int(input('Año de nacimiento: '))
                nacionalidad = input('País de origen: ')
                print("*" * 50)
                autor1 = Autor(nombre_autor, apellido_autor, 0, 0, None, None, anio_nacimiento, nacionalidad)
                core_autor.ABMAutor.nuevo_autor(autor1)
                print(autor1)
                print("*" * 50)
                print("\n")
            elif opcion == 2:
                print("*" * 50)
                print('LISTADO DE AUTORES'.center(50))
                print("*" * 50)
                core_autor.ABMAutor.listar_autor()
                print("*" * 50)
            elif opcion == 3:
                print("*" * 50)
                print('BAJA AUTOR'.center(50))
                print("*" * 50)
                id_autor = int(input('Ingrese el id del autor: '))
                core_autor.ABMAutor.borrar_autor(id_autor)
                print("*" * 50)
            elif opcion == 4:
                print("*" * 50)
                print('MODIFICAR DATOS DE AUTOR'.center(50))
                print("*" * 50)
                id_autor = int(input('Ingrese el id del autor: '))
                core_autor.ABMAutor.buscar_autor(id_autor)
                nombre_autor = input('Nombre: ')
                apellido_autor = input('Apellido: ')
                anio_nacimiento = int(input('Año de nacimiento: '))
                nacionalidad = input('País de origen: ')
                print("*" * 50)
                autor1 = Autor(nombre_autor, apellido_autor, 0, 0, None, None, anio_nacimiento, nacionalidad)
                core_autor.ABMAutor.modificar_autor(autor1, id_autor)
                print("*" * 50)
            elif opcion < 0 or opcion > 5:
                print("Opción inválida. Por favor, elige una opción válida.")
        except Exception as e:
            print(f'Ocurrio un error de tipo: {e}')
            opcion = None
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
    else:
        print(f'Volviendo al menu principal...')
