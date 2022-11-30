def price(Mes1, Mes2, Mes3):
    """Función que calcula el precio a pagar de cada cliente"
    Parámetros:
        -tupla: con los valores del consumo del cliente de tres meses
    Salida:
        Mes1: variable tipo float del consumo del mes uno
        Mes2: variable tipo float del consumo del mes dos
        Mes3: variable tipo float del consumo del mes tres
    """
    return (Mes1 + Mes2 + Mes3) * 0.0615


def gas2price(lista):
    """Función que convierte una lista de consumos de gas de diferentes clientes
    durante tres meses a otra lista de precios a cobrar.
    Parámetros:
        -lista: lista con tuplas del consumo de los clientes
    Salida:
        Lista con los precios a cobrar a cada cliente
    """
    lista_precios = []
    for cliente in lista:
        lista_precios.append(price(cliente[0], cliente[1], cliente[2]))
    return lista_precios


print(gas2price([(1.10, 1.50, 1.40), (1.25, 1.50, 1.30)]))
