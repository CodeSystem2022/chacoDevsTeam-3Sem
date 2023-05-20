class Persona:

    def __init__(self, nombre=None, apellido=None, dni=0, celular=0, domicilio=None, email=None):
        if dni > 0:
            self._dni = dni
            self._nombre = nombre
            self._apellido = apellido
            self._celular = celular
            self._domicilio = domicilio
            self._email = email
        else:
            self._nombre = nombre
            self._apellido = apellido

    def __str__(self):
        return f'Datos: Nombre: {self._nombre}, Apellido: {self._apellido}, Celular: {self._celular}, ' \
               f'Domicilio: {self._domicilio}, Email: {self._email}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, celular):
        self._celular = celular

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, domicilio):
        self._domicilio = domicilio

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email



