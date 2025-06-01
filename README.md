# 📚 Sistema de Gestión de Biblioteca (CLI)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![CSV](https://img.shields.io/badge/CSV-000000?style=flat-square&logo=visualstudiocode&logoColor=white)](https://es.wikipedia.org/wiki/Valores_separados_por_comas)
[![Regex](https://img.shields.io/badge/Regex-FF4500?style=flat-square)](https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular)

## 📝 Descripción

Aplicación de línea de comandos (CLI) para gestionar libros en una biblioteca. Permite añadir, buscar, prestar y devolver libros, guardando los datos en un archivo CSV.

## ✨ Características

* **Añadir Libros:** Registro con ID único y validación.
* **Buscar Libros:** Búsqueda flexible por título y autor (parcial, sin distinguir mayúsculas/minúsculas o acentos).
* **Gestionar Préstamos/Devoluciones:** Cambia el estado de disponibilidad del libro.
* **Ver Libros:** Lista todos los libros con su estado.
* **Persistencia de Datos:** Guarda y carga los libros desde `data/libros.csv`.
* **Logging:** Registra acciones clave con un decorador.

## 🚀 Cómo Usar

### Requisitos

* Python 3.x

### Instalación

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/MiguelVasquezAl/Sistema-Biblioteca.git](https://github.com/MiguelVasquezAl/Sistema-Biblioteca.git)
    cd Sistema-Biblioteca
    ```
2.  (Opcional pero recomendado) Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    # En Windows: .\venv\Scripts\activate
    # En macOS/Linux: source venv/bin/activate
    ```

### Ejecución

1.  Asegúrate de estar en el directorio `Sistema-Biblioteca` y con el entorno virtual activado (si lo usaste).
2.  Ejecuta el programa:
    ```bash
    python main.py
    ```

### Interfaz del Programa

El programa mostrará un menú en la terminal: