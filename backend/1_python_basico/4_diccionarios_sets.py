# =====================================================================
#   4_diccionarios_sets.py
#   Diccionarios y Sets en Python: de básico a avanzado
#   Ejecuta el archivo completo y ve leyendo cada sección con su salida.
# =====================================================================


# =====================================================================
#   PARTE 1: DICCIONARIOS - BÁSICO
# =====================================================================
print("\n========== 1. CREAR DICCIONARIOS ==========")

# Un diccionario guarda pares  clave: valor  entre llaves {}
persona = {
    "name": "Joan",
    "age": 39,
    "phone": "3143644646",   # texto: no se hacen cuentas con él y conserva ceros
}
print(persona)
print(type(persona))          # <class 'dict'>

vacio = {}                    # diccionario vacío
vacio2 = dict()               # otra forma
print(vacio, vacio2)

# Con la función dict() y argumentos con nombre
ciudad = dict(nombre="Bogotá", pais="Colombia", altitud=2640)
print(ciudad)

# Las claves deben ser INMUTABLES: str, int, float, tuple (no listas)
coordenadas = {(4.6, -74.0): "Bogotá", (6.2, -75.5): "Medellín"}
print(coordenadas)


print("\n========== 2. LEER VALORES ==========")

print(persona["name"])        # acceso directo con []
# print(persona["email"])     # KeyError: la clave no existe -> el programa se cae

# .get() no falla: devuelve None o un valor por defecto
print(persona.get("email"))                   # None
print(persona.get("email", "sin email"))      # valor por defecto

# Saber si una clave existe
print("age" in persona)       # True
print("email" in persona)     # False

print(len(persona))           # cantidad de pares clave-valor


print("\n========== 3. AGREGAR, MODIFICAR Y BORRAR ==========")

persona["email"] = "joan@mail.com"   # si la clave NO existe -> la agrega
persona["age"] = 40                  # si la clave existe   -> la modifica
print(persona)

# update(): agrega o modifica varias claves a la vez
persona.update({"city": "Bogotá", "age": 39})
print(persona)

# Borrar
del persona["city"]                  # borra la clave (KeyError si no existe)
print(persona)

email = persona.pop("email")         # borra y DEVUELVE el valor
print("Email eliminado:", email)

print(persona.pop("twitter", "no tenía"))   # pop con valor por defecto, no falla

ultimo = persona.popitem()           # borra y devuelve el último par agregado
print("popitem:", ultimo)
print(persona)

# setdefault(): devuelve el valor; si la clave no existe, la crea
persona.setdefault("phone", "0000")  # ya existe -> no cambia
persona.setdefault("country", "Colombia")
print(persona)

copia = persona.copy()               # copia independiente (superficial)
copia["name"] = "Otro"
print(persona["name"], copia["name"])

copia.clear()                        # vacía el diccionario
print(copia)


print("\n========== 4. RECORRER UN DICCIONARIO ==========")

producto = {"nombre": "Café", "precio": 18900, "stock": 25}

print(producto.keys())        # dict_keys([...])
print(producto.values())      # dict_values([...])
print(producto.items())       # dict_items([(clave, valor), ...])

print("\n-- solo claves --")
for clave in producto:        # recorrer directo da las claves
    print(clave)

print("\n-- solo valores --")
for valor in producto.values():
    print(valor)

print("\n-- clave y valor --")
for clave, valor in producto.items():
    print(f"{clave} -> {valor}")


print("\n========== 5. TU TABLA, AHORA CON DICCIONARIO ==========")

persona = {"name": "Joan", "age": 39, "phone": "3143644646"}

print("-" * 23)
for clave, valor in persona.items():
    print(f"|{clave:<10}|{str(valor):<10}|")
print("-" * 23)


# =====================================================================
#   PARTE 2: DICCIONARIOS - INTERMEDIO
# =====================================================================
print("\n========== 6. LISTA DE DICCIONARIOS ==========")

students = [
    {"name": "Ana",    "age": 20, "nota": 4.5},
    {"name": "Luis",   "age": 22, "nota": 3.2},
    {"name": "Camila", "age": 19, "nota": 4.8},
    {"name": "Pedro",  "age": 21, "nota": 2.9},
]

print(students[0])            # primer estudiante
print(students[0]["name"])    # nombre del primer estudiante

print(f"\n|{'Nombre':<10}|{'Edad':>5}|{'Nota':>5}|")
print("-" * 24)
for s in students:
    print(f"|{s['name']:<10}|{s['age']:>5}|{s['nota']:>5.1f}|")

# Promedio de notas
notas = [s["nota"] for s in students]
promedio = sum(notas) / len(notas)
print(f"\nPromedio del curso: {promedio:.2f}")

# Ordenar por nota (de mayor a menor)
ordenados = sorted(students, key=lambda s: s["nota"], reverse=True)
print("Ranking:", [s["name"] for s in ordenados])

# Mejor y peor estudiante
mejor = max(students, key=lambda s: s["nota"])
peor = min(students, key=lambda s: s["nota"])
print(f"Mejor: {mejor['name']} ({mejor['nota']})  |  Peor: {peor['name']} ({peor['nota']})")


print("\n========== 7. DICCIONARIOS ANIDADOS ==========")

empresa = {
    "nombre": "TechCol",
    "direccion": {
        "ciudad": "Medellín",
        "calle": "Cra 43A #1-50",
    },
    "empleados": [
        {"nombre": "Laura", "cargo": "Backend"},
        {"nombre": "Diego", "cargo": "Frontend"},
    ],
}

print(empresa["direccion"]["ciudad"])          # Medellín
print(empresa["empleados"][1]["nombre"])       # Diego

empresa["direccion"]["codigo_postal"] = "050021"
empresa["empleados"].append({"nombre": "Joan", "cargo": "Backend"})

for emp in empresa["empleados"]:
    print(f"- {emp['nombre']}: {emp['cargo']}")

# OJO: .copy() es superficial. Los objetos internos se comparten.
import copy
superficial = empresa.copy()
profunda = copy.deepcopy(empresa)
superficial["direccion"]["ciudad"] = "Cali"     # ¡también cambia en empresa!
print("Original tras modificar la copia superficial:", empresa["direccion"]["ciudad"])
print("Copia profunda (no se afectó):", profunda["direccion"]["ciudad"])


print("\n========== 8. CONTAR Y AGRUPAR ==========")

# Contar cuántas veces aparece cada palabra
texto = "python es genial y python es fácil y python es poderoso"
conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)

# Agrupar empleados por cargo
agrupado = {}
for emp in empresa["empleados"]:
    agrupado.setdefault(emp["cargo"], []).append(emp["nombre"])
print(agrupado)


print("\n========== 9. DICT COMPREHENSION ==========")

# {clave: valor for elemento in iterable}
cuadrados = {n: n ** 2 for n in range(1, 6)}
print(cuadrados)

# Con condición
aprobados = {s["name"]: s["nota"] for s in students if s["nota"] >= 3.0}
print("Aprobados:", aprobados)

# Transformar valores: precios con IVA (19%)
precios = {"Arroz": 3500, "Café": 18900, "Leche": 4200}
con_iva = {prod: round(p * 1.19) for prod, p in precios.items()}
print(con_iva)

# Invertir un diccionario (valor -> clave)
invertido = {v: k for k, v in precios.items()}
print(invertido)

# Crear un dict desde dos listas con zip()
claves = ["name", "age", "phone"]
valores = ["Joan", 39, "3143644646"]
print(dict(zip(claves, valores)))

# fromkeys(): mismas claves con un valor inicial
print(dict.fromkeys(["lunes", "martes", "miércoles"], 0))


# =====================================================================
#   PARTE 3: SETS (CONJUNTOS)
# =====================================================================
print("\n========== 10. CREAR SETS ==========")

# Un set es una colección SIN orden y SIN duplicados
colores = {"rojo", "verde", "azul", "rojo"}
print(colores)                # el "rojo" repetido desaparece
print(type(colores))

vacio = set()                 # ¡OJO! {} crea un diccionario, no un set
print(type({}), type(set()))

# Uso más común: eliminar duplicados de una lista
numeros = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unicos = set(numeros)
print(unicos)
print(sorted(unicos))         # volver a lista ordenada

print(set("mississippi"))     # letras únicas de un texto

# Los sets NO tienen índice:  colores[0]  -> TypeError


print("\n========== 11. AGREGAR, BORRAR Y BUSCAR ==========")

frutas = {"manzana", "pera"}
frutas.add("mango")                          # agrega uno
frutas.update(["uva", "fresa", "pera"])      # agrega varios (ignora repetidos)
print(frutas)

frutas.remove("uva")          # borra; KeyError si no existe
frutas.discard("kiwi")        # borra; NO falla si no existe
print(frutas)

print("mango" in frutas)      # buscar en un set es MUY rápido
print(len(frutas))

for fruta in sorted(frutas):  # se puede recorrer (sorted para orden fijo)
    print("-", fruta)


print("\n========== 12. OPERACIONES DE CONJUNTOS ==========")

backend = {"Python", "SQL", "Docker", "Git"}
frontend = {"JavaScript", "HTML", "CSS", "Git"}

print("Unión (todo):          ", backend | frontend)          # .union()
print("Intersección (ambos):  ", backend & frontend)          # .intersection()
print("Diferencia (solo back):", backend - frontend)          # .difference()
print("Diferencia simétrica:  ", backend ^ frontend)          # en uno u otro, no en ambos

# Subconjuntos y superconjuntos
basico = {"Python", "Git"}
print(basico.issubset(backend))      # ¿basico está dentro de backend? True
print(backend.issuperset(basico))    # True
print(basico.isdisjoint({"HTML"}))   # ¿no comparten nada? True


print("\n========== 13. SET COMPREHENSION Y FROZENSET ==========")

pares = {n for n in range(10) if n % 2 == 0}
print(pares)

correos = ["ana@gmail.com", "luis@hotmail.com", "pedro@gmail.com"]
dominios = {c.split("@")[1] for c in correos}
print(dominios)

# frozenset: set inmutable (puede ser clave de diccionario)
equipo = frozenset(["Ana", "Luis"])
proyectos = {equipo: "App de ventas"}
print(proyectos)


# =====================================================================
#   PARTE 4: AVANZADO
# =====================================================================
print("\n========== 14. MÓDULO collections ==========")

from collections import Counter, defaultdict

# Counter: cuenta automáticamente
conteo = Counter(texto.split())
print(conteo)
print(conteo.most_common(2))         # las 2 más repetidas

# defaultdict: crea el valor por defecto si la clave no existe
grupos = defaultdict(list)
for s in students:
    estado = "aprobado" if s["nota"] >= 3.0 else "reprobado"
    grupos[estado].append(s["name"])
print(dict(grupos))


print("\n========== 15. UNIR DICCIONARIOS ==========")

base = {"host": "localhost", "port": 3306}
extra = {"port": 5432, "user": "admin"}

print({**base, **extra})      # desempaquetado (el de la derecha gana)
print(base | extra)           # operador | (Python 3.9+)


print("\n========== 16. ORDENAR UN DICCIONARIO ==========")

ventas = {"Arroz": 120, "Café": 340, "Leche": 210, "Pan": 95}

por_clave = dict(sorted(ventas.items()))
por_valor = dict(sorted(ventas.items(), key=lambda par: par[1], reverse=True))
print("Por nombre:", por_clave)
print("Más vendidos:", por_valor)


print("\n========== 17. PROYECTO MINI: INVENTARIO ==========")

inventario = {
    "Arroz": {"precio": 3500,  "stock": 40, "categoria": "granos"},
    "Café":  {"precio": 18900, "stock": 0,  "categoria": "bebidas"},
    "Leche": {"precio": 4200,  "stock": 15, "categoria": "lácteos"},
    "Té":    {"precio": 7600,  "stock": 8,  "categoria": "bebidas"},
}

print(f"|{'Producto':<10}|{'Precio':>10}|{'Stock':>6}|{'Total':>12}|")
print("-" * 43)
valor_total = 0
for nombre, datos in inventario.items():
    total = datos["precio"] * datos["stock"]
    valor_total += total
    print(f"|{nombre:<10}|{datos['precio']:>10,}|{datos['stock']:>6}|{total:>12,}|")
print("-" * 43)
print(f"Valor total del inventario: ${valor_total:,}")

agotados = [n for n, d in inventario.items() if d["stock"] == 0]
print("Agotados:", agotados)

categorias = {d["categoria"] for d in inventario.values()}
print("Categorías:", sorted(categorias))


# =====================================================================
#   RESUMEN: ¿CUÁNDO USAR CADA UNO?
# =====================================================================
print("""
========== RESUMEN ==========
LISTA  [ ]  -> ordenada, permite duplicados, se modifica.   Ej: notas
TUPLA  ( )  -> ordenada, permite duplicados, NO se modifica. Ej: coordenadas
DICT   {k:v}-> pares clave-valor, claves únicas.            Ej: datos de una persona
SET    { }  -> sin orden, SIN duplicados, búsqueda rápida.  Ej: etiquetas únicas
""")


# =====================================================================
#   EJERCICIOS PARA PRACTICAR (resuélvelos debajo)
# =====================================================================
# 1. Crea un diccionario con 5 países y sus capitales. Imprímelo como tabla.
# 2. Pide al usuario un país con input() y muestra su capital con .get().
# 3. Dada una lista de compras con repetidos, muestra los productos únicos (set)
#    y cuántas veces aparece cada uno (Counter).
# 4. Con la lista students, crea un dict {nombre: "Aprobado"/"Reprobado"}
#    usando dict comprehension.
# 5. Dos amigos tienen sets de películas vistas. Muestra cuáles vieron
#    ambos, cuáles solo uno y todas juntas.
# 6. Agrega al inventario una función de "vender": resta stock y avisa si
#    no hay suficiente.

print("\n******Practica******")

persona_1 = { 
             "name: " : "Joan",
             "age: " : 39 ,
             "number: " : "3143644646"
             }
print(persona_1)
print(type(persona_1))

#otra forma con funcion dict()

persona_2 = dict(name= "Joan",
                 age= 39,
                 number= "3143644646" 
                 )
print(persona_2)
print(type(persona_2))

#leer un valor

print(persona_2["age"])
#print(persona_2["color"])   genera error, se cae el programa

print(persona_2.get("color"))  # no generar error el programa continua

print(persona_2.get("email", "no registra"))


print("age: " in persona_1)
print("email" in persona_2)

coordenadas = {(4.6, -74.0): "Bogotá", (6.2, -75.5): "Medellín"}
print(coordenadas)