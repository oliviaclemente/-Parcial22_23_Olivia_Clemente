class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("¡El alumno " + self.nombre + " se ha creado con éxito!")
    
    def calificacion(self):
        if self.nota >= 5:
            print("El alumno " + self.nombre + " ha aprobado con una nota de " + str(self.nota))
        else:
            print("El alumno " + self.nombre + " ha suspendido con una nota de " + str(self.nota))

#alumno1 = Alumno("Juan", 7)
#alumno2 = Alumno("María", 3)

#alumno1.calificacion()  # imprimirá "El alumno Juan ha aprobado con una nota de 7"
#alumno2.calificacion()  # imprimirá "El alumno María ha suspendido con una nota de 3"
