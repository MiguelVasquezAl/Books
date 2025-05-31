import os
from core.registro import agregar_libro
from core.busqueda import buscar_libros_por_titulo, buscar_libros_por_autor, ver_todos_los_libros
from core.prestamos import registrar_prestamo, registrar_devolucion
from utils.validador import generar_id_unico

def mostrar_menu():
    print("\nBienvenido al sistema de biblioteca 📚")
    print("1. Ver todos los libros")
    print("2. Buscar libro por título")
    print("3. Buscar libro por autor")
    print("4. Agregar nuevo libro")
    print("5. Registrar préstamo")
    print("6. Registrar devolución")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("> ")

        if opcion == '1':
            disponibles_only = input("¿Mostrar solo libros disponibles? (s/n): ").lower() == 's'
            ver_todos_los_libros(disponibles_only)
        elif opcion == '2':
            titulo = input("Ingrese el título (o parte del título) a buscar: ")
            buscar_libros_por_titulo(titulo)
        elif opcion == '3':
            autor = input("Ingrese el autor a buscar: ")
            buscar_libros_por_autor(autor)
        elif opcion == '4':
            id_libro = generar_id_unico()
            titulo = input("Título: ")
            autor = input("Autor: ")
            while True:
                try:
                    anio = int(input("Año: "))
                    break
                except ValueError:
                    print("⚠️ El año debe ser un número entero.")
            agregar_libro(id_libro, titulo, autor, anio)
        elif opcion == '5':
            id_libro = input("Ingrese el ID del libro a prestar: ")
            registrar_prestamo(id_libro)
        elif opcion == '6':
            id_libro = input("Ingrese el ID del libro a devolver: ")
            registrar_devolucion(id_libro)
        elif opcion == '7':
            print("¡Gracias por usar el sistema de biblioteca!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    main()