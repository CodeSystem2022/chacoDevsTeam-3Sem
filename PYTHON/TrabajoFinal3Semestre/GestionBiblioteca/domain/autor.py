from domain.persona import Persona


class Autor(Persona):
    def __init__(self, nombre=None, apellido=None, dni=0, celular=0, domicilio=None, email=None, anio_nacimiento=None,
                 nacionalidad=None):
        super().__init__(nombre, apellido, dni, celular, domicilio, email)
        self._anio_nacimiento = anio_nacimiento
        self._nacionalidad = nacionalidad

    def __str__(self):
        return f'Autor: Datos: nombre: {super().nombre} apellido: {super().apellido} ' \
               f'Año Nacimiento: {self._anio_nacimiento} ' \
               f'Nacionalidad: {self._nacionalidad} '

    @property
    def anio_nacimiento(self):
        return self._anio_nacimiento

    @anio_nacimiento.setter
    def anio_nacimiento(self, fecha_nacimiento):
        self._anio_nacimiento = fecha_nacimiento

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self,nacionalidad):
        self._nacionalidad = nacionalidad
