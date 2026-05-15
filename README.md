# 🌌 Sistema Astronómico

Proyecto desarrollado en Python para la gestión de cuerpos celestes mediante interfaz de consola.

El sistema permite visualizar, buscar y agregar cuerpos celestes almacenados en un archivo Excel, utilizando tablas. Permitiendo mayor facilidad
a aquellas personas que buscan organizar datos astronómicos.

---

## Características del programa

-  Visualización de cuerpos celestes en tablas organizadas
-  Búsqueda por tipo de cuerpo celeste y buscar por inicial
-  Se pueden registrar nuevos, modificar y eliminar cuerpos
-  Guardado en la tabla de cuerpos celestes
-  Interfaz visual

---

## Programa y librerías utilizadas

- Python
- Pandas
- Tabulate
- Colorama
- OpenPyXL

---

## Estructura del proyecto

```text
sistema_astronomico/
│
├── main.py
├── cuerpos_celestes.xlsx
├── README.md
└── requirements.txt
```

---

## Instalación para el programa

### 1 Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

### 2 Entrar a la carpeta del proyecto

```bash
cd tu_repositorio
```

### 3 Instalar dependencias

```bash
pip install pandas tabulate colorama openpyxl
```

O usando requirements:

```bash
pip install -r requirements.txt
```

---

##  Ejecución

Ejecuta el programa con:

```bash
python main.py
```

---

## Funcionalidades del sistema

### 1 Ver cuerpos celestes

Muestra todos los registros almacenados en el archivo Excel mediante tablas organizadas.

### 2 Buscar por tipo

Permite buscar cuerpos celestes según su tipo:

- Planeta
- Estrella
- Satélite
- Galaxia
- Nebulosa
- etc.

### 3 Agregar cuerpo celeste

El usuario puede registrar nuevos cuerpos ingresando:

- Nombre
- Tipo
- Ubicación
- Distancia
- Diámetro

El sistema valida que:
- Los textos no estén vacíos
- Los números sean válidos y positivos

### 4 Eliminar cuerpo celeste

Permite eliminar un cuerpo celeste mediante su nombre.

El sistema:
- Busca coincidencias
- Valida que el cuerpo exista
- Elimina el registro correctamente

---

### 5 Modificar datos

Permite actualizar la información de un cuerpo celeste existente.

El usuario puede modificar:
- Nombre
- Tipo
- Ubicación
- Distancia
- Diámetro
  
---

### 6 Buscar por inicial

Permite buscar cuerpos celestes por la letra inicial.

Ejemplo:
- A → Andrómeda

---

### 7 Guardar y salir

Los datos se almacenan automáticamente en:

```text
cuerpos_celestes.xlsx
```

---

## Formato de datos

El archivo Excel debe contener columnas como:

| nombre | tipo | ubicacion | distancia (ly) | diametro (km) |
|---|---|---|---|---|
| Tierra | Planeta | Sistema Solar | 0 | 12742 |

---

## Librerías utilizadas

## Pandas

Utilizada para:
- Leer archivos Excel
- Convertir datos en DataFrames
- Guardar información

## Tabulate

Permite mostrar tablas con formato elegante en consola.

## Colorama

Agrega colores y mejor apariencia visual al sistema.

---

## Conceptos aplicados

Este proyecto utiliza:

- Funciones
- Ciclos `while`
- Condicionales
- Manejo de excepciones (`try-except`)
- Validación de datos
- Diccionarios
- Listas
- Archivos Excel
- Programación modular

---

# Nombre de integrantes:

##- César Alexander Segura Díaz
##- Damián Medina Llanas
##- Yann Andrés Rodríguez Hernández

Proyecto desarrollado en Python.

---

### Licencia

Ninguna. Este programa es de uso académico.

