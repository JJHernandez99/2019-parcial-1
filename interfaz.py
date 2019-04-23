from decimal_to_hexa import decimal_to_hexa

def interfaz (numero):

    if not numero:
        return 'Por favor, Ingrese un numero'

    try:
        int(numero)

        if 4095 < int(numero):
            return 'Ingrese un numero menor a 4095'
        else:
            if int(numero) < 0:
                return 'Por favor,Ingrese un numero positivo'
            else:
                return decimal_to_hexa(numero)
    except:

        return 'Por favor, Ingrese un numero'