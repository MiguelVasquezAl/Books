import csv
import os
from typing import List, Dict
from utils.decoradores import log_action

DATA_FILE = 'data/libros.csv'
HEADERS = ["id", "titulo", "autor", "anio", "disponible"]

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
            libros.append(row)
    return libros

def _guardar_libros(libros: List[Dict]):
    """Guarda la lista de libros en el CSV."""
    with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(libros)

@log_action("registrar_prestamo")
def registrar_prestamo(id_libro: str):
    """Registra el préstamo de un libro."""
    libros = _cargar_libros()
    encontrado = False
    for libro in libros:
        if libro['id'] == id_libro:
            if libro['disponible']:
                libro['disponible'] = False
                print(f"✔ Libro '{libro['titulo']}' (ID: {id_libro}) prestado correctamente.")
            else:
                print(f"⚠️ El libro '{libro['titulo']}' (ID: {id_libro}) no está disponible para préstamo.")
            encontrado = True
            break
    if not encontrado:
        print(f"⚠️ No se encontró ningún libro con el ID: {id_libro}")
    _guardar_libros(libros)

@log_action("registrar_devolucion")
def registrar_devolucion(id_libro: str):
    """Registra la devolución de un libro."""
    libros = _cargar_libros()
    encontrado = False
    for libro in libros:
        if libro['id'] == id_libro:
            if not libro['disponible']:
                libro['disponible'] = True
                print(f"✔ Libro '{libro['titulo']}' (ID: {id_libro}) devuelto correctamente.")
            else:
                print(f"⚠️ El libro '{libro['titulo']}' (ID: {id_libro}) ya está disponible.")
            encontrado = True
            break
    if not encontrado:
        print(f"⚠️ No se encontró ningún libro con el ID: {id_libro}")
    _guardar_libros(libros)