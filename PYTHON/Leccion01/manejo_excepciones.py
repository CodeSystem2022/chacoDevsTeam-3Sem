from NumerosIgualesException import NumerosIgualesException
resultado = None
try:
    a = int(input('Digite el primero numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise NumerosIgualesException('Son iguales')
    resultado = a / b  # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivision - Ocurrio un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}')
else:
    print('No se arrojo ninguna excepcion')  # es opcional se ejecuta cuando no hay excepciones
finally:
    print('Ejecucion de este bloque finally')  # siempre se va a ejecutar

print(f'El resultado es: {resultado}')
print('seguimos...')
