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

