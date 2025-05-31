import csv
import os
import random
import string
from typing import Dict
import unicodedata 

DATA_FILE = 'data/libros.csv'

def validar_libro(titulo: str, autor: str, anio: int) -> bool:
    """Valida los campos de un libro."""
    if not titulo or not autor:
        print("⚠️ El título y el autor no pueden estar vacíos.")
        return False
    if not isinstance(anio, int) or anio < 1800:
        print("⚠️ El año debe ser un número entero mayor o igual a 1800.")
        return False
    return True

def _cargar_ids_existentes() -> set:
    """Carga todos los IDs existentes del CSV."""
    if not os.path.exists(DATA_FILE):
        return set()
    ids = set()
    with open(DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ids.add(row['id'])
    return ids

def id_existe(id_libro: str) -> bool:
    """Verifica si un ID de libro ya existe."""
    return id_libro in _cargar_ids_existentes()

def generar_id_unico() -> str:
    """Genera un ID único para un nuevo libro."""
    existing_ids = _cargar_ids_existentes()
    while True:
        # Genera un ID de 5 caracteres alfanuméricos
        new_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if new_id not in existing_ids:
            return new_id

def normalizar_texto(texto: str) -> str:
    """
    Normaliza el texto: lo convierte a minúsculas, elimina acentos y
    caracteres especiales, y limpia espacios extra.
    """
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar acentos y caracteres especiales (ñ -> n, á -> a)
    # NFC normaliza y luego se eliminan caracteres no ASCII (excepto letras y números)
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    # Remover caracteres que no sean letras, números o espacios (opcional, para más flexibilidad)
    # texto = re.sub(r'[^a-z0-9\s]', '', texto) # No lo aplicaremos por ahora para no perder flexibilidad
    # Limpiar múltiples espacios y espacios al inicio/final
    texto = ' '.join(texto.split()).strip()
    return texto