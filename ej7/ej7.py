class Polinomio:
    def __init__(self, coeficientes):
        # coeficientes es una lista de los coeficientes del polinomio en orden descendente
        self.coeficientes = coeficientes

    def __str__(self):
        # convertir el polinomio a una cadena de caracteres
        s = ''
        for i in range(len(self.coeficientes)-1, -1, -1):
            if self.coeficientes[i] != 0:
                s += str(self.coeficientes[i]) + 'x^' + str(i) + ' + '
        # quitar el último '+'
        return s[:-3]

    def restar(self, otro):
        # restar otro polinomio al polinomio actual
        n = len(self.coeficientes)
        m = len(otro.coeficientes)
        coeficientes = []
        for i in range(max(n, m)):
            c1 = self.coeficientes[i] if i < n else 0
            c2 = otro.coeficientes[i] if i < m else 0
            coeficientes.append(c1 - c2)
        return Polinomio(coeficientes)

    def dividir(self, otro):
        # dividir el polinomio actual por otro polinomio
        n = len(self.coeficientes)
        m = len(otro.coeficientes)
        if m > n:
            return Polinomio([0])
        coeficientes = [0] * (n - m + 1)
        for i in range(n-m, -1, -1):
            coeficientes[i] = self.coeficientes[m+i-1] / otro.coeficientes[m-1]
            for j in range(m):
                self.coeficientes[i+j] -= coeficientes[i] * otro.coeficientes[j]
        return Polinomio(coeficientes)

    def eliminar_termino(self, grado):
        # eliminar un término del polinomio
        if grado >= len(self.coeficientes):
            return self
        coeficientes = self.coeficientes.copy()
        coeficientes[grado] = 0
        return Polinomio(coeficientes)

    def existe_termino(self, grado):
        # determinar si un término existe en el polinomio
        return grado < len(self.coeficientes) and self.coeficientes[grado] != 0

p1 = Polinomio([2, 0, 1, 3])
p2 = Polinomio([1, 2, 0, 4, 5])

print('p1 =', p1)
print('p2 =', p2)

# restar p2 de p1
p3 = p1.restar(p2)
print('p1 - p2 =', p3)

# dividir p1 por p2
p4 = p1.dividir(p2)
print('p1 / p2 =', p4)

# eliminar el término de grado 2 de p1
p5 = p1.eliminar_termino(2)
print('p1 sin el término de grado 2 =', p5)
 