from domain.persona import Persona


class Socio(Persona):
    contador_socio = 0

    def __init__(self, fecha_alta, libros_prestados, nombre, apellido, dni, celular, domicilio, email):
        super().__init__(nombre, apellido, dni, celular, domicilio, email)
        Socio.contador_socio = +1
        self._id_socio = Socio.contador_socio
        self._fecha_alta = fecha_alta
        self._libros_prestados = libros_prestados

    def __str__(self):
        return f'Socio: Alta N°: {self._id_socio} Fecha Alta: {self._fecha_alta} [ {super().__str__()}'

    @property
    def id_socio(self):
        return self._id_socio

    @id_socio.setter
    def id_socio(self, id_socio):
        self._id_socio = id_socio

    @property
    def fecha_alta(self):
        return self._fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, fecha_alta):
        self._fecha_alta = fecha_alta

    @property
    def libros_prestados(self):
        return self._libros_prestados

    @libros_prestados.setter
    def libros_prestados(self, libros_prestados):
        self._libros_prestados = libros_prestados
