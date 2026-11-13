print("Inicio de estudio de python")

#1 python · PY
# =============================================================================
# 1_python.py  ·  Tipos de variables en Python
# =============================================================================
# Cómo usar este archivo:
#   1. Lee cada bloque y sus comentarios.
#   2. Ejecútalo:  python backend/1_python_basico/1_python.py
#   3. Antes de ejecutar cada bloque, ADIVINA qué va a imprimir.
#   4. Cambia los valores y vuelve a ejecutar. Romper cosas es parte de aprender.
#   5. Al final hay ejercicios: resuélvelos tú, sin IA.
#
# Tip: si quieres ejecutar solo un bloque, comenta los demás seleccionándolos
#      y presionando Cmd + /  en VS Code.
# =============================================================================
 
 
# -----------------------------------------------------------------------------
# 1. ¿QUÉ ES UNA VARIABLE?
# -----------------------------------------------------------------------------
# Una variable es un NOMBRE que apunta a un VALOR guardado en memoria.
# En Python no declaras el tipo: Python lo deduce del valor (tipado dinámico).
 
nombre = "Joan"      # el nombre "nombre" apunta al texto "Joan"
edad = 30            # el nombre "edad" apunta al número 30
 
print("--- 1. Variables ---")
print(nombre)
print(edad)
 
 
# -----------------------------------------------------------------------------
# 2. LOS 5 TIPOS BÁSICOS
# -----------------------------------------------------------------------------
 
# int  -> números enteros (sin decimales), positivos o negativos, sin límite de tamaño
habitantes_bogota = 7_900_000      # el guion bajo solo ayuda a leer; Python lo ignora
temperatura_bajo_cero = -5
 
# float -> números con decimales. Se usa el PUNTO, nunca la coma.
estatura = 1.75
trm_dolar = 4_150.32
 
# str -> texto (string). Va entre comillas simples o dobles, son equivalentes.
ciudad = "Bogotá"
pais = 'Colombia'
frase = "Me dijo: 'hola'"           # comillas simples dentro de dobles
parrafo = """Este texto
ocupa varias
líneas."""                          # triple comilla para texto multilínea
 
# bool -> verdadero o falso. Solo existen dos valores: True y False (con mayúscula).
esta_estudiando = True
tiene_trabajo_remoto = False
 
# NoneType -> "no hay valor todavía". Solo existe un valor: None.
segundo_nombre = None
 
print("\n--- 2. Tipos básicos ---")
print(habitantes_bogota, temperatura_bajo_cero)
print(estatura, trm_dolar)
print(ciudad, pais, frase)
print(parrafo)
print(esta_estudiando, tiene_trabajo_remoto)
print(segundo_nombre)
 
 
# -----------------------------------------------------------------------------
# 3. type(): PREGUNTARLE A PYTHON QUÉ TIPO ES
# -----------------------------------------------------------------------------
 
print("\n--- 3. type() ---")
print(type(habitantes_bogota))   # <class 'int'>
print(type(estatura))            # <class 'float'>
print(type(ciudad))              # <class 'str'>
print(type(esta_estudiando))     # <class 'bool'>
print(type(segundo_nombre))      # <class 'NoneType'>
 
# Ojo: el tipo depende de cómo escribes el valor, no de lo que "significa".
print(type(10))       # int
print(type(10.0))     # float  (tiene punto decimal)
print(type("10"))     # str    (tiene comillas: es TEXTO, no número)
 
 
# -----------------------------------------------------------------------------
# 4. TIPADO DINÁMICO: UNA VARIABLE PUEDE CAMBIAR DE TIPO
# -----------------------------------------------------------------------------
# El nombre se puede reasignar a un valor de otro tipo.
# Es posible, pero en código real EVÍTALO: confunde a quien lo lee.
 
dato = 100
print("\n--- 4. Tipado dinámico ---")
print(dato, type(dato))
 
dato = "cien"
print(dato, type(dato))
 
dato = None
print(dato, type(dato))
 
 
# -----------------------------------------------------------------------------
# 5. CONVERSIÓN DE TIPOS (casting)
# -----------------------------------------------------------------------------
# Usas el nombre del tipo como si fuera una función: int(), float(), str(), bool()
 
print("\n--- 5. Conversión de tipos ---")
 
# str -> int / float  (muy común: lo que escribe un usuario siempre llega como texto)
texto_edad = "30"
edad_numero = int(texto_edad)
print(edad_numero, type(edad_numero))
 
texto_precio = "4150.32"
precio = float(texto_precio)
print(precio, type(precio))
 
# int / float -> str
codigo = 57
codigo_texto = str(codigo)
print(codigo_texto, type(codigo_texto))
 
# float -> int  CORTA los decimales, NO redondea
print(int(3.99))      # 3, no 4
print(int(-3.99))     # -3
 
# int -> float
print(float(7))       # 7.0
 
# Conversiones que FALLAN (descomenta una a la vez para ver el error):
# int("3.5")          # ValueError: el texto tiene punto, no es un entero
# int("treinta")      # ValueError: no es un número
# float("4,5")        # ValueError: Python usa punto, no coma
 
 
# -----------------------------------------------------------------------------
# 6. bool(): QUÉ CUENTA COMO VERDADERO Y QUÉ COMO FALSO
# -----------------------------------------------------------------------------
# Regla: lo "vacío" o "cero" es False. Todo lo demás es True.
 
print("\n--- 6. Valores verdaderos y falsos ---")
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False  (texto vacío)
print(bool(None))      # False
 
print(bool(1))         # True
print(bool(-8))        # True   (cualquier número distinto de cero)
print(bool(" "))       # True   (un espacio NO es vacío)
print(bool("False"))   # True   (¡trampa! es un texto con letras, no está vacío)
 
 
# -----------------------------------------------------------------------------
# 7. isinstance(): COMPROBAR SI UN VALOR ES DE CIERTO TIPO
# -----------------------------------------------------------------------------
# Más útil que type() cuando quieres verificar, porque devuelve True o False.
 
print("\n--- 7. isinstance() ---")
print(isinstance(30, int))           # True
print(isinstance("30", int))         # False
print(isinstance(1.75, (int, float)))  # True: ¿es int O float?
 
# Dato curioso: en Python, bool es un tipo especial de int.
print(isinstance(True, int))         # True
print(int(True), int(False))         # 1 0
 
 
# -----------------------------------------------------------------------------
# 8. INMUTABILIDAD: LOS TIPOS BÁSICOS NO SE MODIFICAN, SE REEMPLAZAN
# -----------------------------------------------------------------------------
# int, float, str, bool y None son INMUTABLES: el valor no cambia por dentro.
# Cuando "cambias" una variable, el nombre pasa a apuntar a un valor NUEVO.
# id() muestra la dirección en memoria del valor al que apunta el nombre.
 
print("\n--- 8. Inmutabilidad ---")
saludo = "hola"
print(id(saludo))
saludo = "hola mundo"
print(id(saludo))      # otro id: es un objeto nuevo, el anterior no se modificó
 
# Esto FALLA porque un str no se puede modificar por dentro (descomenta para ver):
# saludo[0] = "H"      # TypeError: 'str' object does not support item assignment
 
 
# -----------------------------------------------------------------------------
# 9. ASIGNACIONES ÚTILES
# -----------------------------------------------------------------------------
 
print("\n--- 9. Asignaciones ---")
 
# Varias variables en una línea
x, y, z = 1, 2.5, "tres"
print(x, y, z)
 
# El mismo valor a varias variables
a = b = c = 0
print(a, b, c)
 
# Intercambiar valores sin variable auxiliar
primero, segundo = "café", "té"
primero, segundo = segundo, primero
print(primero, segundo)        # té café
 
 
# -----------------------------------------------------------------------------
# 10. CÓMO NOMBRAR VARIABLES (reglas y convenciones)
# -----------------------------------------------------------------------------
# REGLAS (si no las cumples, error):
#   - Solo letras, números y guion bajo.
#   - No pueden empezar con número:     1nombre  -> error
#   - No pueden ser palabras reservadas: class, if, for, True, None...
#   - Distinguen mayúsculas:             edad, Edad y EDAD son 3 variables distintas
#
# CONVENCIONES (PEP 8, lo que esperan en un trabajo):
#   - snake_case para variables:  salario_mensual   (no salarioMensual)
#   - MAYÚSCULAS para constantes: SALARIO_MINIMO = 1_750_905
#   - Nombres que expliquen qué guardan: precio_unitario mejor que p o x1
#   - Evita tildes y ñ aunque Python las acepte: anio mejor que año
 
SALARIO_MINIMO_2026 = 1_750_905     # constante: por convención no se reasigna
salario_mensual = 4_500_000
 
print("\n--- 10. Nombres ---")
print(SALARIO_MINIMO_2026, salario_mensual)
 
 
# -----------------------------------------------------------------------------
# 11. TYPE HINTS: INDICAR EL TIPO ESPERADO (opcional, pero profesional)
# -----------------------------------------------------------------------------
# Python NO obliga a respetarlos; sirven como documentación y para que
# VS Code te avise de errores. Los vas a ver mucho en FastAPI.
 
usuario: str = "joanflorez-alt"
anios_experiencia: int = 0
promedio: float = 4.3
activo: bool = True
telefono: str | None = None          # puede ser texto o None
 
print("\n--- 11. Type hints ---")
print(usuario, anios_experiencia, promedio, activo, telefono)
 
 
# =============================================================================
# EJERCICIOS (resuélvelos debajo de cada enunciado)
# =============================================================================
# 1. Crea una variable para cada tipo básico (int, float, str, bool, None)
#    con datos tuyos reales, e imprime cada una junto con su type().
#
# 2. Tienes  precio_texto = "85000". Conviértelo a int y luego a float.
#    Imprime los tres valores y sus tipos.
#
# 3. Sin ejecutar, escribe en un comentario qué imprime cada línea.
#    Luego ejecuta y compara:
#       print(bool("0"))
#       print(bool(0))
#       print(int(9.9))
#       print(type(None))
#
# 4. Intercambia los valores de  ciudad_origen = "Cali"  y
#    ciudad_destino = "Medellín"  en una sola línea.
#
# 5. Corrige estos nombres para que cumplan PEP 8 (o que no den error):
#       2do_apellido = "Pérez"
#       NumeroDeHijos = 2
#       valor maximo = 100
#       class = "A"
#
# 6. Reto: ¿por qué  int("3.5")  falla pero  int(float("3.5"))  funciona?
#    Escribe la explicación en un comentario.
# =============================================================================
 
# Tus respuestas aquí:

name= "Joan Florez"
number= "34.2"
print(number)
print(type(number))
number_int = (float(number))
print(number_int)
print(number + number)
print(number_int + number_int)

print(number, name, number_int)

print(bool(0))
print(bool(1))
print(bool(0))
print(bool(2))

#EJERCICO bool
print("\n---bool---")

texto = input("ingrese su texto:").strip()

tiene_contenido = bool(texto)

if tiene_contenido:
    print("El texto tiene contenido")
else:
    print("texto vacio")

