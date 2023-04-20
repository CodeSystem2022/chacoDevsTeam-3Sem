from ManejoArchivos import ManejoArchivos

# MANEJO DE CONTEXTO WITH: sintaxis simplificada, abre y cierra el archivo
with open("prueba.txt", "r", encoding="utf8") as archivo:
    print(archivo.read())
# No hace falta ni el try, ni el finally
# en el contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes métodos: __enter__ este es el que abre
# Ahora el siguiente método es el que cierra: __exit__

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())