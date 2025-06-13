## Trabajo Integrador: Conjuntos y Operaciones con DNIs
## PARTE A
## Primero solicitamos al usuario que ingrese una cantidad de DNIs y luego los almacenamos en un diccionario.
diccionario_dni = {}
a = True
while a:
    cantidad_dni = input("Ingresa la cantidad de DNIs que queres ingresar (entre 1 y 30): ")
    if cantidad_dni.isnumeric():
        cantidad_dni = int(cantidad_dni)
        if 1 <= cantidad_dni <= 30:
            a = False
        else:
            print("Por favor, ingresa un número entre 1 y 30.")
    else:
        print("Por favor, ingresa un número válido.")

for i in range(cantidad_dni):
    dni = input(f"Ingrese el DNI que va a tener el indice {i}: ")
    while not dni.isnumeric():
        print("Por favor, ingresa solo números para el DNI.")
        dni = input(f"Ingrese el DNI que va a tener el indice {i}: ")
    digitos_unicos = set()
    for digito in dni:
        digitos_unicos.add(int(digito))
    diccionario_dni[i] = {
        "original": dni,
        "digitos_unicos": digitos_unicos,
        "frecuencias": {},
        "suma": 0
    }
    for digito in dni:
        diccionario_dni[i]["suma"] += int(digito)
        if digito in diccionario_dni[i]["frecuencias"]:
            diccionario_dni[i]["frecuencias"][digito] += 1
        else:
            diccionario_dni[i]["frecuencias"][digito] = 1

## Mostramos los resultados de los DNIs ingresados
print("\nLos DNIs ingresados son:\n")
for a in range(cantidad_dni): # Iteramos sobre los DNIs ingresdos
    print(f"DNI con índice {a}: \n"
          f"  Dígitos únicos: {diccionario_dni[a]['digitos_unicos']} \n"
          f"  Frecuencia de cada dígito: \n")
    
    for digito, frecuencia in diccionario_dni[a]["frecuencias"].items():
        print(f"    Dígito '{digito}': {frecuencia} vez/veces")
    print(f"  Suma total de los dígitos: {diccionario_dni[a]['suma']} \n")
    
encontrados = set()  #Inicializamos un conjunto para almacenar los pares de DNIs con conjuntos equivalentes en set para que no se repitan

## Esta parte del codigo corresponde a la expresion: "Si al menos dos conjuntos comparten exactamente los mismos digitos unicos, entonces se clasifican como conjuntos equivalentes."

for i in range(cantidad_dni): #Bucle para iterar sobre los DNIs
    for j in range(i + 1, cantidad_dni): # Bucle anidado para comparar cada DNI con los demás
        if diccionario_dni[i]["digitos_unicos"] == diccionario_dni[j]["digitos_unicos"]: #Si los conjuntos de digitos unicos son equivalentes
            clave = tuple(sorted([i, j]))  # Los convertimos en tupla ordenada para evitar duplicados y eso lo podemsp hacer con sorted para ordenar
            if clave not in encontrados: #Control para evitar comparaciones repetidas
                encontrados.add(clave) #Añadimos la clave al conjunto
                print(f"Los DNIs en los índices {i} y {j} tienen conjuntos equivalentes: {diccionario_dni[i]['digitos_unicos']}")
if len(encontrados) == 0: #Si la lista de encontrads esta vacia, significa que no se encontraron DNIs equivalentes
    print("No se encontraron DNIs con conjuntos equivalentes.")
    
## Funciones para realizar operaciones entre conjuntos de DNIs
def union(seleccion1, seleccion2):
    conjunto1 = diccionario_dni[seleccion1]["digitos_unicos"]
    conjunto2 = diccionario_dni[seleccion2]["digitos_unicos"]
    resultado = conjunto1.union(conjunto2) #Usamos el metodo union que ya viene con los sets de python para calcular mas facil
    print(f"La unión entre el DNI {seleccion1} y el DNI {seleccion2} es:\n{resultado}\n")

def interseccion(seleccion1, seleccion2):
    conjunto1 = diccionario_dni[seleccion1]["digitos_unicos"]
    conjunto2 = diccionario_dni[seleccion2]["digitos_unicos"]
    resultado = conjunto1.intersection(conjunto2)
    print(f"La intersección entre el DNI {seleccion1} y el DNI {seleccion2} es:\n{resultado}\n")

def diferencia(seleccion1, seleccion2):
    conjunto1 = diccionario_dni[seleccion1]["digitos_unicos"]
    conjunto2 = diccionario_dni[seleccion2]["digitos_unicos"]
    resultado = conjunto1.difference(conjunto2)
    print(f"La diferencia entre el DNI {seleccion1} y el DNI {seleccion2} es:\n{resultado}\n")

def diferencia_simetrica(seleccion1, seleccion2):
    conjunto1 = diccionario_dni[seleccion1]["digitos_unicos"]
    conjunto2 = diccionario_dni[seleccion2]["digitos_unicos"]
    resultado = conjunto1.symmetric_difference(conjunto2)
    print(f"La diferencia simétrica entre el DNI {seleccion1} y el DNI {seleccion2} es:\n{resultado}\n")

## Menu para seleccionar la operacio a realizar con los conjuntos de DNIs
decision = "1"
while decision != "0":
    decision = input("Ingresa 1 para calcular la union de los conjuntos de dos DNIs: \n"
                     "Ingresa 2 para calcular la interseccion de los conjuntos de dos DNIs: \n"
                     "Ingresa 3 para calcular la diferencia de los conjuntos de dos DNIs: \n"
                     "Ingresa 4 para calcular la diferencia simetrica de de los conjuntos de dos DNIs: \n"
                     "Ingresa 0 para salir y comenzar el programa de calculo de años (PARTE B): \n")
    
    if decision != "0":
        seleccion1 = int(input("Ingresa el numero indice del primer conjunto: "))
        seleccion2 = int(input("Ingresa el numero indice del segundo conjunto: "))
    if decision == "1":
        union(seleccion1, seleccion2)
    elif decision == "2":
        interseccion(seleccion1, seleccion2)
    elif decision == "3":
        diferencia(seleccion1, seleccion2)
    elif decision == "4":
        diferencia_simetrica(seleccion1, seleccion2)
    elif decision == "0":
        print("Saliendo..")
    else:
        print("Uno o más de los índices ingresados no son válidos, volve a intentarlo.")
        

## PARTE B
## Primero solicitamos que ingrese los años de nacimiento
b = True
while b: # Bucle para asegurarnos de que la cantidad de fechas sea un número válido
    cantidad_fechas = input("Ingresa la cantidad de años de nacimiento que queres ingresar (menor a 100 y mayor a 0): ")
    if cantidad_fechas.isnumeric():
        if int(cantidad_fechas) < 100 and int(cantidad_fechas) > 0 : #Control para que no ingrese un numero negativo o cero
            cantidad_fechas = int(cantidad_fechas)
            b = False
        else:
            print("Por favor, ingresa un número menor a 100 y mayor que 0.")
    else:
        print("Por favor, ingresa un número válido.")

fechas = []

while len(fechas) < cantidad_fechas: # Bucle para asegurarnos de que se ingresen la cantidad correcta de fechas
    fecha = input(f"Ingrese año de nacimiento: ")
    if fecha.isnumeric():
        if 1900 <= int(fecha) <= 2025:
            fechas.append(int(fecha))
        else:
            print("Por favor, ingresa un año válido entre 1900 y 2025.")
    else:
        print("Por favor, ingresa un año válido entre 1900 y 2025 (número).")
    

contador_par = 0
contador_impar = 0
contador_genZ = 0
for i in range(cantidad_fechas): #Bucle para determinar los años pares o impares
    if fechas[i] > 2000: #Si el año es posterior al 2000
        contador_genZ += 1 # Agregamos al contador de generacion Z
    if (fechas[i]) % 2 == 0: #Si el año es par
        contador_par += 1
    else: #Si el año es impar
        contador_impar += 1
        
print(f"\nCantidad de años pares: {contador_par}")
print(f"Cantidad de años impares: {contador_impar}\n")

if contador_genZ == cantidad_fechas: #Si todos los años son posteriores al 2000
    print("Grupo Z")
else:
    print("No todos los años son posteriores al 2000")
    
def es_bisiesto(fecha):
    if (fecha % 4 == 0 and fecha % 100 != 0) or (fecha % 400 == 0):
        return True
    return False

for i in range(cantidad_fechas): #Bucle para determinar si hay años bisiestos
    if es_bisiesto(int(fechas[i])): #Si el año es bisiesto
        print("Tenemos un año especial y es el año:", fechas[i], "\n")
        
fecha_actual = 2025 # El año actual para calcular las edades
edades = [] # Lista para almacenar las edades actuales
for i in range(len(fechas)): # Bucle para calcular las edades actuales
    edad = fecha_actual - fechas[i] # Calculamos la edad actual restando el año de nacimiento al año actual
    edades.append(edad) # Añadimos la edad a la lista de edades

print("Producto cartesiano entre años de nacimiento y edades actuales:")
for i in range(len(fechas)): # Bucle para mostrar el producto cartesiano
    for j in range(len(edades)): # Bucle anidado para mostrar el producto cartesiano
        print(f"({fechas[i]}, {edades[j]})") # Esto muestra el par (año de nacimiento, edad actual) para cada combinación
