# Generar las tablas hash
def generar_tablas_hash():
    tabla_encriptacion = {}
    tabla_desencriptacion = {}
    matriz_hash = [[0 for i in range(8)] for j in range(94)]
    for i in range(32, 126):
        for j in range(8):
            matriz_hash[i-32][j] = (i+j) % 94
    for i in range(94):
        cadena = ""
        for j in range(8):
            cadena += chr(matriz_hash[i][j] + 32)
        tabla_encriptacion[chr(i+32)] = cadena
        tabla_desencriptacion[cadena] = chr(i+32)
    return tabla_encriptacion, tabla_desencriptacion

# Encriptar un mensaje
def encriptar(mensaje, tabla_encriptacion):
    mensaje_encriptado = ""
    for caracter in mensaje:
        mensaje_encriptado += tabla_encriptacion[caracter]
    return mensaje_encriptado

# Desencriptar un mensaje
def desencriptar(mensaje_encriptado, tabla_desencriptacion):
    mensaje = ""
    for i in range(0, len(mensaje_encriptado), 8):
        cadena = mensaje_encriptado[i:i+8]
        mensaje += tabla_desencriptacion[cadena]
    return mensaje

# Ejemplo de uso
tabla_encriptacion, tabla_desencriptacion = generar_tablas_hash()
mensaje_original = "Hola, Rebelión!"
mensaje_encriptado = encriptar(mensaje_original, tabla_encriptacion)
mensaje_desencriptado = desencriptar(mensaje_encriptado, tabla_desencriptacion)
print("Mensaje original:", mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)
