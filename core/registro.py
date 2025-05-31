import csv
import os
from utils.validador import validar_libro, id_existe
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

def _guardar_libros(libros):
    """Guarda la lista de libros en el CSV."""
    with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(libros)

@log_action("agregar_libro")
def agregar_libro(id_libro: str, titulo: str, autor: str, anio: int):
    """Agrega un nuevo libro al sistema."""
    if not validar_libro(titulo, autor, anio):
        return

    if id_existe(id_libro):
        print(f"⚠️ El ID '{id_libro}' ya existe. No se puede agregar el libro.")
        return

    libros = _cargar_libros()
    nuevo_libro = {
        "id": id_libro,
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "disponible": True
    }
    libros.append(nuevo_libro)
    _guardar_libros(libros)
    print("✔ Libro agregado correctamente.")