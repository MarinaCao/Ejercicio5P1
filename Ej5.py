# Solicitar al usuario que ingrese una lista de números
print("Ingrese una lista de números (ingrese un número negativo para detenerse):")

# Inicializar una lista vacía para almacenar los números ingresados por el usuario
numeros = []

# Iterar hasta que se ingrese un número negativo
while True:
    # Solicitar al usuario que ingrese un número y convertirlo a entero
    numero = int(input("Ingrese un número: "))
    
    # Verificar si el número ingresado es negativo
    if numero < 0:
        # Si es negativo, detener la iteración
        break
    
    # Agregar el número a la lista
    numeros.append(numero)

# Imprimir la lista de números ingresados antes de encontrar un número negativo
print("(Con break)La lista de números ingresados es:", numeros)
# Solicitar al usuario que ingrese una lista de números
print("Ingrese una lista de números (ingrese un número negativo para detenerse):")

# Inicializar una lista vacía para almacenar los números ingresados por el usuario
numeros = []

# Inicializar una bandera para controlar la terminación del bucle
terminado = False

# Iterar hasta que el usuario ingrese un número negativo o marque que ha terminado
while not terminado:
    # Solicitar al usuario que ingrese un número y convertirlo a entero
    numero = int(input("Ingrese un número: "))
    
    # Verificar si el número ingresado es negativo
    if numero < 0:
        # Si es negativo, establecer la bandera a True para salir del bucle
        terminado = True
    else:
        # Si el número es positivo, agregarlo a la lista
        numeros.append(numero)

# Imprimir la lista de números ingresados antes de encontrar un número negativo
print("Sin breakLa lista de números ingresados es:", numeros)
