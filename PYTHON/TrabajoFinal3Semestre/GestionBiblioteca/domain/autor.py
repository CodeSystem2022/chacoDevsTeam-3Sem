from GestionBiblioteca.domain.persona import Persona


class Autor(Persona):
    def __init__(self, nombre=None, apellido=None, dni=0, celular=0, domicilio=None, email=None, libros_publicados=None,
                 libros_escritos=None):
        super().__init__(nombre, apellido, dni, celular, domicilio, email)
        self._libros_publicados = libros_publicados
        self._libros_escritos = libros_escritos

    def _str_(self):
        return f'Autor [ Datos: nombre: {super().nombre} apellido: {super().apellido} ' \
               f'Libros Publicados: {self._libros_publicados} ' \
               f'Libros Escritos: {self._libros_escritos}] '

    @property
    def libros_publicados(self):
        return self._libros_publicados

    @libros_publicados.setter
    def libros_publicados(self, libros_publicados):
        self._libros_publicados = libros_publicados

    @property
    def libros_escritos(self):
        return self._libros_escritos

    @libros_escritos.setter
    def libros_escritos(self, libros_escritos):
        self._libros_escritos = libros_escritos
