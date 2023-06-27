import psycopg2 as bd
import config.logger_base as logger_base
import sys


import psycopg2 as bd
import config.logger_base as logger_base
import sys


class DatabaseManager:
    _DATABASE = 'gestionbiblioteca'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _CONEXION = None
    _CURSOR = None

    @classmethod
    def crear_basedatos(cls):
        # Establecer conexión sin especificar la base de datos
        conn = bd.connect(host=cls._HOST,
                          user=cls._USERNAME,
                          password=cls._PASSWORD,
                          port=cls._DB_PORT)
        conn.autocommit = True

        cursor = conn.cursor();
        # Crear la base de datos
        cursor.execute(f"CREATE DATABASE {cls._DATABASE}")
        print(f"La base de datos '{cls._DATABASE}' ha sido creada.")
        logger_base.log.info(f"La base de datos '{cls._DATABASE}' ha sido creada.")

    @classmethod
    def crear_tabla(cls, nombre_tabla, columnas):
        # Establecer conexión con la base de datos
        conn = cls.obtener_conexion()
        cursor = cls.obtener_cursor()
        with conn:
            with conn.cursor() as cursor:
                # Verificar si la tabla ya existe
                cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (nombre_tabla,))
                existe = cursor.fetchone()[0]
                if existe:
                    print(f"La tabla '{nombre_tabla}' ya existe en la base de datos '{cls._DATABASE}'.")
                else:
                    # Crear la tabla
                    cursor.execute(f"CREATE TABLE {nombre_tabla} ({columnas})")
                    print(f"Se creo tabla '{nombre_tabla}' en la base de datos '{cls._DATABASE}'.")
                    logger_base.log.info(f"Se creo tabla '{nombre_tabla}' en la base de datos '{cls._DATABASE}'.")
                    conn.commit()

    @classmethod
    def inicializar(cls):
        manager = DatabaseManager()
        try:
            print('*' * 50)
            print('CONFIGURACION'.center(50))
            print('*' * 50)
            manager.crear_basedatos()
        except Exception as e:
            if str(e) == 'database "gestionbiblioteca" already exists\n' or 'la base de datos "gestionbiblioteca" ya existe\n':
                print("Base de datos estado: OK")
            else:
                logger_base.log.error(f'OCURRIO UN ERROR {e}')

        try:
            manager.crear_tabla(nombre_tabla="SOCIO",
                                columnas="id_socio SERIAL PRIMARY KEY, dni INT, nombre VARCHAR(50), apellido VARCHAR(50),"
                                         " celular VARCHAR(50), domicilio VARCHAR(50), email VARCHAR(50)")
        except Exception as e:
            if str(e) == 'relation "socio" already exists\n' or 'la relación "socio" ya existe\n':
                print("Tabla socio estado: OK")
            else:
                logger_base.log.error(f'OCURRIO UN ERROR {e}')

        try:
            manager.crear_tabla(nombre_tabla="AUTOR",
                                columnas="id_autor SERIAL PRIMARY KEY, nombre VARCHAR(50), apellido VARCHAR(50),"
                                         " anio_nacimiento INT, nacionalidad VARCHAR(50) ")
        except Exception as e:
            if str(e) == 'relation "autor" already exists\n' or 'la relación "autor" ya existe\n':
                print("Tabla autor estado: OK")
            else:
                logger_base.log.error(f'OCURRIO UN ERROR {e}')
        try:
            manager.crear_tabla(nombre_tabla="LIBRO",
                                columnas="id_libro SERIAL PRIMARY KEY, titulo VARCHAR(50), genero VARCHAR(50), "
                                         "autor VARCHAR(50), anio_publicacion INT, isbn VARCHAR(50), cantidad INT, "
                                         "editorial VARCHAR(255), autor_id INT, FOREIGN KEY (autor_id) "
                                         "REFERENCES AUTOR (id_autor)")
        except Exception as e:
            if str(e) == 'relation "libro" already exists\n' or 'la relación "libro" ya existe\n':
                print("Tabla libro estado: OK")
            else:
                logger_base.log.error(f'OCURRIO UN ERROR {e}')
        try:
            manager.crear_tabla(nombre_tabla="SOLICITUD_LIBRO",
                                columnas="id_solicitud SERIAL PRIMARY KEY, libro_id INT, "
                                         "FOREIGN KEY (libro_id) REFERENCES LIBRO (id_libro), socio_id  INT,"
                                         " FOREIGN KEY (socio_id) REFERENCES SOCIO (id_socio) ,fecha_solicitud DATE , "
                                         "estado VARCHAR(50)")
        except Exception as e:
            if str(e) == 'relation "solicitud_libro" already exists\n' or 'la relación "solicitud_libro" ya existe':
                print("Tabla solicitud_libro estado: OK")
            else:
                logger_base.log.error(f'OCURRIO UN ERROR {e}')
        print('*' * 50)

    @classmethod
    def obtener_conexion(cls):
        if cls._CONEXION is None:
            try:
                cls._CONEXION = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                logger_base.log.debug(f'Conexion exitosa: {cls._CONEXION}')
                return cls._CONEXION
            except Exception as e:
                logger_base.log.error(f'Ocurrio un error de tipo: {e}')
                sys.exit()
        else:
            return cls._CONEXION

    @classmethod
    def obtener_cursor(cls):
        if cls._CURSOR is None:
            try:
                cls._CURSOR = cls.obtener_conexion().cursor()
                logger_base.log.debug(f'Se abrio correctamente el cursor: {cls._CURSOR}')
                return cls._CURSOR
            except Exception as e:
                logger_base.log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._CURSOR
