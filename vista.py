from modul import obtener_libros

def mostrar_libros():
  libros=obtener_libros()
  for libro in libros:
    print(f"ID: {libro['id']} , titulo: {libro['titulo']},autor: {libro['autor']}")