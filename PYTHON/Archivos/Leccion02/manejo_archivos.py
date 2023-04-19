# Declaramos una variable
try:
    archivo = open("prueba.txt", "w") # La "W" es de Write, que significa "Escribir"
    archivo.write("Programamos con diferentes tipos de archivos, ahora en txt.\n")
    archivo.write("Con esto terminamos")
except Exception as e:
    print(e);
finally: # Siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo

# Ejercicio para saber si una variable es igual a la otra - Alejo Gutierrez
try:
    a = int(input("Digite el primer numero: "))
    b = int(input("Digite el segundo numero: "))
    if a == b: # raise nos permite acceder a una excepcion
        print("Son numeros iguales")
    resultado = a / b # Modificamos
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {type(e)}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError - Ocurrio un error: {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {type(e)}")
else:
    print("No se arrojo ninguna excepcion")
finally: # Siempre se va a ejecutar
    print("Ejecucioon de este bloque Finally")

print(f"El resultado es {resultado}")

# Recorrer Un arreglo - Juan Carlos Gutierrez
miArreglo = [1, 2, "tres", 4, "cinco"]

for elemento in miArreglo:
    try:
        print(elemento)
    except Exception as e:
        print(f"Ocurrió un error al imprimir el elemento {elemento}: {e}")