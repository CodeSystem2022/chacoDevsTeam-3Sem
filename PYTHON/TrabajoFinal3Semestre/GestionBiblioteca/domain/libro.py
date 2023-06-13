class Libro:
    def __init__(self, titulo, genero, anio_publicacion, isbn, autor_id, cantidad, editorial):
        self._titulo = titulo
        self._genero = genero
        self._anio_publicacion = anio_publicacion
        self._isbn = isbn
        self._autor_id = autor_id
        self._cantidad = cantidad
        self._editorial = editorial

    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor_id}, Genero: {self._genero}, " \
               f"Anio Publicación: {self._anio_publicacion}, existencia: {self._cantidad} ISBN: {self._isbn} " \
               f"Editorial: {self._editorial}"

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def autor_id(self):
        return self._autor_id

    @autor_id.setter
    def autor_id(self, autor_id):
        self._autor_id = autor_id

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @anio_publicacion.setter
    def anio_publicacion(self, anio_publicacion):
        self._anio_publicacion = anio_publicacion

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad