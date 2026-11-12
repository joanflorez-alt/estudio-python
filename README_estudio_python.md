# estudio_python

Mi ruta de estudio de Python: backend y análisis de datos.

Este README explica, paso a paso, cómo dejar esta carpeta lista: entorno virtual, Git y conexión con GitHub. Cada comando va en la terminal de VS Code, uno por uno, presionando Enter después de cada uno.

> Requisitos ya cumplidos: Git instalado, Homebrew instalado y GitHub CLI conectado como `joanflorez-alt`.

---

## Elige tu camino

Hay dos formas de llegar al mismo resultado. Escoge **una** y no mezcles los pasos.

| | Opción A: desde tu Mac | Opción B: desde la web de GitHub |
| --- | --- | --- |
| Empiezas en | La carpeta local `estudio_python` | github.com |
| `.gitignore` | Lo creas tú (Paso 1) | GitHub lo genera con la plantilla Python |
| Conexión con GitHub | Al final, con `gh repo create` (Paso 13) | Al inicio, con `git clone` |
| Carpeta final | `~/proyectos/estudio_python` | `~/proyectos/estudio-python` |
| Sigue | Pasos 0 a 14 | [Opción B](#opción-b-crear-el-repo-desde-la-web-de-github) y luego los pasos que indica |

---

# Opción A: desde tu Mac

## Paso 0. Ubicarte en la carpeta

```bash
cd ~/proyectos/estudio_python
```

Verifica que estás en el lugar correcto:

```bash
pwd
```

Debe mostrar `/Users/mac/proyectos/estudio_python`.

---

## Paso 1. Crear el archivo `.gitignore` (PRIMERO que todo)

Este archivo le dice a Git qué **no** debe subir a GitHub. Se crea antes del entorno virtual para que la carpeta `venv` nunca se suba por error.

Desde la terminal:

```bash
touch .gitignore
```

O desde VS Code, sin terminal: clic derecho en el explorador de la izquierda → **New File** → escribe exactamente `.gitignore` (con punto al inicio y sin extensión).

Ábrelo, pega este contenido y guarda con `Cmd + S`:

```
# Entorno virtual
venv/
.venv/

# Archivos de Python
__pycache__/
*.pyc

# Variables secretas
.env

# Archivos del Mac
.DS_Store

# Jupyter
.ipynb_checkpoints/

# Bases de datos locales
*.sqlite3
```

---

## Paso 2. Crear este README

```bash
touch README.md
```

Pega aquí el contenido de este documento y guarda. GitHub muestra el `README.md` como portada del repositorio.

---

## Paso 3. Crear las carpetas

```bash
mkdir backend
```

```bash
mkdir backend/01-python-intermedio
```

```bash
mkdir datos
```

Git **no sube carpetas vacías**. Una carpeta solo aparece en GitHub cuando tiene al menos un archivo adentro.

---

## Paso 4. Crear el primer archivo de código

```bash
touch backend/01-python-intermedio/ejercicio_01.py
```

Ábrelo en VS Code, escribe esto y guarda:

```python
print("Hola, empiezo mi ruta de Python")
```

---

## Paso 5. Crear el entorno virtual

```bash
python3 -m venv venv
```

Esto crea la carpeta `venv` con un Python aislado solo para este proyecto.

---

## Paso 6. Activar el entorno virtual

```bash
source venv/bin/activate
```

Debe aparecer `(venv)` al inicio de la línea:

```
(venv) mac@MacBook-Air-de-mac-2 estudio_python %
```

Si VS Code pregunta si quieres usar este entorno para el proyecto, responde **Sí**.

---

## Paso 7. Probar que todo funciona

```bash
python --version
```

```bash
python backend/01-python-intermedio/ejercicio_01.py
```

Debe imprimir: `Hola, empiezo mi ruta de Python`

---

## Paso 8. Actualizar pip y guardar las dependencias

```bash
pip install --upgrade pip
```

```bash
pip freeze > requirements.txt
```

`requirements.txt` guarda la lista de librerías instaladas. Hoy queda casi vacío; se llena a medida que instales cosas (pandas, fastapi, etc.). Cada vez que instales algo nuevo, repite `pip freeze > requirements.txt`.

---

## Paso 9. Iniciar Git en la carpeta

```bash
git init
```

```bash
git branch -M main
```

---

## Paso 10. Revisar qué se va a subir

```bash
git status
```

Deben aparecer en rojo: `.gitignore`, `README.md`, `backend/` y `requirements.txt`.

**La carpeta `venv/` NO debe aparecer.** Si aparece, revisa que guardaste bien el `.gitignore` del Paso 1.

---

## Paso 11. Preparar los archivos

```bash
git add .
```

```bash
git status
```

Ahora deben aparecer en verde.

---

## Paso 12. Hacer el primer commit

```bash
git commit -m "Estructura inicial: README, gitignore y fase 1"
```

---

## Paso 13. Crear el repositorio en GitHub y subirlo

Este único comando crea el repo en GitHub, lo conecta con tu carpeta y sube todo:

```bash
gh repo create estudio-python --public --source=. --remote=origin --push
```

- `estudio-python` es el nombre que tendrá en GitHub. Puede ser diferente al de la carpeta local.
- `--source=.` usa la carpeta actual.
- `--push` sube el commit de una vez.

---

## Paso 14. Verlo en GitHub

```bash
gh repo view --web
```

Se abre el navegador con tu repositorio en `github.com/joanflorez-alt/estudio-python`.

---

# Opción B: crear el repo desde la web de GitHub

Con esta opción, GitHub crea el `README.md` y el `.gitignore` por ti, y la carpeta llega a tu Mac ya conectada. No necesitas `git init` ni `gh repo create`.

## B1. Crear el repositorio en github.com

1. Entra a [github.com/new](https://github.com/new).
2. **Repository name:** `estudio-python`
3. **Description:** `Mi ruta de estudio: Python backend y análisis de datos`
4. Marca **Public**.
5. Marca **Add a README file**.
6. En **Add .gitignore**, busca y elige **Python**. Esta plantilla ya excluye `venv/`, `.env` y `__pycache__/`.
7. Clic en **Create repository**.

## B2. Agregar `.DS_Store` al `.gitignore` (desde la web)

La plantilla de Python no incluye el archivo oculto del Mac.

1. En tu repo, abre el archivo `.gitignore`.
2. Clic en el ícono del lápiz (**Edit this file**).
3. Ve al final del archivo y agrega esta línea:
   ```
   .DS_Store
   ```
4. Clic en **Commit changes** → **Commit changes**.

## B3. Clonar el repo en tu Mac

```bash
cd ~/proyectos
```

```bash
git clone https://github.com/joanflorez-alt/estudio-python.git
```

```bash
cd estudio-python
```

Revisa que llegaron los archivos (`-a` muestra también los ocultos como `.gitignore`):

```bash
ls -a
```

## B4. Borrar la carpeta que creaste a mano

Si ya tenías `~/proyectos/estudio_python` (con guion bajo) y no tiene nada importante, bórrala para no confundirte. Hazlo desde el Finder (arrastrar a la Papelera) o con:

```bash
rm -rf ~/proyectos/estudio_python
```

Si tenía archivos que quieres conservar, muévelos primero a `estudio-python`.

## B5. Continuar con los pasos de la Opción A

Desde la carpeta `~/proyectos/estudio-python`, sigue estos pasos de la Opción A:

- **Salta los Pasos 1 y 2**: el `.gitignore` y el `README.md` ya existen. Si quieres, abre el `README.md` en VS Code y pega este contenido en lugar del texto corto que puso GitHub.
- **Paso 3** a **Paso 8**: carpetas, primer archivo, entorno virtual y `requirements.txt`.
- **Salta el Paso 9** (`git init`): el repo ya está iniciado.
- **Paso 10** a **Paso 12**: revisar, `git add .` y commit.
- **En vez del Paso 13**, solo sube:
  ```bash
  git push
  ```
- **Paso 14** para verlo en la web.

En la rutina diaria, usa `cd ~/proyectos/estudio-python` (con guion).

---

## Rutina de cada sesión de estudio

Al **empezar**:

```bash
cd ~/proyectos/estudio_python
```

```bash
source venv/bin/activate
```

Al **terminar**:

```bash
git add .
```

```bash
git commit -m "Describe lo que hiciste hoy"
```

```bash
git push
```

```bash
deactivate
```

Ejemplos de buenos mensajes de commit:

- `"Fase 1: ejercicios de clases y herencia"`
- `"Fase 1: manejo de errores con try/except"`
- `"Fase 3: consultas con JOIN y GROUP BY"`

---

## Al empezar una fase nueva

```bash
mkdir backend/02-git-buenas-practicas
```

```bash
touch backend/02-git-buenas-practicas/ejercicio_01.py
```

---

## Errores comunes

| Error | Causa | Solución |
| --- | --- | --- |
| `command not found: python` | El entorno virtual no está activo | `source venv/bin/activate` |
| `fatal: not a git repository` | No estás en la carpeta del proyecto, o no hiciste `git init` | `cd ~/proyectos/estudio_python` y revisa el Paso 9 |
| `venv/` aparece en `git status` | El `.gitignore` no se guardó o tiene otro nombre | Revisa el Paso 1; el archivo debe llamarse exactamente `.gitignore` |
| `Name already exists on this account` | Ya existe un repo `estudio-python` en GitHub | Usa otro nombre en el Paso 13 o borra el repo viejo en github.com |
| `error: remote origin already exists` | La carpeta ya estaba conectada a un repo | `git remote -v` para ver a cuál, y `git push` directamente |
| `nothing to commit` | No hay cambios nuevos desde el último commit | Normal: guarda tus archivos (`Cmd + S`) y vuelve a intentar |

---

## Estructura del proyecto

```
estudio_python/
├── .gitignore
├── README.md
├── requirements.txt
├── venv/                       (no se sube a GitHub)
├── backend/
│   └── 01-python-intermedio/
│       └── ejercicio_01.py
└── datos/                      (se sube cuando tenga archivos)
```
