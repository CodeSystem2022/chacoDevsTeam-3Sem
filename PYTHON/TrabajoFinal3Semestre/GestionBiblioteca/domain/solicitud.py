class Solicitud:
    def __init__(self, libro_id, socio_id, fecha_solicitud, estado):
        self._libro_id = libro_id
        self._socio_id = socio_id
        self._fecha_solicitud = fecha_solicitud
        self._estado = estado

    @property
    def libro_id(self):
        return self._libro_id

    @libro_id.setter
    def libro_id(self, libro_id):
        self._libro_id = libro_id

    @property
    def socio_id(self):
        return self._socio_id

    @socio_id.setter
    def socio_id(self, socio_id):
        self._socio_id = socio_id

    @property
    def fecha_solicitud(self):
        return self._fecha_solicitud

    @fecha_solicitud.setter
    def fecha_solicitud(self, fecha_solicitud):
        self._fecha_solicitud = fecha_solicitud

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

