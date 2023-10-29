"""
Bien!
"""
def busqueda_binaria_elemento_duplicado(arr, objetivo, encontrar_ultimo=False):
    bajo = 0
    alto = len(arr) - 1
    resultado = -1

    while bajo <= alto:
        medio = bajo + (alto - bajo) // 2

        if arr[medio] == objetivo:
            resultado = medio
            if encontrar_ultimo:
                bajo = medio + 1  # Moverse a la derecha para encontrar la última ocurrencia
            else:
                alto = medio - 1  # Moverse a la izquierda para encontrar la primera ocurrencia
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return resultado

# Ejemplo de uso
arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6]

objetivo = 3

primera_ocurrencia = busqueda_binaria_elemento_duplicado(arr, objetivo, encontrar_ultimo=False)
ultima_ocurrencia = busqueda_binaria_elemento_duplicado(arr, objetivo, encontrar_ultimo=True)

if primera_ocurrencia != -1:
    print(f"Primera ocurrencia duplicada de {objetivo} encontrada en la posición {primera_ocurrencia}")
else:
    print(f"{objetivo} no encontrado en la lista.")

if ultima_ocurrencia != -1:
    print(f"Última ocurrencia duplicada de {objetivo} encontrada en la posición {ultima_ocurrencia}")
else:
    print(f"{objetivo} no encontrado en la lista.")
