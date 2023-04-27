import psycopg2  # Esto es para poder conectarnos a Postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)  # De esta manera ejecutamos la sentencia
registros = cursor.fetchall()  # Este metodo permite recuperar todos los registros de la sentencia
print(registros)

cursor.close()
conexion.close()
