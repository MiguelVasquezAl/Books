import csv
import os
import re
from typing import List, Dict, Optional
from utils.validador import normalizar_texto # <--- Importar la nueva función

DATA_FILE = 'data/libros.csv'

def _cargar_libros():
    """Carga todos los libros del CSV."""
    if not os.path.exists(DATA_FILE):
        return []
    libros = []
    with open(DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['anio'] = int(row['anio'])
            row['disponible'] = row['disponible'].lower() == 'true'
            # No normalizamos aquí, la normalización se hace en la búsqueda
            libros.append(row)
    return libros

def _imprimir_libros(libros: List[Dict]):
    """Imprime una lista de libros en un formato legible."""
    if not libros:
        print("No se encontraron libros.")
        return
    for libro in libros:
        estado = "Disponible" if libro['disponible'] else "Prestado"
        print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['anio']}, Estado: {estado}")

def buscar_libros_por_titulo(titulo_busqueda: str):
    """Busca libros por título exacto o parcial, con búsqueda flexible."""
    libros = _cargar_libros()
    resultados = []
    # Normalizar la entrada del usuario para la búsqueda
    busqueda_normalizada = normalizar_texto(titulo_busqueda)
    regex = re.compile(busqueda_normalizada, re.IGNORECASE)

    for libro in libros:
        # Normalizar el título del libro en el registro antes de comparar
        titulo_libro_normalizado = normalizar_texto(libro['titulo'])
        if regex.search(titulo_libro_normalizado):
            resultados.append(libro)
    _imprimir_libros(resultados)

def buscar_libros_por_autor(autor_busqueda: str):
    """Busca libros por autor, con búsqueda flexible."""
    libros = _cargar_libros()
    resultados = []
    # Normalizar la entrada del usuario para la búsqueda
    busqueda_normalizada = normalizar_texto(autor_busqueda)
    regex = re.compile(busqueda_normalizada, re.IGNORECASE)

    for libro in libros:
        # Normalizar el autor del libro en el registro antes de comparar
        autor_libro_normalizado = normalizar_texto(libro['autor'])
        if regex.search(autor_libro_normalizado):
            resultados.append(libro)
    _imprimir_libros(resultados)

def ver_todos_los_libros(solo_disponibles: bool = False):
    """Muestra un listado general de libros, opcionalmente filtrado por disponibilidad."""
    libros = _cargar_libros()
    if solo_disponibles:
        libros = [libro for libro in libros if libro['disponible']]
    _imprimir_libros(libros)