# Declaramos una variable
try:
    archivo = open("prueba.txt", "w") # La "W" es de Write, que significa "Escribir"
    archivo.write("Programamos con diferentes tipos de archivos, ahora en txt.\n")
    archivo.write("Con esto terminamos")
    archivo.write('las letras son: \nr read leer, \na append anexa, \nw write escribir,\nx excepcion crea un archivo')
    archivo.write('\nt esta es para texto o text, \nb archivos binarios, \nw+ lee y escribe son iguales a r+\n')
except Exception as e:
    print(e);
finally: # Siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo
    