<p align="center">
    <img width="100%" src="https://user-images.githubusercontent.com/70241433/233533920-47091762-ed02-441c-bcb9-02b0112a2dc4.gif"> 
</p>


# **Integrantes**

:godmode:Balbuena, Fernando Nicolas 

:godmode:Espinola, Renzo Oscar    

:godmode:Giménez Ríos, Tatiana T.  

:godmode:Gutiérrez, Juana Natalia   

:godmode:Gutiérrez, Alejo Hernán 

:godmode:Gutiérrez, Juan Carlos 

:godmode:Gutiérrez, René Agustín

:godmode:Iván, Matías 

:godmode:Valdez, Carlos Federico

:godmode:Valladares, Juan Ignacio  


# **Proyecto Integrador Gestion Biblioteca**

Se acordo con el equipo a desarrollar otro tipo de aplicación  por la cual se opto  por un sistema de gestion de Biblioteca, donde podriamos explayar los conocimientos adquiridos en el transcurso del semestre.

# Estructura:

## Clases de dominio:

### Persona:

#### Constructor:

__init__(self, nombre=None, apellido=None, dni=0, celular=0, domicilio=None, email=None): Este es el constructor de la clase Persona. Permite crear una instancia de Persona con los siguientes parámetros opcionales:
nombre (str): Nombre de la persona.
apellido (str): Apellido de la persona.
dni (int): DNI de la persona.
celular (int): Número de celular de la persona.
domicilio (str): Domicilio de la persona.
email (str): Dirección de correo electrónico de la persona.

#### Métodos:

__str__(self): Devuelve una representación en forma de cadena de la instancia de Persona. La cadena contiene los datos de la persona, incluyendo nombre, apellido, celular, domicilio y email.

#### Propiedades y setters:

nombre: Propiedad que permite acceder al nombre de la persona. Se puede obtener su valor con persona.nombre y modificar con persona.nombre = nuevo_nombre.

dni: Propiedad que permite acceder al DNI de la persona. Se puede obtener su valor con persona.dni y modificar con persona.dni = nuevo_dni.

apellido: Propiedad que permite acceder al apellido de la persona. Se puede obtener su valor con persona.apellido y modificar con persona.apellido = nuevo_apellido.

celular: Propiedad que permite acceder al número de celular de la persona. Se puede obtener su valor con persona.celular y modificar con persona.celular = nuevo_celular.

domicilio: Propiedad que permite acceder al domicilio de la persona. Se puede obtener su valor con persona.domicilio y modificar con persona.domicilio = nuevo_domicilio.

email: Propiedad que permite acceder al email de la persona. Se puede obtener su valor con persona.email y modificar con persona.email = nuevo_email.

Estos métodos y propiedades permiten acceder y modificar los atributos de la instancia de Persona de manera controlada.

### Socio:

#### Atributos:

_id_socio: Identificador único del socio.
_fecha_alta: Fecha de alta del socio.
_libros_prestados: Cantidad de libros prestados por el socio.

#### Constructor 

__init__(self, fecha_alta, libros_prestados, nombre, apellido, dni, celular, domicilio, email): Constructor de la clase Socio que recibe los siguientes parámetros:

fecha_alta: Fecha de alta del socio.
libros_prestados: Cantidad de libros prestados por el socio.
nombre: Nombre del socio.
apellido: Apellido del socio.
dni: DNI del socio.
celular: Número de celular del socio.
domicilio: Domicilio del socio.
email: Dirección de correo electrónico del socio.

#### Métodos:

__str__(self): Devuelve una representación en forma de cadena del objeto Socio. La cadena contiene el ID del socio, la fecha de alta y los datos personales heredados de la clase Persona.

##### Propiedades y setters:

id_socio: Propiedad que permite acceder al ID del socio. Se puede obtener su valor con socio.id_socio y modificar con socio.id_socio = nuevo_id.

fecha_alta: Propiedad que permite acceder a la fecha de alta del socio. Se puede obtener su valor con socio.fecha_alta y modificar con socio.fecha_alta = nueva_fecha.

libros_prestados: Propiedad que permite acceder a la cantidad de libros prestados por el socio. Se puede obtener su valor con socio.libros_prestados y modificar con socio.libros_prestados = nueva_cantidad.

La clase Socio hereda de la clase Persona y agrega atributos y métodos específicos para representar a un socio en el contexto de una biblioteca.

### Autor:

#### Atributos:

_anio_nacimiento: Año de nacimiento del autor.
_nacionalidad: Nacionalidad del autor.

#### Constructor
__init__(self, nombre=None, apellido=None, dni=0, celular=0, domicilio=None, email=None, anio_nacimiento=None, nacionalidad=None): Constructor de la clase Autor que recibe los siguientes parámetros:

nombre: Nombre del autor.
apellido: Apellido del autor.
dni: DNI del autor.
celular: Número de celular del autor.
domicilio: Domicilio del autor.
email: Dirección de correo electrónico del autor.
anio_nacimiento: Año de nacimiento del autor.
nacionalidad: Nacionalidad del autor.

#### Métodos:

__str__(self): Devuelve una representación en forma de cadena del objeto Autor. La cadena contiene los datos personales del autor heredados de la clase Persona, el año de nacimiento y la nacionalidad.

#### Propiedades y setters:

anio_nacimiento: Propiedad que permite acceder al año de nacimiento del autor. Se puede obtener su valor con autor.anio_nacimiento y modificar con autor.anio_nacimiento = nuevo_anio.
nacionalidad: Propiedad que permite acceder a la nacionalidad del autor. Se puede obtener su valor con autor.nacionalidad y modificar con autor.nacionalidad = nueva_nacionalidad.
La clase Autor hereda de la clase Persona y agrega atributos y métodos específicos para representar a un autor en el contexto de una biblioteca.

### Libro:

#### Atributos:

_titulo: Título del libro.
_genero: Género del libro.
_anio_publicacion: Año de publicación del libro.
_isbn: ISBN del libro.
_autor_id: ID del autor del libro.
_cantidad: Cantidad de ejemplares disponibles del libro.
_editorial: Editorial del libro.

### Constructor 

__init__(self, titulo, genero, anio_publicacion, isbn, autor_id, cantidad, editorial): Constructor de la clase Libro que recibe los siguientes parámetros:

titulo: Título del libro.
genero: Género del libro.
anio_publicacion: Año de publicación del libro.
isbn: ISBN del libro.
autor_id: ID del autor del libro.
cantidad: Cantidad de ejemplares disponibles del libro.
editorial: Editorial del libro.

#### Métodos:

__str__(self): Devuelve una representación en forma de cadena del objeto Libro. La cadena contiene el título, autor, género, año de publicación, cantidad de ejemplares, ISBN y editorial del libro.

#### Propiedades y setters:

editorial: Propiedad que permite acceder a la editorial del libro. Se puede obtener su valor con libro.editorial y modificar con libro.editorial = nueva_editorial.
titulo: Propiedad que permite acceder al título del libro. Se puede obtener su valor con libro.titulo y modificar con libro.titulo = nuevo_titulo.
genero: Propiedad que permite acceder al género del libro. Se puede obtener su valor con libro.genero y modificar con libro.genero = nuevo_genero.
autor_id: Propiedad que permite acceder al ID del autor del libro. Se puede obtener su valor con libro.autor_id y modificar con libro.autor_id = nuevo_id.
anio_publicacion: Propiedad que permite acceder al año de publicación del libro. Se puede obtener su valor con libro.anio_publicacion y modificar con libro.anio_publicacion = nuevo_anio.
isbn: Propiedad que permite acceder al ISBN del libro. Se puede obtener su valor con libro.isbn y modificar con libro.isbn = nuevo_isbn.
cantidad: Propiedad que permite acceder a la cantidad de ejemplares disponibles del libro. Se puede obtener su valor con libro.cantidad y modificar con libro.cantidad = nueva_cantidad.
La clase Libro representa un libro en el contexto de una biblioteca y proporciona métodos y propiedades para acceder y modificar sus atributos.

### Solicitud:

#### Atributos:

_libro_id: ID del libro asociado a la solicitud.
_socio_id: ID del socio asociado a la solicitud.
_fecha_solicitud: Fecha de la solicitud.
_estado: Estado de la solicitud.

#### Constructor 
__init__(self, libro_id, socio_id, fecha_solicitud, estado): Constructor de la clase Solicitud que recibe los siguientes parámetros:

libro_id: ID del libro asociado a la solicitud.
socio_id: ID del socio asociado a la solicitud.
fecha_solicitud: Fecha de la solicitud.
estado: Estado de la solicitud.

#### Propiedades y setters:

libro_id: Propiedad que permite acceder al ID del libro asociado a la solicitud. Se puede obtener su valor con solicitud.libro_id y modificar con solicitud.libro_id = nuevo_id.
socio_id: Propiedad que permite acceder al ID del socio asociado a la solicitud. Se puede obtener su valor con solicitud.socio_id y modificar con solicitud.socio_id = nuevo_id.
fecha_solicitud: Propiedad que permite acceder a la fecha de la solicitud. Se puede obtener su valor con solicitud.fecha_solicitud y modificar con solicitud.fecha_solicitud = nueva_fecha.
estado: Propiedad que permite acceder al estado de la solicitud. Se puede obtener su valor con solicitud.estado y modificar con solicitud.estado = nuevo_estado.
La clase Solicitud representa una solicitud realizada por un socio para el préstamo de un libro. Permite acceder y modificar los atributos asociados a la solicitud.

## Clases de core:

### core_autor.py

Metodos:

nuevo_autor(cls, autor): Este método estático permite insertar un nuevo autor en la base de datos. Toma un objeto Autor como argumento, que contiene los datos del autor a insertar. Realiza la conexión a la base de datos, ejecuta una sentencia INSERT y guarda el número de registros insertados. También registra un mensaje en el archivo de log en caso de éxito o error.

buscar_autor(cls, id_autor): Este método estático busca un autor en la base de datos por su ID. Toma el ID del autor como argumento y devuelve el registro del autor encontrado. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene el primer registro coincidente. Si ocurre un error, registra un mensaje en el archivo de log.

buscar_autor_por_nombre(cls, autor): Este método estático busca un autor en la base de datos por su nombre. Toma el nombre del autor como argumento y devuelve el ID del autor encontrado. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT con una cláusula LIKE y obtiene el primer registro coincidente. Si ocurre un error, registra un mensaje en el archivo de log.

buscar_autor_por_apellido(cls, autor): Este método estático busca un autor en la base de datos por su apellido. Toma el apellido del autor como argumento y devuelve el ID del autor encontrado. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT con una cláusula LIKE y obtiene el primer registro coincidente. Si ocurre un error, registra un mensaje en el archivo de log.

listar_autor(cls): Este método estático lista todos los autores en la base de datos. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene todos los registros. Si hay registros, los muestra en la consola. Si no hay registros, muestra un mensaje indicando que no existen registros cargados. Si ocurre un error, registra un mensaje en el archivo de log.

borrar_autor(cls, id_autor): Este método estático borra un autor de la base de datos por su ID. Toma el ID del autor como argumento, realiza la conexión a la base de datos, ejecuta una sentencia DELETE y guarda el número de registros eliminados. También registra un mensaje en el archivo de log en caso de éxito o error.

modificar_autor(cls, autor, id_autor): Este método estático modifica los datos de un autor en la base de datos. Toma un objeto Autor con los nuevos datos del autor y el ID del autor a modificar. Realiza la conexión a la base de datos, ejecuta una sentencia UPDATE y guarda el número de registros actualizados. También registra un mensaje en el archivo de log en caso de éxito o error.

### core_libro.py

Métodos:

nuevo_libro(cls, libro): Este método estático permite insertar un nuevo libro en la base de datos. Toma un objeto libro como argumento, que contiene los datos del libro a insertar. Realiza la conexión a la base de datos, ejecuta una sentencia INSERT y guarda el número de registros insertados. También muestra por consola los registros insertados y registra un mensaje en el archivo de log en caso de éxito o error.

buscar_libro(cls, id_libro): Este método estático busca un libro en la base de datos por su ID. Toma el ID del libro como argumento y muestra por consola los registros encontrados. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene el primer registro coincidente. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

listar_libros(cls): Este método estático lista todos los libros en la base de datos. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene todos los registros. Si hay registros, muestra por consola los detalles de cada libro. Si no hay registros, muestra un mensaje indicando que no existen registros cargados. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

borrar_libro(cls, id_libro): Este método estático elimina un libro de la base de datos por su ID. Toma el ID del libro como argumento, realiza la conexión a la base de datos, ejecuta una sentencia DELETE y guarda el número de registros eliminados. También muestra por consola los registros eliminados y registra un mensaje en el archivo de log en caso de éxito o error.

modificar_libro(cls, libro, id_libro): Este método estático modifica los datos de un libro en la base de datos. Toma un objeto libro con los nuevos datos del libro y el ID del libro a modificar. Realiza la conexión a la base de datos, ejecuta una sentencia UPDATE y guarda el número de registros actualizados. También muestra por consola los registros actualizados y registra un mensaje en el archivo de log en caso de éxito o error.

agregar_libro_existente(cls, cantidad, id_libro): Este método estático permite agregar más ejemplares a un libro existente en la base de datos. Toma la cantidad a agregar y el ID del libro como argumentos. Realiza la conexión a la base de datos, ejecuta una sentencia UPDATE y guarda el número de registros actualizados. También muestra por consola los registros actualizados y registra un mensaje en el archivo de log en caso de éxito o error.

buscar_libro_por_titulo(cls, titulo): Este método estático busca un libro en la base de datos por su título. Toma el título del libro como argumento y ejecuta una sentencia SELECT con una cláusula LIKE. Devuelve el ID del libro encontrado o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_id_libro_por_id(cls, titulo): Este método estático busca un libro en la base de datos por su ID. Toma el ID del libro como argumento y ejecuta una sentencia SELECT. Devuelve el ID del libro encontrado o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_libro_por_isbn(cls, isbn): Este método estático busca un libro en la base de datos por su ISBN. Toma el ISBN del libro como argumento y ejecuta una sentencia SELECT con una cláusula LIKE. Devuelve el ID del libro encontrado o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_cantidad_libro_por_isbn(cls, isbn): Este método estático busca la cantidad de ejemplares de un libro en la base de datos por su ISBN. Toma el ISBN del libro como argumento y ejecuta una sentencia SELECT. Devuelve la cantidad de ejemplares encontrados o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_cantidad_libro_por_id(cls, id_libro): Este método estático busca la cantidad de ejemplares de un libro en la base de datos por su ID. Toma el ID del libro como argumento y ejecuta una sentencia SELECT. Devuelve la cantidad de ejemplares encontrados o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

### core_socio:

Métodos:

nuevo_socio(cls, socio): Este método estático permite insertar un nuevo socio en la base de datos. Toma un objeto socio como argumento, que contiene los datos del socio a insertar. Realiza la conexión a la base de datos, ejecuta una sentencia INSERT y guarda el número de registros insertados. También muestra por consola los registros insertados y registra un mensaje en el archivo de log en caso de éxito o error.

buscar_socio(cls, id_socio): Este método estático busca un socio en la base de datos por su ID. Toma el ID del socio como argumento y muestra por consola los registros encontrados. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene el primer registro coincidente. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_socio_por_nombre(cls, socio): Este método estático busca un socio en la base de datos por su nombre. Toma el nombre del socio como argumento y ejecuta una sentencia SELECT con una cláusula LIKE. Devuelve el ID del socio encontrado o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_socio_por_apellido(cls, socio): Este método estático busca un socio en la base de datos por su apellido. Toma el apellido del socio como argumento y ejecuta una sentencia SELECT con una cláusula LIKE. Devuelve el ID del socio encontrado o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

buscar_socio_por_id(cls, socio): Este método estático busca un socio en la base de datos por su ID. Toma el ID del socio como argumento y ejecuta una sentencia SELECT. Devuelve el ID del socio encontrado o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

listar_socios(cls): Este método estático lista todos los socios en la base de datos. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene todos los registros. Si hay registros, muestra por consola los detalles de cada socio. Si no hay registros, muestra un mensaje indicando que no existen registros cargados. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

borrar_socio(cls, id_socio): Este método estático elimina un socio de la base de datos por su ID. Toma el ID del socio como argumento, realiza la conexión a la base de datos, ejecuta una sentencia DELETE y guarda el número de registros eliminados. También muestra por consola los registros eliminados y registra un mensaje en el archivo de log en caso de éxito o error.

modificar_socio(cls, socio, id_socio): Este método estático modifica los datos de un socio en la base de datos por su ID. Toma un objeto socio con los nuevos datos y el ID del socio a modificar. Realiza la conexión a la base de datos, ejecuta una sentencia UPDATE y guarda el número de registros actualizados. También muestra por consola los registros actualizados y registra un mensaje en el archivo de log en caso de éxito o error.

### core_solicitud:

Métodos:

nueva_solicitud(cls, solicitud): Este método estático permite insertar una nueva solicitud de libro en la base de datos. Toma un objeto solicitud como argumento, que contiene los datos de la solicitud a insertar. Realiza la conexión a la base de datos, ejecuta una sentencia INSERT y guarda el número de registros insertados. También muestra por consola los registros insertados y registra un mensaje en el archivo de log en caso de éxito o error.

listar_solicitudes(cls): Este método estático lista todas las solicitudes de libros en la base de datos que no han sido devueltas. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene los registros correspondientes. Si hay registros, muestra por consola los detalles de cada solicitud. Si no hay registros, muestra un mensaje indicando que no existen registros cargados. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

listar_solicitudes_por_id(cls, id_socio, id_libro): Este método estático lista las solicitudes de libros en la base de datos de un socio específico y un libro específico que no ha sido devuelto. Toma el ID del socio y el ID del libro como argumentos y ejecuta una sentencia SELECT con una cláusula WHERE. Devuelve el ID de la solicitud encontrada o None si no se encontró ningún registro. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

listar_devolucion(cls): Este método estático lista todas las solicitudes de libros en la base de datos que han sido devueltas. Realiza la conexión a la base de datos, ejecuta una sentencia SELECT y obtiene los registros correspondientes. Si hay registros, muestra por consola los detalles de cada solicitud. Si no hay registros, muestra un mensaje indicando que no existen registros cargados. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

listar_devolucion_socio(cls, socio_id): Este método estático lista las solicitudes de libros en la base de datos que han sido devueltas por un socio específico. Toma el ID del socio como argumento y ejecuta una sentencia SELECT con una cláusula WHERE. Muestra por consola los detalles de cada solicitud devuelta por el socio. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

listar_solicitud_socio(cls, socio_id): Este método estático lista las solicitudes de libros en la base de datos que aún no han sido devueltas por un socio específico. Toma el ID del socio como argumento y ejecuta una sentencia SELECT con una cláusula WHERE. Si hay registros, muestra por consola los detalles de cada solicitud. Si no hay registros, muestra un mensaje indicando que no existen registros cargados. Si ocurre un error, muestra un mensaje por consola y registra un mensaje en el archivo de log.

## Clases de service:

### service_autor:

La clase service_autor proporciona un servicio para interactuar con la entidad "Autor" a través de un menú de opciones. Importa los módulos necesarios y utiliza la funcionalidad proporcionada por el módulo core_autor para realizar operaciones en la base de datos.

Métodos:

service_autor(): Este método es el punto de entrada del servicio. Muestra un menú de opciones y permite al usuario seleccionar una opción. El ciclo se repite hasta que el usuario seleccione la opción de salida (opción 5). Dentro del ciclo, se captura la opción del usuario y se ejecuta el código correspondiente a cada opción.

Opción 1: NUEVO AUTOR: Permite al usuario ingresar los datos de un nuevo autor y crea un objeto Autor con esos datos. Luego, llama al método core_autor.ABMAutor.nuevo_autor() para insertar el autor en la base de datos. Muestra por consola el autor creado.

Opción 2: LISTADO DE AUTORES: Muestra por consola el listado de todos los autores en la base de datos utilizando el método core_autor.ABMAutor.listar_autor().

Opción 3: BAJA AUTOR: Permite al usuario ingresar el ID de un autor y llama al método core_autor.ABMAutor.borrar_autor() para eliminar ese autor de la base de datos.

Opción 4: MODIFICAR DATOS DE AUTOR: Permite al usuario ingresar el ID de un autor y muestra los datos actuales del autor. Luego, permite al usuario ingresar los nuevos datos del autor y crea un objeto Autor con esos datos. Llama al método core_autor.ABMAutor.modificar_autor() para actualizar los datos del autor en la base de datos.

Opción inválida: Si el usuario ingresa una opción inválida, muestra un mensaje de error.

Si ocurre una excepción durante la ejecución del código, se captura la excepción, se muestra un mensaje de error y se registra un mensaje en el archivo de log utilizando logger_base.log.error().

El servicio continúa ejecutándose hasta que el usuario selecciona la opción de salida (opción 5), momento en el cual se muestra un mensaje indicando que se está volviendo al menú principal.

### service_libro:

Crear un nuevo libro: Esta opción permite al usuario ingresar los datos de un nuevo libro, como ISBN, título, género, año de publicación, cantidad de copias y editorial. Además, se solicita al usuario que ingrese información sobre el autor del libro, ya sea por nombre, apellido o ID. Si el libro ya existe en la base de datos (se verifica mediante el ISBN), se muestra un mensaje de error.

Listar libros existentes: Esta opción muestra una lista de todos los libros existentes en la base de datos.

Eliminar un libro: El usuario puede seleccionar esta opción e ingresar el ID del libro que desea eliminar. El libro correspondiente se elimina de la base de datos.

Modificar los datos de un libro: Esta opción permite al usuario ingresar el ID del libro que desea modificar. Luego se le solicita que ingrese los nuevos datos del libro, como título, género, editorial y detalles del autor. Una vez ingresados los nuevos datos, se realiza la modificación en la base de datos.

Agregar copias a un libro existente: Si el usuario selecciona esta opción, se le solicita el ISBN del libro al que desea agregar copias. Si el libro existe en la base de datos, se solicita al usuario que ingrese la cantidad de copias que desea agregar. Luego se actualiza la cantidad de copias en la base de datos.

Volver al menú principal: Esta opción permite al usuario regresar al menú principal.

La clase service_libro utiliza varios módulos y clases para llevar a cabo estas operaciones, como el módulo config, los módulos core_libro y core_autor, la clase Libro del módulo domain.libro, y los módulos ui.mostrar_menu_libro y ui.mostrar_menu_principal_abm1.

En caso de que ocurra un error durante la ejecución de alguna operación, se captura la excepción y se muestra un mensaje de error, además de guardar el registro de error en un archivo de registro utilizando la clase logger_base del módulo config.

### service_socio:

Crear un nuevo socio: Esta opción permite al usuario ingresar los datos de un nuevo socio, como nombre, apellido, DNI, celular, domicilio y correo electrónico. Además, se genera la fecha actual utilizando la función obtener_fecha_hoy del módulo date_utils. Luego se crea una instancia de la clase Socio con los datos ingresados y se llama al método nuevo_socio de la clase ABMSocio del módulo core_socio para agregar al socio a la base de datos.

Listar socios existentes: Esta opción muestra un listado de todos los socios existentes en la base de datos utilizando el método listar_socios de la clase ABMSocio del módulo core_socio.

Eliminar un socio: El usuario puede seleccionar esta opción e ingresar el ID del socio que desea eliminar. Se llama al método borrar_socio de la clase ABMSocio del módulo core_socio para eliminar al socio correspondiente de la base de datos.

Modificar los datos de un socio: Esta opción permite al usuario ingresar el ID del socio que desea modificar. Se llama al método buscar_socio de la clase ABMSocio del módulo core_socio para buscar al socio correspondiente en la base de datos. Luego se solicita al usuario que ingrese los nuevos datos del socio, como nombre, apellido, DNI, celular, domicilio y correo electrónico. Se crea una instancia de la clase Socio con los nuevos datos y se llama al método modificar_socio de la clase ABMSocio del módulo core_socio para actualizar los datos del socio en la base de datos.

Volver al menú principal: Esta opción permite al usuario regresar al menú principal.

La clase service_socio utiliza varios módulos y clases para llevar a cabo estas operaciones, como el módulo config, el módulo core_socio, la clase Socio del módulo domain.socio, el módulo date_utils y el módulo ui.

En caso de que ocurra un error durante la ejecución de alguna operación, se captura la excepción y se muestra un mensaje de error. Además, se registra el error utilizando la clase logger_base del módulo config.

### service_solicitud:

El servicio se organiza en la clase SolicitudService.

La clase SolicitudService contiene dos métodos principales: service_solicitud_alta y service_devolucion_alta, que se encargan de gestionar el registro de solicitudes de libros y devoluciones de libros, respectivamente.

El método service_solicitud_alta permite registrar una solicitud de libro. Dentro del método, se muestra un menú con las siguientes opciones:

Registrar una solicitud de un libro
Listar Solicitudes
Volver
El usuario puede elegir una opción ingresando el número correspondiente. Si elige la opción 1, se realiza lo siguiente:

Se solicita al usuario que busque un libro mediante la función buscar_libro.
Si se encuentra el libro, se verifica la cantidad disponible.
Si hay disponibilidad, se solicita al usuario que busque un socio mediante la función buscar_socio.
Si se encuentra el socio, se crea una instancia de la clase Solicitud con los datos del libro, socio, fecha actual y estado "NO_DEVUELTO".
Se registra la solicitud llamando al método nueva_solicitud de la clase ABMSolicitud del módulo core_solicitud.
Se actualiza la cantidad de libros disponibles restando 1 mediante el método agregar_libro_existente de la clase ABMLibro del módulo core_libro.
Si no hay disponibilidad del libro o se producen errores durante el proceso, se muestra un mensaje correspondiente.

Si el usuario elige la opción 2 del menú, se muestra otro menú con las siguientes opciones:

Listar por socio
Listar general
Volver
El usuario puede elegir una opción ingresando el número correspondiente. Si elige la opción 1, se solicita al usuario que busque un socio mediante la función buscar_socio. Si se encuentra el socio, se muestra el historial de solicitudes del socio utilizando el método listar_solicitud_socio de la clase ABMSolicitud del módulo core_solicitud. Si elige la opción 2, se muestra el historial general de solicitudes utilizando el método listar_solicitudes del mismo módulo.

El método service_devolucion_alta permite registrar una devolución de libro. Similar al método anterior, se muestra un menú con las siguientes opciones:

Registrar una devolución de un libro
Listar devoluciones
Volver
Si el usuario elige la opción 1, se realiza lo siguiente:

Se solicita al usuario que busque un socio mediante la función buscar_socio.
Se solicita al usuario que busque un libro mediante la función buscar_libro.
Se muestra el historial de solicitudes de ese libro y socio utilizando el método listar_solicitudes_por_id de la clase ABMSolicitud del módulo core_solicitud.
Si se encuentra el libro y el socio, se crea una instancia de la clase Solicitud con los datos del libro, socio, fecha actual y estado "DEVUELTO".
Se registra la devolución llamando al método nueva_solicitud de la clase ABMSolicitud del módulo core_solicitud.
Se actualiza la cantidad de libros disponibles sumando 1 mediante el método agregar_libro_existente de la clase ABMLibro del módulo core_libro.
Al igual que antes, se manejan las situaciones en las que no se encuentre el libro, el socio o se produzcan errores.

## Clases de config

### database_manager:

Atributos de clase:

_DATABASE, _USERNAME, _PASSWORD, _DB_PORT, _HOST: Estos atributos almacenan los valores necesarios para establecer la conexión con la base de datos PostgreSQL.
_CONEXION, _CURSOR: Estos atributos son utilizados para almacenar la conexión y el cursor a la base de datos, respectivamente.
Método de clase crear_basedatos():

Este método se encarga de crear la base de datos especificada por el atributo _DATABASE.
Establece una conexión sin especificar la base de datos utilizando los valores de atributos correspondientes.
Luego, ejecuta una consulta SQL para crear la base de datos.
Finalmente, muestra un mensaje indicando que la base de datos ha sido creada y registra un log con la misma información.
Método de clase crear_tabla(nombre_tabla, columnas):

Este método se utiliza para crear una tabla en la base de datos.
Recibe el nombre de la tabla y una cadena de texto que representa las columnas de la tabla.
Utiliza los métodos obtener_conexion() y obtener_cursor() para obtener una conexión y un cursor a la base de datos.
Verifica si la tabla ya existe en la base de datos utilizando una consulta SQL.
Si la tabla no existe, ejecuta una consulta SQL para crear la tabla.
Muestra un mensaje indicando si la tabla fue creada o si ya existía y registra un log con la misma información.
Método de clase inicializar():

Este método se encarga de inicializar la base de datos y las tablas necesarias.
Crea una instancia de DatabaseManager.
Intenta crear la base de datos y las tablas de "SOCIO", "AUTOR", "LIBRO" y "SOLICITUD_LIBRO" utilizando el método crear_tabla().
Si alguna tabla ya existe, muestra un mensaje indicando que la tabla ya existe.
En caso de que ocurra alguna excepción, registra un log con la información del error.
Métodos de clase obtener_conexion() y obtener_cursor():

Estos métodos se utilizan para obtener la conexión y el cursor a la base de datos, respectivamente.
Si la conexión o el cursor aún no han sido creados, establecen una nueva conexión utilizando los atributos correspondientes.
Si la conexión o el cursor ya existen, los devuelve

### logger_base:

log.basicConfig(): Esta función configura el comportamiento de registro de la biblioteca logging. Recibe varios argumentos para personalizar la configuración:

level: Especifica el nivel de registro mínimo que se mostrará. En este caso, se establece en log.INFO, lo que significa que solo se mostrarán los mensajes de registro con un nivel igual o superior a INFO.

format: Define el formato del mensaje de registro. En este caso, se utiliza el siguiente formato: '%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s'. Este formato incluye la fecha y hora del registro, el nivel del registro, el nombre del archivo y el 

número de línea donde se realiza el registro, y el mensaje en sí.

datefmt: Especifica el formato de fecha y hora que se utilizará en el registro. En este caso, se establece en '%I:%M:%S %p', lo que indica que se utilizará un formato de 12 horas.

handlers: Define los controladores de registro que se utilizarán. En este caso, se proporcionan dos controladores:

log.FileHandler('capa_datos.log'): Este controlador guarda los registros en un archivo llamado capa_datos.log. Los registros se agregarán al final del archivo cada vez que se realice un registro.

log.StreamHandler(): Este controlador envía los registros a la corriente de salida estándar, lo que significa que se mostrarán en la consola.

En resumen, las instrucciones configuran la biblioteca de registro logging en Python para que los mensajes de registro con un nivel igual o superior a INFO se muestren en la consola y se guarden en un archivo llamado capa_datos.log. El formato del mensaje de registro incluye la fecha y hora, el nivel del registro, el nombre del archivo y el número de línea, y el mensaje en sí. El formato de fecha y hora utiliza un formato de 12 horas.

## Clase del paquete utils

### date_utils.py

La primera línea import datetime importa el módulo datetime, que proporciona clases para trabajar con fechas y horas en Python.

La función obtener_fecha_hoy() es definida sin argumentos. Esta función se encargará de obtener la fecha actual y formatearla.

La siguiente línea fecha_actual = datetime.date.today() utiliza la clase date del módulo datetime para obtener la fecha actual. datetime.date.today() devuelve un objeto date que representa la fecha actual.

Después, se utiliza fecha_actual.strftime("%d/%m/%Y") para formatear la fecha actual. strftime es un método que se utiliza para formatear una fecha en una cadena de caracteres según un formato específico. En este caso, se utiliza el formato "%d/%m/%Y", donde %d representa el día, %m representa el mes y %Y representa el año en formato de cuatro dígitos. Por lo tanto, fecha_actual.strftime("%d/%m/%Y") devuelve una cadena de caracteres que representa la fecha actual en formato "dd/mm/aaaa".

Finalmente, se retorna fecha_formateada que contiene la fecha actual formateada como resultado de la función obtener_fecha_hoy().

En resumen, este código importa el módulo datetime, define una función llamada obtener_fecha_hoy() que utiliza el módulo datetime para obtener la fecha actual y la devuelve formateada como una cadena de caracteres en el formato "dd/mm/aaaa".

## Clase del paquete enums

### estados_libros.py

La primera línea from enum import Enum importa la clase Enum del módulo enum, que proporciona una forma de definir enumerados en Python.

La clase EstadoLibro es definida utilizando la clase Enum como base. Esto significa que EstadoLibro es una subclase de Enum y se utiliza para representar un conjunto fijo de estados posibles para un libro.

Dentro de la clase EstadoLibro, se definen dos miembros del enumerado: DEVUELTO y NO_DEVUELTO. Cada miembro está asociado a un valor específico. En este caso, '1' está asociado a DEVUELTO y '2' está asociado a NO_DEVUELTO. Estos valores pueden ser cualquier tipo de datos válido en Python, no están limitados a cadenas de caracteres.

A continuación, se define un método estático llamado obtener_estado(). Los métodos estáticos se definen utilizando el decorador @staticmethod. Un método estático pertenece a la clase en lugar de a una instancia de la clase y no puede acceder a atributos de instancia.

El método obtener_estado() simplemente retorna una lista de todos los miembros del enumerado EstadoLibro utilizando list(EstadoLibro). La función list() toma un iterable (en este caso, EstadoLibro) y devuelve una lista que contiene todos los elementos del iterable. En este caso, el resultado será una lista que contiene los miembros DEVUELTO y NO_DEVUELTO.

En resumen, este código define un enumerado llamado EstadoLibro con dos miembros: DEVUELTO y NO_DEVUELTO. Luego, proporciona un método estático llamado obtener_estado() que retorna una lista con todos los miembros del enumerado

## Clase del paquete ui

### ui.py

La clase que has proporcionado no es realmente una clase en sí misma, sino una serie de funciones que imprimen menús en la consola. Cada función corresponde a un menú diferente y muestra las opciones disponibles en cada uno.

Aquí está una explicación general de cada función:

mostrar_menu_socio(): Esta función muestra un menú para la administración de socios. Imprime un encabezado con el título "ABM SOCIO" centrado y una serie de opciones numeradas para agregar, listar, eliminar y modificar socios, así como una opción para volver al menú principal.

mostrar_menu_autor(): Esta función muestra un menú para la administración de autores. Imprime un encabezado con el título "ABM AUTOR" centrado y una serie de opciones numeradas para agregar, listar, eliminar y modificar autores, así como una opción para volver al menú principal.

mostrar_menu_libro(): Esta función muestra un menú para la administración de libros. Imprime un encabezado con el título "ABM de Libro" centrado y una serie de opciones numeradas para agregar, listar, eliminar y modificar libros, así como una opción para agregar un libro existente y una opción para volver al menú principal.

mostrar_menu_principal_abm1(): Esta función muestra un menú principal que presenta las opciones de administración de socios, autores y libros. Imprime un encabezado con el título "ABM de Libro" centrado y una serie de opciones numeradas para acceder a los menús de administración correspondientes, así como una opción para volver al menú principal.

mostrar_menu_principal(): Esta función muestra el menú principal de la aplicación. Imprime un encabezado con el título "GESTION BIBLIOTECA" centrado y una serie de opciones numeradas para acceder a diferentes funcionalidades, como la administración de socios, autores y libros, así como opciones para retirar/devolver libros y salir del programa.

mostrar_menu_solicitud(): Esta función muestra un menú para la gestión de solicitudes y devoluciones de libros. Imprime un encabezado con el título "SOLICITUD/DEVOLUCION DE LIBROS" centrado y una serie de opciones numeradas para solicitar libros, devolver libros y volver al menú principal.

En resumen, estas funciones definen diferentes menús y opciones para una aplicación de gestión de biblioteca. Cada función imprime el menú correspondiente en la consola para que el usuario pueda interactuar con la aplicación seleccionando las opciones deseadas.

## Clase del paquete test

### test_gestion_biblioteca.py

En las primeras líneas, se importan diferentes módulos y clases necesarias para la ejecución del programa. Se importa ui.ui, SolicitudService de service.service_solicitud, service_autor de service.service_autor, service_socio de service.service_socio, service_libro de service.service_libro, mostrar_menu_principal y mostrar_menu_solicitud de ui.ui, y DatabaseManager de config.database_manager.

La función inicio() se define para inicializar la base de datos utilizando DatabaseManager.inicializar(). Esta función captura cualquier excepción que pueda ocurrir durante la inicialización e imprime el mensaje de error correspondiente.

La función ejecutar_opcion_abm(opcion) se define para ejecutar una opción seleccionada en el menú principal relacionada con las operaciones de administración (ABM: Alta, Baja, Modificación) de socios, autores y libros. Dependiendo de la opción seleccionada, se llama a las funciones correspondientes de los servicios (service_socio(), service_autor(), service_libro()) o se muestra un mensaje de "Volviendo al menú principal" si la opción es "4".

La función ejecutar_opcion_solicitud(opcion1) se define para ejecutar una opción seleccionada en el menú de solicitud y devolución de libros. Dependiendo de la opción seleccionada, se llama a las funciones correspondientes de SolicitudService (service_solicitud_alta(), service_devolucion_alta()) o se retorna si la opción es "3" (volver).

La función ejecutar_opcion(opcion) se define para ejecutar una opción seleccionada en el menú principal. Si la opción es "1", se muestra el menú de administración (ABM) y se solicita una opción al usuario en un bucle hasta que se seleccione la opción "4" (volver al menú principal). Si la opción es "2", se muestra el menú de solicitud y devolución de libros y se solicita una opción al usuario en un bucle hasta que se seleccione la opción "3" (volver al menú principal). Si la opción es "3", se imprime "VOLVER".

La función menu() se define para ejecutar el flujo principal del programa. Primero, se llama a inicio() para inicializar la base de datos. Luego, se muestra el menú principal y se solicita una opción al usuario en un bucle hasta que se seleccione la opción "3" (salir del programa). Dentro del bucle, se llama a ejecutar_opcion(opcion) para ejecutar la opción seleccionada y se vuelve a mostrar el menú principal.

Finalmente, se llama a menu() para iniciar la ejecución del programa y se imprime "Hasta Luego!" al finalizar.

En resumen, este código define diferentes funciones para mostrar menús de opciones y ejecutar acciones correspondientes en una aplicación de gestión de biblioteca. El programa interactúa con el usuario, mostrando los menús y solicitando opciones, y realiza las operaciones correspondientes utilizando los servicios y la base de datos.
