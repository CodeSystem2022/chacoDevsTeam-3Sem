import config.database_manager as db
import config.logger_base as logger_base


class ABMAutor:
    MI_BD = 'gestionbiblioteca'
    TABLA = 'autor'

    @classmethod
    def nuevo_autor(cls, autor):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sentencia = f'INSERT INTO {cls.TABLA} (nombre, apellido, anio_nacimiento, nacionalidad) ' \
                            f'VALUES (%s, %s, %s, %s)'
                valores = (autor.nombre, autor.apellido, autor.anio_nacimiento, autor.nacionalidad)
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados}')
                conexion.commit()
                logger_base.log.info(f'Los registros insertados son: {registros_insertados}')
        except Exception as e:
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_autor(cls, id_autor):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT * FROM {cls.TABLA} WHERE id_autor = %s'
                    cursor.execute(sentencia, (id_autor,))
                    registros = cursor.fetchone()
                    print(registros)
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_autor_por_nombre(cls, autor):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_autor FROM {cls.TABLA} WHERE nombre like %s'
                    cursor.execute(sentencia, (f'%{autor}%',))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_autor_por_apellido(cls, autor):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_autor FROM {cls.TABLA} WHERE apellido like %s'
                    cursor.execute(sentencia, (f'%{autor}%',))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def listar_autor(cls):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT * FROM {cls.TABLA}'
                    cursor.execute(sentencia)
                    registros = cursor.fetchall()
                    if len(registros) > 0:
                        for registro in registros:
                            print(registro)
                    else:
                        print(f'No existen registros cargados')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def borrar_autor(cls, id_autor):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'DELETE FROM {cls.TABLA} WHERE id_autor=%s'
                    valores = (id_autor,)
                    cursor.execute(sentencia, valores)
                    registros_eliminados = cursor.rowcount
                    print(f'Los registros eliminados son: {registros_eliminados}')
                    logger_base.log.info(f'Los registros eliminados son: {registros_eliminados}')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def modificar_autor(cls, autor, id_autor):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sentencia = f'UPDATE {cls.TABLA} SET nombre= %s, apellido=%s, anio_nacimiento=%s, nacionalidad=%s WHERE id_autor=%s'
                valores = (
                    autor.nombre, autor.apellido, autor.anio_nacimiento, autor.nacionalidad, id_autor)
                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados}')
                logger_base.log.info(f'Los registros actualizados son: {registros_actualizados}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
