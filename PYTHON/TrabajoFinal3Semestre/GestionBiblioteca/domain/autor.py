from domain.persona import Persona


class Autor(Persona):
    def __init__(self, nombre=None, apellido=None, dni=0, celular=0, domicilio=None, email=None, fecha_nacimiento=None,
                 nacionalidad=None):
        super().__init__(nombre, apellido, dni, celular, domicilio, email)
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad

    def __str__(self):
        return f'Autor: Datos: nombre: {super().nombre} apellido: {super().apellido} ' \
               f'Año Nacimiento: {self._fecha_nacimiento} ' \
               f'Nacionalidad: {self._nacionalidad} '

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self,nacionalidad):
        self._nacionalidad = nacionalidad
