# =============================================================================
# 3_listas_tuplas.py  ·  Listas, tuplas, desempaquetado y f-strings
# =============================================================================
# Cómo usar este archivo:
#   1. Lee cada bloque y ADIVINA qué imprime antes de ejecutar.
#   2. Ejecútalo:  python backend/1_python_basico/3_listas_tuplas.py
#   3. Cambia los datos por los tuyos y vuelve a ejecutar.
#   4. Resuelve los ejercicios del final sin IA. Primero los propuestos,
#      después inventa los tuyos.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. ¿QUÉ ES UNA LISTA?
# -----------------------------------------------------------------------------
# Una lista guarda VARIOS valores en orden, dentro de corchetes [ ].
# Puede tener valores de distintos tipos, repetidos, o estar vacía.

ciudades = ["Bogotá", "Medellín", "Cali", "Ibagué"]
precios = [85000, 120000, 45000, 120000]        # se permiten repetidos
mezcla = ["Joan", 30, 1.75, True, None]         # distintos tipos (posible, pero poco común)
vacia = []

print("--- 1. Listas ---")
print(ciudades)
print(precios)
print(mezcla)
print(vacia)
print(type(ciudades))       # <class 'list'>
print(len(ciudades))        # 4  cuántos elementos tiene


# -----------------------------------------------------------------------------
# 2. ACCEDER POR POSICIÓN (índice)
# -----------------------------------------------------------------------------
# Las posiciones empiezan en 0. Los índices negativos cuentan desde el final.
#
#   ciudades =  ["Bogotá", "Medellín", "Cali", "Ibagué"]
#   índice  ->      0          1          2        3
#   negativo->     -4         -3         -2       -1

print("\n--- 2. Índices ---")
print(ciudades[0])          # Bogotá      el primero
print(ciudades[2])          # Cali
print(ciudades[-1])         # Ibagué      el último (sin saber cuántos hay)
print(ciudades[-2])         # Cali        el penúltimo

# print(ciudades[10])       # IndexError: no existe la posición 10 (descomenta)


# -----------------------------------------------------------------------------
# 3. SLICING: CORTAR UN PEDAZO  [inicio:fin:paso]
# -----------------------------------------------------------------------------
# Toma desde "inicio" HASTA "fin" SIN incluir "fin".
# Si omites inicio, empieza desde 0. Si omites fin, va hasta el final.

numeros = [10, 20, 30, 40, 50, 60]

print("\n--- 3. Slicing ---")
print(numeros[1:4])         # [20, 30, 40]     posiciones 1, 2 y 3
print(numeros[:3])          # [10, 20, 30]     los 3 primeros
print(numeros[3:])          # [40, 50, 60]     desde la posición 3 hasta el final
print(numeros[-2:])         # [50, 60]         los 2 últimos
print(numeros[::2])         # [10, 30, 50]     de 2 en 2
print(numeros[::-1])        # [60, 50, ..., 10] al revés

# ¡Funciona IGUAL con los str! (un texto es una secuencia de caracteres)
cedula = "1023456789"
print(cedula[:3])           # 102
print(cedula[-4:])          # 6789   (útil para mostrar "****6789")
print("Python"[::-1])       # nohtyP


# -----------------------------------------------------------------------------
# 4. LA GRAN DIFERENCIA: LAS LISTAS SON MUTABLES
# -----------------------------------------------------------------------------
# Los str NO se pueden cambiar por dentro. Las listas SÍ.
# Y la mayoría de métodos de lista MODIFICAN la lista original
# (al revés de lo que aprendiste con los métodos de str).

print("\n--- 4. Mutabilidad ---")
frutas = ["mango", "lulo", "maracuyá"]
frutas[1] = "guanábana"     # cambio el elemento de la posición 1
print(frutas)               # ['mango', 'guanábana', 'maracuyá']

texto = "lulo"
# texto[0] = "L"            # TypeError con str (descomenta para comparar)


# -----------------------------------------------------------------------------
# 5. AGREGAR ELEMENTOS
# -----------------------------------------------------------------------------

print("\n--- 5. Agregar ---")
compras = ["arroz", "café"]

compras.append("panela")            # agrega UNO al final
print(compras)                      # ['arroz', 'café', 'panela']

compras.insert(0, "huevos")         # agrega en una posición específica
print(compras)                      # ['huevos', 'arroz', 'café', 'panela']

compras.extend(["leche", "pan"])    # agrega VARIOS al final
print(compras)

# ¡Trampa! append con una lista mete la lista ENTERA como un solo elemento
otra = ["a", "b"]
otra.append(["c", "d"])
print(otra)                         # ['a', 'b', ['c', 'd']]  ← lista dentro de lista


# -----------------------------------------------------------------------------
# 6. QUITAR ELEMENTOS
# -----------------------------------------------------------------------------

print("\n--- 6. Quitar ---")
pendientes = ["pagar luz", "estudiar", "mercar", "estudiar"]

pendientes.remove("estudiar")       # quita la PRIMERA vez que aparece ese valor
print(pendientes)                   # ['pagar luz', 'mercar', 'estudiar']

ultimo = pendientes.pop()           # quita el último y lo DEVUELVE
print(ultimo)                       # estudiar
print(pendientes)                   # ['pagar luz', 'mercar']

primero = pendientes.pop(0)         # quita el de la posición 0 y lo devuelve
print(primero)                      # pagar luz

del pendientes[0]                   # borra por posición, sin devolver nada
print(pendientes)                   # []

# pendientes.remove("viajar")       # ValueError: ese valor no está (descomenta)

lista_temporal = [1, 2, 3]
lista_temporal.clear()              # vacía la lista completa
print(lista_temporal)               # []


# -----------------------------------------------------------------------------
# 7. BUSCAR Y CONTAR
# -----------------------------------------------------------------------------

print("\n--- 7. Buscar y contar ---")
notas = [4.5, 3.0, 4.5, 2.8, 5.0]

print(4.5 in notas)                 # True    ¿está ese valor?
print(1.0 in notas)                 # False
print(1.0 not in notas)             # True
print(notas.index(2.8))             # 3       ¿en qué posición está?
print(notas.count(4.5))             # 2       ¿cuántas veces aparece?

# Funciones útiles con listas de números
print(len(notas))                   # 5      cantidad
print(min(notas))                   # 2.8    el menor
print(max(notas))                   # 5.0    el mayor
print(sum(notas))                   # 19.8   la suma


# -----------------------------------------------------------------------------
# 8. ORDENAR
# -----------------------------------------------------------------------------
# sort()    -> MÉTODO: modifica la lista original, no devuelve nada.
# sorted()  -> FUNCIÓN: devuelve una lista NUEVA ordenada; la original queda igual.

print("\n--- 8. Ordenar ---")
edades = [34, 19, 45, 27]

ordenadas = sorted(edades)
print(ordenadas)                    # [19, 27, 34, 45]
print(edades)                       # [34, 19, 45, 27]  ← original intacta

edades.sort()
print(edades)                       # [19, 27, 34, 45]  ← original modificada

edades.sort(reverse=True)           # de mayor a menor
print(edades)                       # [45, 34, 27, 19]

edades.reverse()                    # invierte el orden actual (no ordena)
print(edades)

# Error muy común: guardar el resultado de sort()
mal = [3, 1, 2].sort()
print(mal)                          # None  ← sort() no devuelve la lista


# -----------------------------------------------------------------------------
# 9. ¡CUIDADO! ASIGNAR NO ES COPIAR
# -----------------------------------------------------------------------------
# Con  b = a  NO creas una lista nueva: los dos nombres apuntan a LA MISMA lista.
# Si cambias una, "cambia" la otra. Para una copia real usa .copy()

print("\n--- 9. Referencia vs copia ---")
original = ["a", "b", "c"]
mismo = original                    # mismo objeto, dos nombres
copia = original.copy()             # objeto nuevo e independiente

original.append("d")
print(original)                     # ['a', 'b', 'c', 'd']
print(mismo)                        # ['a', 'b', 'c', 'd']  ← ¡también cambió!
print(copia)                        # ['a', 'b', 'c']       ← no se afectó


# -----------------------------------------------------------------------------
# 10. LISTAS DENTRO DE LISTAS (como una tabla)
# -----------------------------------------------------------------------------
# Cada lista interna es una "fila". Se accede con dos índices: [fila][columna]

print("\n--- 10. Listas anidadas ---")
tabla = [
    ["Bogotá", "Cundinamarca", 7_900_000],
    ["Medellín", "Antioquia", 2_600_000],
    ["Cali", "Valle del Cauca", 2_300_000],
]

print(tabla[1])                     # ['Medellín', 'Antioquia', 2600000]
print(tabla[1][0])                  # Medellín
print(tabla[2][2])                  # 2300000
print(len(tabla))                   # 3 filas


# -----------------------------------------------------------------------------
# 11. TUPLAS: LISTAS QUE NO SE PUEDEN MODIFICAR
# -----------------------------------------------------------------------------
# Van entre paréntesis ( ). Se leen igual que una lista (índices, slicing,
# in, count, index, len), pero NO tienen append, remove, sort, etc.
#
# ¿Cuándo usar tupla en vez de lista?
#   - Datos que NO deben cambiar: coordenadas, una fecha, colores RGB.
#   - Para proteger datos de cambios por error.

print("\n--- 11. Tuplas ---")
coordenadas_bogota = (4.711, -74.072)
fecha_nacimiento = (1992, 5, 18)
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes")

print(coordenadas_bogota[0])        # 4.711
print(dias_semana[-1])              # viernes
print(dias_semana[:2])              # ('lunes', 'martes')
print(type(fecha_nacimiento))       # <class 'tuple'>

# fecha_nacimiento[0] = 1990        # TypeError: las tuplas no se modifican (descomenta)

# Trampa: una tupla de UN solo elemento necesita una coma
no_es_tupla = ("hola")
si_es_tupla = ("hola",)
print(type(no_es_tupla))            # <class 'str'>
print(type(si_es_tupla))            # <class 'tuple'>


# -----------------------------------------------------------------------------
# 12. DESEMPAQUETAR: SACAR LOS VALORES EN VARIABLES
# -----------------------------------------------------------------------------
# Ya lo usaste en tu práctica. La cantidad de variables debe coincidir
# con la cantidad de elementos.

print("\n--- 12. Desempaquetar ---")
latitud, longitud = coordenadas_bogota
print(latitud, longitud)

anio, mes, dia = fecha_nacimiento
print(dia, mes, anio)

# Con * una variable recoge "el resto" en una lista
primero, *resto = ["oro", "plata", "bronce", "mención"]
print(primero)                      # oro
print(resto)                        # ['plata', 'bronce', 'mención']

*inicio, ultimo = [1, 2, 3, 4]
print(inicio, ultimo)               # [1, 2, 3] 4

# Si no coinciden las cantidades:
# a, b = [1, 2, 3]                  # ValueError: too many values to unpack (descomenta)

# El intercambio  x, y = y, x  del archivo 1 funciona gracias a esto:
# Python arma una tupla (y, x) y la desempaqueta en x, y.


# -----------------------------------------------------------------------------
# 13. CONVERTIR ENTRE str, LISTA Y TUPLA
# -----------------------------------------------------------------------------

print("\n--- 13. Conversiones ---")
print(list("hola"))                 # ['h', 'o', 'l', 'a']
print(list((1, 2, 3)))              # [1, 2, 3]       tupla -> lista
print(tuple([1, 2, 3]))             # (1, 2, 3)       lista -> tupla

# El flujo de limpieza que ya practicaste: texto -> lista -> valores limpios
fila = "Ibagué, Tolima, 580000"
partes = fila.split(",")
print(partes)                       # ['Ibagué', ' Tolima', ' 580000']  ← espacios
ciudad, departamento, poblacion = partes
ciudad = ciudad.strip()
departamento = departamento.strip()
poblacion = int(poblacion.strip())
print(ciudad, departamento, poblacion, type(poblacion))


# -----------------------------------------------------------------------------
# 14. f-STRINGS: ARMAR TEXTO CON VARIABLES
# -----------------------------------------------------------------------------
# Una f antes de las comillas permite meter variables y expresiones entre { }.

print("\n--- 14. f-strings ---")
nombre = "Joan"
edad = 30
salario = 4_500_000
promedio = 4.2666666

print(f"Hola, soy {nombre} y tengo {edad} años")
print(f"El próximo año tendré {edad + 1}")                # expresiones dentro de { }
print(f"Mi nombre en mayúsculas: {nombre.upper()}")      # métodos dentro de { }
print(f"Primera ciudad de la lista: {ciudades[0]}")      # índices dentro de { }

# Formato de números con  :
print(f"Salario: {salario:,}")                           # 4,500,000   separador de miles
print(f"Salario: ${salario:,}".replace(",", "."))        # $4.500.000  formato colombiano
print(f"Promedio: {promedio:.2f}")                       # 4.27        2 decimales
print(f"Avance: {0.756:.1%}")                            # 75.6%       porcentaje

# Alinear (útil para imprimir tablas)
print(f"|{'Producto':<12}|{'Precio':>10}|")              # < izquierda, > derecha
print(f"|{'Arroz':<12}|{3500:>10,}|")
print(f"|{'Café':<12}|{18900:>10,}|")

# Truco para depurar: el = muestra el nombre de la variable y su valor
print(f"{edad=}")                                        # edad=30


# =============================================================================
# EJERCICIOS (resuélvelos debajo de cada enunciado)
# =============================================================================
# 1. LISTA DE MERCADO
#    Crea una lista con 3 productos. Luego:
#    a) Agrega 2 más al final y 1 al inicio.
#    b) Quita uno por su nombre.
#    c) Imprime el primero, el último y cuántos hay.
#
# 2. NOTAS
#    notas = [3.5, 4.8, 2.9, 4.0, 3.7]
#    Imprime: la nota más alta, la más baja, la suma y el promedio
#    (promedio = suma / cantidad) con 1 decimal usando f-string.
#
# 3. ORDENAR SIN DAÑAR
#    precios = [45000, 12000, 98000, 30000]
#    Imprime los precios ordenados de menor a mayor SIN modificar la lista
#    original. Demuestra con un print que la original sigue igual.
#
# 4. SLICING CON TEXTO
#    tarjeta = "4532015112830366"
#    Imprime "**** **** **** 0366" usando slicing y una f-string.
#
# 5. LA TRAMPA DE LA COPIA
#    a = [1, 2, 3]
#    b = a
#    b.append(4)
#    Sin ejecutar: ¿qué imprime print(a)? Escríbelo en un comentario,
#    ejecuta y explica. Luego corrígelo para que a NO cambie.
#
# 6. FILA DE UN CSV (continuación de tu práctica)
#    fila = "Pereira, Risaralda, 480000, 1863"
#    Sepárala, desempaqueta en 4 variables LIMPIAS (sin espacios),
#    convierte población y año de fundación a int, e imprime:
#    "Pereira (Risaralda) fue fundada en 1863 y tiene 480.000 habitantes"
#
# 7. TUPLA
#    Crea una tupla con tu fecha de nacimiento (año, mes, día).
#    a) Desempaquétala en 3 variables.
#    b) Intenta cambiar el año y copia el error en un comentario.
#    c) ¿Por qué tiene sentido que una fecha de nacimiento sea tupla?
#
# 8. TABLA
#    Crea una lista de 3 productos donde cada uno sea [nombre, precio, cantidad].
#    Imprime una tabla alineada con f-strings que tenga encabezado:
#       Producto      Precio   Cant.
#
# 9. RETO
#    ranking = ["Ana", "Luis", "Marta", "Pedro", "Sofía"]
#    Usando desempaquetado con *, guarda el primero en "ganador",
#    el último en "ultimo" y los del medio en "medio". Imprime los tres.
# =============================================================================

# Tus respuestas aquí:



#PRACTICA

nueva_lista = ["manzana", "banano", "pera"]
list_2 = [1,2,3,4,5,6]
list_3 = [1, "uno", False, 3.14]
print(nueva_lista)
print(list_2)
print(list_3)

print(list_2[-3])


number_list = [11,12,13,14,15,16,17,18,19,20]

print(number_list[::4])

name = "Joan Manuel Florez"
print(name[::-1].replace(" ",""))

students = ["Ana", "Mario", "Pedro"]
print(students)

students.append("Carlos")
students.append("Laura")
print(students)

students.insert(0, "Sofia")
print(students)

students.insert(2, "JMmario")
print(students)

students.extend(["luis", "juana", "carla", "alan"])
print(students)

students[1] = "WWW"
print(students)


clave = "1234566789"
print("*******",clave[-4:])


print("\n--- 6. Quitar ---")
pendientes = ["pagar luz", "estudiar", "mercar", "estudiar"]

pendientes.remove("estudiar")       # quita la PRIMERA vez que aparece ese valor
print(pendientes)                   # ['pagar luz', 'mercar', 'estudiar']

ultimo = pendientes.pop()           # quita el último y lo DEVUELVE
print(ultimo)                       # estudiar
print(pendientes)                   # ['pagar luz', 'mercar']

primero = pendientes.pop(0)         # quita el de la posición 0 y lo devuelve
print(primero)                      # pagar luz

del pendientes[0]                   # borra por posición, sin devolver nada
print(pendientes)                   # []

# pendientes.remove("viajar")       # ValueError: ese valor no está (descomenta)

lista_temporal = [1, 2, 3]
lista_temporal.clear()              # vacía la lista completa
print(lista_temporal)   

facturas = ["luz", "agua", "gas", "internet", "vigilancia", "luz"]
print(facturas)

facturas.remove("luz")
print(facturas)

facturas.append("luz")
print(facturas)
facturas.pop()
print(facturas) 

facturas.pop(4)
print(facturas)

del facturas[1]
print(facturas) 

print("\n--- 7. Buscar y contar ---")

calificaciones = [3, 4.5, 3.1, 4.8, 5, 4, 1, 2, 2, 2, 0.5]

print( 8 in calificaciones)

print(3 not in calificaciones)

print(calificaciones.index(2))

print(calificaciones.count(2))

lista_names = ["ana", "mario", "mario", "maria", "mario"]
print(lista_names.count("mario"))

"""
print(4.5 in notas)                 # True    ¿está ese valor?
print(1.0 in notas)                 # False
print(1.0 not in notas)             # True
print(notas.index(2.8))             # 3       ¿en qué posición está?
print(notas.count(4.5))             # 2       ¿cuántas veces aparece?

# Funciones útiles con listas de números
print(len(notas))                   # 5      cantidad
print(min(notas))                   # 2.8    el menor
print(max(notas))                   # 5.0    el mayor
print(sum(notas))                   # 19.8   la suma
"""

#tuplas

fecha_cumple = (4, 9, 1987)
print(fecha_cumple)
print(type(fecha_cumple))
day, month, year = fecha_cumple

print("dia:", day, "mes:", month, "ano:", year)

"""print("\n--- 14. f-strings ---")
nombre = "Joan"
edad = 30
salario = 4_500_000
promedio = 4.2666666

print(f"Hola, soy {nombre} y tengo {edad} años")
print(f"El próximo año tendré {edad + 1}")                # expresiones dentro de { }
print(f"Mi nombre en mayúsculas: {nombre.upper()}")      # métodos dentro de { }
print(f"Primera ciudad de la lista: {ciudades[0]}")      # índices dentro de { }

# Formato de números con  :
print(f"Salario: {salario:,}")                           # 4,500,000   separador de miles
print(f"Salario: ${salario:,}".replace(",", "."))        # $4.500.000  formato colombiano
print(f"Promedio: {promedio:.2f}")                       # 4.27        2 decimales
print(f"Avance: {0.756:.1%}")                            # 75.6%       porcentaje

# Alinear (útil para imprimir tablas)
print(f"|{'Producto':<12}|{'Precio':>10}|")              # < izquierda, > derecha
print(f"|{'Arroz':<12}|{3500:>10,}|")
print(f"|{'Café':<12}|{18900:>10,}|")

# Truco para depurar: el = muestra el nombre de la variable y su valor
print(f"{edad=}")      

"""

name = "Manuel"
age = 39

phrase = f"My name is {name.upper()} and next year I'll be {age + 1} years old"
print(phrase)

citys = ["Bogotá", "cucuta", "medellin", "cali"]

print(phrase, f"y la segunda ciudad de la lista es {citys[1]}")


sueldo = 7_343_000

print(f"sueldo  {sueldo:,}")
print(f"sueldo  {sueldo:,}".replace(",", "."))


notas = [2,3,1,5,6,9,11,20]
print(notas)

print(sorted(notas))
print(notas)

notas.sort()
print(notas)

promedio = sum(notas)/ len(notas)
print(promedio)
print(f"El promedio de las notas es {promedio:.1f}")

decimal = 0.23445
porcentaje = f"en porcentaje es {decimal:.1%}"
print(porcentaje)

print("\n---Tablas--- ")

print(f"|{'Producto':<12}|{'Precio':>10}|")              # < izquierda, > derecha
print(f"|{'Arroz':<12}|{3500:>10,}|")
print(f"|{'Café':<12}|{18900:>10,}|")


print("\n *****tabla propia*****")

print(f"|{"name":<10}|{"Joan":<10}|")
print(f"|{"age":<10}|{"39":<10}|")
print(f"|{"phone":<10}|{3143644646:<10}|")