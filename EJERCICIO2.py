prefijos = {"+30": "Grecia", "+33": "Francia", "+34": "España", "+351": "Portugal",
            "+380": "Ucrania", "+39": "Italia", "+41": "Suiza", "+44": "Reino Unido",
            "+49": "Alemania", "+7": "Rusia"}

def check_phone_number(numero):
    """"Función que comprueba que el número de teléfono es correcto en longitud
    y si el primer dígito es seis.
    Parámetro:
        -numero: número de teléfono a comprobar
    Salida:
        Booleano con valor:
            -False: Si el número es incorrecto
            -True: Si el número es correcto
    """
    return int(len(numero)) == 9 and int(numero[0]) == 6


def check_phone_country(prefijo):
    """Función que consulta en el diccionario de prefijos el país de este
    Parámetros:
        -Prefijo: prefijo telefónico del número introducido
    Salida:
        Str con el nombre del país asociado al prefijo
    """
    return prefijos.get(prefijo, "No encontrado")

def phone_call(numero_tlf):
    """Función en la que separa el número telefónico en el prefijo y el número
    Parámetro:
        -numero_tlf: número de teléfono completo
    Salida:
        Dos opciones:
            -Si el número es correcto devolverá el número y el país asociado
            -Si el número es incorredcto devolverá un aviso
    """

