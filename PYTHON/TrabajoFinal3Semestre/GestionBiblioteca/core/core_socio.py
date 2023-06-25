import psycopg2
import config.database_manager as db
import config.logger_base as logger_base


class ABMSocio:
    MI_BD = 'gestionbiblioteca'
    TABLA = 'socio'

    @classmethod
    def nuevo_socio(cls, socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sentencia = f'INSERT INTO {cls.TABLA} (dni, nombre, apellido, celular, domicilio, email) VALUES (%s, %s, %s, %s, %s, %s)'
                valores = (socio.dni, socio.nombre, socio.apellido, socio.celular, socio.domicilio, socio.email)
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados}')
                logger_base.log.info(f'Los registros insertados son: {registros_insertados}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_socio(cls, id_socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT * FROM {cls.TABLA} WHERE id_socio = %s'
                    cursor.execute(sentencia, (id_socio,))
                    registros = cursor.fetchone()
                    print(f' Selecciono el socio :{registros}')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_socio_por_nombre(cls, socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_socio FROM {cls.TABLA} WHERE nombre like %s'
                    cursor.execute(sentencia, (f'%{socio}%',))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_socio_por_apellido(cls, socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_socio FROM {cls.TABLA} WHERE apellido like %s'
                    cursor.execute(sentencia, (f'%{socio}%',))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_socio_por_id(cls, socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_socio FROM {cls.TABLA} WHERE id_socio = %s'
                    valores = (socio,)
                    cursor.execute(sentencia, valores)
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def listar_socios(cls):
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
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def borrar_socio(cls, id_socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'DELETE FROM {cls.TABLA} WHERE id_socio=%s'
                    valores = (id_socio,)
                    cursor.execute(sentencia, valores)
                    registros_eliminados = cursor.rowcount
                    print(f'Los registros eliminados son: {registros_eliminados}')
                    logger_base.log.info(f'Los registros eliminados son: {registros_eliminados}')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def modificar_socio(cls, socio, id_socio):
        conexion = db.DatabaseManager.obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sentencia = f'UPDATE {cls.TABLA} SET dni=%s, nombre= %s, apellido=%s, celular=%s, domicilio=%s, email=%s WHERE id_socio=%s'
                valores = (
                    socio.dni, socio.nombre, socio.apellido, socio.celular, socio.domicilio, socio.email, id_socio)
                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados}')
                logger_base.log.info(f'Los registros actualizados son: {registros_actualizados}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')