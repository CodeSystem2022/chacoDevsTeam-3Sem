import datetime


def obtener_fecha_hoy():
    fecha_actual = datetime.date.today()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
    return fecha_formateada
