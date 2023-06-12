from enum import Enum


class EstadoLibro(Enum):
    DEVUELTO = '1'
    NO_DEVUELTO = '2'


@staticmethod
def obtener_estado():
    return list(EstadoLibro)