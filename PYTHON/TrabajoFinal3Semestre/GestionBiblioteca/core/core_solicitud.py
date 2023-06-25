import config.database_manager as db
import config.logger_base as logger_base
from enums import estados_libros


class ABMSolicitud:
    MI_BD = 'gestionbiblioteca'
    TABLA = 'solicitud_libro'

    @classmethod
    def nueva_solicitud(cls, solicitud):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sentencia = f'INSERT INTO {cls.TABLA} (libro_id, socio_id, fecha_solicitud, estado) VALUES (%s, %s, %s, %s)'
                valores = (solicitud.libro_id, solicitud.socio_id, solicitud.fecha_solicitud, solicitud.estado)
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados}')
                logger_base.log.info(f'Los registros insertados son: {registros_insertados}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def listar_solicitudes(cls):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT sol.fecha_solicitud, s.nombre, l.titulo FROM {cls.TABLA} sol  JOIN libro l ON ' \
                                f'sol.libro_id = l.id_libro JOIN socio s ON sol.socio_id = s.id_socio where estado = %s '
                    cursor.execute(sentencia, estados_libros.EstadoLibro.NO_DEVUELTO.value)
                    registros = cursor.fetchall()
                    if len(registros) > 0:
                        for registro in registros:
                            fecha_solicitud = registro[0]
                            fecha_solicitud_formateada = fecha_solicitud.strftime('%d/%m/%Y')
                            nuevo_registro = (fecha_solicitud_formateada, registro[1], registro[2])
                            print(nuevo_registro)
                    else:
                        print(f'No existen registros cargados')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def listar_solicitudes_por_id(cls, id_socio, id_libro):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_solicitud, sol.fecha_solicitud, s.nombre, l.titulo FROM {cls.TABLA} sol  JOIN libro l ON ' \
                                f'sol.libro_id = l.id_libro JOIN socio s ON sol.socio_id = s.id_socio ' \
                                f'WHERE sol.socio_id = %s and sol.libro_id = %s and estado = %s '
                    cursor.execute(sentencia, (id_socio, id_libro, estados_libros.EstadoLibro.NO_DEVUELTO.value))
                    registros = cursor.fetchall()
                    id_solicitud = None
                    for registro in registros:
                        id_solicitud= registro[0]
                        fecha_solicitud = registro[1]
                        fecha_solicitud_formateada = fecha_solicitud.strftime('%d/%m/%Y')
                        nuevo_registro = (fecha_solicitud_formateada, registro[2], registro[3])
                        print(nuevo_registro)
                    return id_solicitud
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def listar_devolucion(cls):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT sol.fecha_solicitud, s.nombre, l.titulo FROM {cls.TABLA} sol  JOIN libro l ON ' \
                                f'sol.libro_id = l.id_libro JOIN socio s ON sol.socio_id = s.id_socio where estado = %s '
                    cursor.execute(sentencia, estados_libros.EstadoLibro.DEVUELTO.value)
                    registros = cursor.fetchall()
                    for registro in registros:
                        fecha_solicitud = registro[0]
                        fecha_solicitud_formateada = fecha_solicitud.strftime('%d/%m/%Y')
                        nuevo_registro = (fecha_solicitud_formateada, registro[1], registro[2])
                        print(nuevo_registro)
        except Exception as e:
            print(f'Ocurrio un error {e}')

    @classmethod
    def listar_devolucion_socio(cls, socio_id):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT sol.fecha_solicitud, s.nombre, l.titulo FROM {cls.TABLA} sol  JOIN libro l ON ' \
                                f'sol.libro_id = l.id_libro JOIN socio s ON sol.socio_id = s.id_socio WHERE estado = %s ' \
                                f'AND socio_id = %s'
                    cursor.execute(sentencia, (estados_libros.EstadoLibro.DEVUELTO.value, socio_id))
                    registros = cursor.fetchall()
                    for registro in registros:
                        fecha_solicitud = registro[0]
                        fecha_solicitud_formateada = fecha_solicitud.strftime('%d/%m/%Y')
                        nuevo_registro = (fecha_solicitud_formateada, registro[1], registro[2])
                        print(nuevo_registro)
        except Exception as e:
            print(f'Ocurrio un error {e}')

    @classmethod
    def listar_solicitud_socio(cls, socio_id):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT sol.fecha_solicitud, s.nombre, l.titulo FROM {cls.TABLA} sol  JOIN libro l ON ' \
                                f'sol.libro_id = l.id_libro JOIN socio s ON sol.socio_id = s.id_socio WHERE estado = %s ' \
                                f'AND socio_id = %s'
                    cursor.execute(sentencia, (estados_libros.EstadoLibro.NO_DEVUELTO.value, socio_id))
                    registros = cursor.fetchall()
                    if len(registros) > 0:
                        for registro in registros:
                            fecha_solicitud = registro[0]
                            fecha_solicitud_formateada = fecha_solicitud.strftime('%d/%m/%Y')
                            nuevo_registro = (fecha_solicitud_formateada, registro[1], registro[2])
                            print(nuevo_registro)
                    else:
                        print(f'No existen registros cargados')
        except Exception as e:
            print(f'Ocurrio un error {e}')