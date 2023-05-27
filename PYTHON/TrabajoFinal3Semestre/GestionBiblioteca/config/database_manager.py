import psycopg2
import config.logger_base as logger_base


class DatabaseManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def crear_basedatos(self):
        # Establecer conexión sin especificar la base de datos
        conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        conn.autocommit = True

        cursor = conn.cursor()
        # Crear la base de datos
        cursor.execute(f"CREATE DATABASE {self.dbname}")
        print(f"La base de datos '{self.dbname}' ha sido creada.")
        logger_base.log.info(f"La base de datos '{self.dbname}' ha sido creada.")

    def crear_tabla(self, nombre_tabla, columnas):
        # Establecer conexión con la base de datos
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        cursor = conn.cursor()
        # Verificar si la tabla ya existe
        cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (nombre_tabla,))
        existe = cursor.fetchone()[0]

        if existe:
            print(f"La tabla '{nombre_tabla}' ya existe en la base de datos '{self.dbname}'.")
        else:
            # Crear la tabla
            cursor.execute(f"CREATE TABLE {nombre_tabla} ({columnas})")
            print(f"Se creo tabla '{nombre_tabla}' en la base de datos '{self.dbname}'.")
            logger_base.log.info(f"Se creo tabla '{nombre_tabla}' en la base de datos '{self.dbname}'.")

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()


def inicializar():
    manager = DatabaseManager(dbname="gestionbiblioteca", user="postgres", password="admin", host="localhost",
                              port="5432")
    try:
        manager.crear_basedatos()
    except Exception as e:
        if str(e) == 'database "gestionbiblioteca" already exists\n':
            print("Base de datos estado: OK")
        else:
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    try:
        manager.crear_tabla(nombre_tabla="SOCIO",
                            columnas="id_socio SERIAL PRIMARY KEY, dni INT, nombre VARCHAR(50), apellido VARCHAR(50),"
                                     " celular VARCHAR(50), domicilio VARCHAR(50), email VARCHAR(50)")
    except Exception as e:
        if str(e) == 'relation "socio" already exists\n':
            print("Tabla socio estado: OK")
        else:
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    try:
        manager.crear_tabla(nombre_tabla="AUTOR",
                            columnas="id_autor SERIAL PRIMARY KEY, nombre VARCHAR(50), apellido VARCHAR(50),"
                                     " libros_publicados INT, libros_escritos VARCHAR(50) ")
    except Exception as e:
        if str(e) == 'relation "autor" already exists\n':
            print("Tabla autor estado: OK")
        else:
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
    try:
        manager.crear_tabla(nombre_tabla="LIBRO",
                            columnas="id_libro SERIAL PRIMARY KEY, titulo VARCHAR(50), genero VARCHAR(50), "
                                     "autor VARCHAR(50), anio_publicacion INT, isbn VARCHAR(50), cantidad INT,"
                                     " autor_id INT, FOREIGN KEY (autor_id) REFERENCES AUTOR (id_autor)")
    except Exception as e:
        if str(e) == 'relation "libro" already exists\n':
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
        if str(e) == 'relation "solicitud_libro" already exists\n':
            print("Tabla solicitud_libro estado: OK")
        else:
            logger_base.log.error(f'OCURRIO UN ERROR {e}')
