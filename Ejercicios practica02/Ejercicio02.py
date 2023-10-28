class Conjunto:
    def __init__(self, iterable=None):
        self.lista = []
        if iterable is not None:
            for elemento in iterable:
                self.agregar(elemento)

    def agregar(self, elemento):
        # Agrega un elemento si no existe en la lista
        if not self.contiene(elemento):
            self.lista.append(elemento)

    def eliminar(self, elemento):
        # Elimina un elemento si existe en la lista
        if self.contiene(elemento):
            i = 0
            while i < len(self.lista):
                if self.lista[i] == elemento:
                    self.lista.pop(i)
                else:
                    i += 1

    def contiene(self, elemento):
        # Verifica si un elemento está presente en la lista
        copia = list(self.lista)  # Copia la lista original
        while not self.esta_vacio():
            e = self.lista.pop()
            if e == elemento:
                self.lista = list(copia)  # Restaura la lista original
                return True
        self.lista = list(copia)  # Restaura la lista original
        return False

    def esta_vacio(self):
        # Verifica si el conjunto está vacío
        return len(self.lista) == 0

    def tamanio(self):
        # Devuelve el tamaño del conjunto
        return len(self.lista)

    def vaciar(self):
        # Vacía el conjunto (elimina todos los elementos)
        self.lista = []

    def union(self, otro_conjunto):
        # Realiza la unión de dos conjuntos
        nuevo_conjunto = Conjunto(self.lista)
        copia = list(otro_conjunto.lista)
        while not otro_conjunto.esta_vacio():
            elemento = otro_conjunto.lista.pop()
            nuevo_conjunto.agregar(elemento)
        otro_conjunto.lista = list(copia)  # Restaura la lista original
        return nuevo_conjunto

    def interseccion(self, otro_conjunto):
        # Realiza la intersección de dos conjuntos
        nuevo_conjunto = Conjunto()
        copia = list(self.lista)
        while not self.esta_vacio():
            elemento = self.lista.pop()
            if otro_conjunto.contiene(elemento):
                nuevo_conjunto.agregar(elemento)
        self.lista = list(copia)  # Restaura la lista original
        return nuevo_conjunto

    def diferencia(self, otro_conjunto):
        # Encuentra la diferencia entre dos conjuntos
        nuevo_conjunto = Conjunto(self.lista)
        copia = list(otro_conjunto.lista)
        while not otro_conjunto.esta_vacio():
            elemento = otro_conjunto.lista.pop()
            nuevo_conjunto.eliminar(elemento)
        otro_conjunto.lista = list(copia)  # Restaura la lista original
        return nuevo_conjunto

    def subconjunto(self, otro_conjunto):
        # Verifica si un conjunto es subconjunto de otro
        copia = list(self.lista)
        while not otro_conjunto.esta_vacio():
            elemento = otro_conjunto.lista.pop()
            if not self.contiene(elemento):
                self.lista = list(copia)  # Restaura la lista original
                return False
        self.lista = list(copia)  # Restaura la lista original
        return True

    def superconjunto(self, otro_conjunto):
        # Verifica si un conjunto es superconjunto de otro
        return otro_conjunto.subconjunto(self)

    def __str__(self):
        # Representación en cadena del conjunto
        return str(self.lista)

# Ejemplo de uso:
conjunto1 = Conjunto([1, 2, 3, 4, 5])
conjunto2 = Conjunto([4, 5, 6, 7, 8])

print(conjunto1)
print(conjunto2)

print("Unión:", conjunto1.union(conjunto2))
print("Intersección:", conjunto1.interseccion(conjunto2))
print("Diferencia:", conjunto1.diferencia(conjunto2))

print("¿conjunto1 es subconjunto de conjunto2?", conjunto1.subconjunto(conjunto2))
print("¿conjunto2 es superconjunto de conjunto1?", conjunto2.superconjunto(conjunto1))
