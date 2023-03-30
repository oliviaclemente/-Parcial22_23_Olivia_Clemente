class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar_elemento(self, clave, valor):
        self.tabla[clave] = valor

    def obtener_elemento(self, clave):
        return self.tabla.get(clave)

    def obtener_tamanio(self):
        return len(self.tabla)

    def obtener_cadena(self):
        return str(self.tabla)


class Encriptador:
    def __init__(self):
        self.tabla_encriptacion = TablaHash()
        self.tabla_desencriptacion = TablaHash()
        self.generar_tablas_hash()

    def generar_tablas_hash(self):
        matriz_hash = [[0 for i in range(8)] for j in range(94)]
        for i in range(32, 126):
            for j in range(8):
                matriz_hash[i-32][j] = (i+j) % 94
        for i in range(94):
            cadena = ""
            for j in range(8):
                cadena += chr(matriz_hash[i][j] + 32)
            caracter = chr(i+32)
            self.tabla_encriptacion.agregar_elemento(caracter, cadena)
            self.tabla_desencriptacion.agregar_elemento(cadena, caracter)

    def encriptar(self, mensaje):
        mensaje_encriptado = ""
        for caracter in mensaje:
            cadena = self.tabla_encriptacion.obtener_elemento(caracter)
            if cadena is not None:
                mensaje_encriptado += cadena
        return mensaje_encriptado

    def desencriptar(self, mensaje_encriptado):
        mensaje = ""
        for i in range(0, len(mensaje_encriptado), 8):
            cadena = mensaje_encriptado[i:i+8]
            caracter = self.tabla_desencriptacion.obtener_elemento(cadena)
            if caracter is not None:
                mensaje += caracter
        return mensaje


# Ejemplo de uso
encriptador = Encriptador()
mensaje_original = "Hola, Rebelión!"
mensaje_encriptado = encriptador.encriptar(mensaje_original)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje original:", mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)
