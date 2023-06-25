<p align="center">
    <img width="100%" src="https://user-images.githubusercontent.com/70241433/233533920-47091762-ed02-441c-bcb9-02b0112a2dc4.gif"> 
</p>

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


