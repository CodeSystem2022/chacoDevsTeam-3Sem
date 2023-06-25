<p align="center">
    <img width="100%" src="https://user-images.githubusercontent.com/70241433/233533920-47091762-ed02-441c-bcb9-02b0112a2dc4.gif"> 
</p>

# **Proyecto Integrador Gestion Biblioteca**

Se acordo con el equipo a desarrollar otro tipo de aplicación por la cual se decidio a por un sistema de gestion de Biblioteca.

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

### Clse Socio:

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

