# =============================================================================
# 2_metodos_str.py  ·  Métodos de texto (str) en Python
# =============================================================================
# Cómo usar este archivo:
#   1. Lee cada bloque y ADIVINA qué imprime antes de ejecutar.
#   2. Ejecútalo:  python backend/1_python_basico/2_metodos_str.py
#   3. Cambia los textos de ejemplo por los tuyos y vuelve a ejecutar.
#   4. Resuelve los ejercicios del final sin IA.
#
# Usamos repr() en algunos print para ver las comillas y los espacios ocultos.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. MÉTODO vs FUNCIÓN
# -----------------------------------------------------------------------------
# FUNCIÓN: se escribe sola y recibe el dato entre paréntesis.
#          len(texto)   type(texto)   print(texto)
#
# MÉTODO:  pertenece a un tipo de dato y se escribe con PUNTO después del dato.
#          texto.upper()   texto.strip()
#
# Los paréntesis () son obligatorios: sin ellos no se ejecuta el método.

nombre = "joan"

print("--- 1. Método vs función ---")
print(len(nombre))          # función: 4
print(nombre.upper())       # método: JOAN
print(nombre.upper)         # sin () NO se ejecuta: muestra que es un método


# -----------------------------------------------------------------------------
# 2. REGLA DE ORO: LOS MÉTODOS DE str NO MODIFICAN EL ORIGINAL
# -----------------------------------------------------------------------------
# Los str son inmutables. Todo método DEVUELVE un texto nuevo.
# Si no lo guardas en una variable, el resultado se pierde.

ciudad = "bogotá"

print("\n--- 2. Inmutabilidad ---")
ciudad.upper()              # crea "BOGOTÁ" y se pierde
print(ciudad)               # bogotá (sigue igual)

ciudad = ciudad.upper()     # ahora sí se guarda
print(ciudad)               # BOGOTÁ


# -----------------------------------------------------------------------------
# 3. MAYÚSCULAS Y MINÚSCULAS
# -----------------------------------------------------------------------------

frase = "pYtHoN es GENIAL"

print("\n--- 3. Mayúsculas y minúsculas ---")
print(frase.upper())        # PYTHON ES GENIAL     todo mayúscula
print(frase.lower())        # python es genial     todo minúscula
print(frase.title())        # Python Es Genial     cada palabra con mayúscula inicial
print(frase.capitalize())   # Python es genial     solo la primera letra del texto
print(frase.swapcase())     # PyThOn ES genial     invierte mayúsculas/minúsculas

# Uso real: comparar sin que importen las mayúsculas
print("ADMIN".lower() == "admin".lower())    # True


# -----------------------------------------------------------------------------
# 4. LIMPIEZA: strip, lstrip, rstrip
# -----------------------------------------------------------------------------

sucio = "  \n  Medellín  \t "

print("\n--- 4. Limpieza de bordes ---")
print(repr(sucio.strip()))      # 'Medellín'       ambos lados
print(repr(sucio.lstrip()))     # 'Medellín  \t '  solo izquierda
print(repr(sucio.rstrip()))     # '  \n  Medellín' solo derecha

# Con argumento: quita ESOS caracteres de los bordes
print("$$$85000$$".strip("$"))  # 85000
print("***oferta***".strip("*")) # oferta


# -----------------------------------------------------------------------------
# 5. REEMPLAZAR: replace(viejo, nuevo)
# -----------------------------------------------------------------------------
# Reemplaza en CUALQUIER parte del texto, no solo en los bordes.

print("\n--- 5. replace ---")
celular = "300-123-4567"
print(celular.replace("-", ""))          # 3001234567

precio_colombiano = "4.150.000"
print(precio_colombiano.replace(".", ""))  # 4150000  (listo para convertir a int)

saludo = "hola hola hola"
print(saludo.replace("hola", "chao", 1))  # chao hola hola  (el 1 = solo la primera vez)

# Eliminar algo = reemplazarlo por texto vacío
print("Hola, mundo!".replace(",", "").replace("!", ""))  # Hola mundo


# -----------------------------------------------------------------------------
# 6. BUSCAR DENTRO DEL TEXTO
# -----------------------------------------------------------------------------

correo = "joan.florez@gmail.com"

print("\n--- 6. Buscar ---")
print(correo.startswith("joan"))     # True   ¿empieza con...?
print(correo.endswith(".com"))       # True   ¿termina con...?
print(correo.endswith((".com", ".co")))  # True: acepta varias opciones en una tupla
print(correo.count("o"))             # 3      ¿cuántas veces aparece?
print(correo.find("@"))              # 11     posición donde aparece (empieza en 0)
print(correo.find("#"))              # -1     -1 significa "no está"

# index() es como find(), pero si no encuentra da ERROR en vez de -1
print(correo.index("@"))             # 11
# correo.index("#")                  # ValueError (descomenta para ver)


# -----------------------------------------------------------------------------
# 7. VALIDAR: métodos que empiezan con "is" y devuelven True/False
# -----------------------------------------------------------------------------

print("\n--- 7. Validar ---")
print("1234567890".isdigit())    # True   ¿solo dígitos?  (útil para cédulas)
print("123-456".isdigit())       # False  el guion no es dígito
print("Joan".isalpha())          # True   ¿solo letras?
print("Joan Florez".isalpha())   # False  ¡el espacio no es letra!
print("abc123".isalnum())        # True   ¿solo letras y números?
print("   ".isspace())           # True   ¿solo espacios?
print("HOLA".isupper())          # True   ¿todo en mayúscula?
print("hola".islower())          # True   ¿todo en minúscula?
print("Hola Mundo".istitle())    # True   ¿formato título?

# Combinado con limpieza: validar una cédula escrita con puntos
cedula = " 1.023.456.789 "
cedula_limpia = cedula.strip().replace(".", "")
print(cedula_limpia, cedula_limpia.isdigit())   # 1023456789 True


# -----------------------------------------------------------------------------
# 8. DIVIDIR Y UNIR: split() y join()
# -----------------------------------------------------------------------------
# split() parte un texto en una LISTA de pedazos.
# join() hace lo contrario: une una lista en un solo texto.
# (Las listas las veremos a fondo pronto; por ahora observa el resultado.)

print("\n--- 8. split y join ---")
nombre_completo = "Joan Sebastián Flórez"
print(nombre_completo.split())          # ['Joan', 'Sebastián', 'Flórez']  separa por espacios

fila_csv = "Bogotá,Cundinamarca,7900000"
print(fila_csv.split(","))              # ['Bogotá', 'Cundinamarca', '7900000']

fecha = "13/11/2026"
print(fecha.split("/"))                 # ['13', '11', '2026']

palabras = ["python", "es", "genial"]
print(" ".join(palabras))               # python es genial
print("-".join(palabras))               # python-es-genial
print("".join(palabras))                # pythonesgenial


# -----------------------------------------------------------------------------
# 9. ALINEAR Y RELLENAR
# -----------------------------------------------------------------------------

print("\n--- 9. Alinear y rellenar ---")
print("7".zfill(3))                 # 007    rellena con ceros a la izquierda
print("factura".center(20, "="))    # ======factura=======
print(repr("Nombre".ljust(10)))     # 'Nombre    '  alinea a la izquierda en 10 espacios
print(repr("Total".rjust(10)))      # '     Total'  alinea a la derecha


# -----------------------------------------------------------------------------
# 10. ENCADENAR MÉTODOS
# -----------------------------------------------------------------------------
# Como cada método devuelve un str, puedes aplicar otro método encima.
# Se ejecutan de IZQUIERDA a DERECHA.

print("\n--- 10. Encadenar ---")
dato = "   JUAN pérez   "
print(dato.strip().lower().title())          # Juan Pérez

usuario = "  Joan.Florez@GMAIL.com "
print(usuario.strip().lower())               # joan.florez@gmail.com

telefono = " (+57) 300 123 4567 "
print(telefono.strip().replace("(+57)", "").replace(" ", ""))   # 3001234567


# -----------------------------------------------------------------------------
# 11. CÓMO DESCUBRIR MÁS MÉTODOS
# -----------------------------------------------------------------------------
# dir() lista todos los métodos de un tipo. Ignora los que empiezan con __.
# help() explica qué hace un método específico (presiona q para salir).

print("\n--- 11. Descubrir métodos ---")
# (Esta línea usa una "list comprehension", que veremos más adelante.
#  Por ahora solo mira el resultado: la lista de métodos de str.)
metodos = [m for m in dir(str) if not m.startswith("_")]
print(metodos)
# help(str.split)      # descomenta para ver la documentación de split


# =============================================================================
# EJERCICIOS (resuélvelos debajo de cada enunciado)
# =============================================================================
# 1. LIMPIAR UN NOMBRE
#    nombre_formulario = "   mARÍA   fernanda   GÓMEZ  "
#    Déjalo como "María Fernanda Gómez".
#    Pista: los espacios del MEDIO también sobran. Prueba split() y join().
#
# 2. CELULAR
#    celular = "+57 (310) 555-1234"
#    Deja solo los 10 dígitos: "3105551234". Luego verifica con isdigit().
#
# 3. CORREO
#    correo = "  Ventas@MiEmpresa.COM.CO  "
#    a) Límpialo y pásalo a minúsculas.
#    b) ¿Termina en ".co"? ¿En ".com"?
#    c) ¿En qué posición está el "@"?
#
# 4. PRECIO
#    precio = "$ 1.250.000"
#    Conviértelo en el número entero 1250000 (tipo int).
#    Imprime el resultado y su type().
#
# 5. FILA DE UN CSV
#    fila = "1023456789;Carlos Ruiz;Cali;Ingeniero"
#    Sepárala por ";" e imprime el resultado. ¿Cuántos datos tiene?
#
# 6. CÓDIGO DE FACTURA
#    numero = "45"
#    Conviértelo en "FAC-00045" usando zfill().
#
# 7. RETO: ¿Por qué esto imprime False? Explícalo en un comentario
#    y luego corrígelo para que imprima True.
#       print("Juan Pérez".isalpha())
# =============================================================================

# Tus respuestas aquí:


#practica
datos = "ibague, Colombia, 8000000"

datos_lista = datos.split(",")
print(datos_lista)

ciudad,pais,poblacion = datos_lista
print(f"{ciudad} queda en {pais} y tiene una poblacion de {poblacion})")


precio = "100.345.432"
precio_limpio = int(precio.replace(".", ""))
print(precio_limpio*2)
