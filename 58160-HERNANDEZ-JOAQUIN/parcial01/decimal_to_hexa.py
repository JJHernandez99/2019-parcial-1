
def decimal_to_hexa(numero):
    diccionario = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} 
    
    numero_a = str(int(numero)%16)
    
    numero_b = str(int((int(numero)/16)%16))

    numero_c = str (int(int(numero)/(16*16)))

    if int(numero_a) > 9:
        numero_a = str(diccionario[int(numero_a)])

    if int(numero_b) > 9:
        numero_b = str(diccionario[int(numero_b)])
    
    if int(numero_c) > 9:
        numero_c = str(diccionario[int(numero_c)])
    
    numero_d = numero_c + numero_b + numero_a
 
    return numero_d

