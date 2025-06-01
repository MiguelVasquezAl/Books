# 📚 Sistema de Gestión de Biblioteca (CLI)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

## 📝 Descripción

Aplicación de línea de comandos (CLI) para gestionar libros en una biblioteca. Permite añadir, buscar, prestar y devolver libros, guardando los datos en un archivo CSV.

## ✨ Características

* **Añadir Libros:** Registro con ID único y validación.
* **Buscar Libros:** Búsqueda flexible por título y autor (parcial, sin distinguir mayúsculas/minúsculas o acentos).
* **Gestionar Préstamos/Devoluciones:** Cambia el estado de disponibilidad del libro.
* **Ver Libros:** Lista todos los libros con su estado.
* **Persistencia de Datos:** Guarda y carga los libros desde `data/libros.csv`.
* **Logging:** Registra acciones clave con un decorador.